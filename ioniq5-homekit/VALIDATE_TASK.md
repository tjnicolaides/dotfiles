# Task: Validate Hyundai Bluelink API access (2024+ Ioniq 5, ccNC, USA)

Validate whether this car authenticates via `hyundai_kia_connect_api` **before** any further build. Do **not** set up Home Assistant, Docker, or anything else — auth check only.

**Context:** Goal is Ioniq 5 → Apple HomeKit via Home Assistant + `hyundai_kia_connect_api`. The gating unknown: newer ccNC cars and US-region support are both flaky, and Hyundai has added reCAPTCHA to login.

**⚠️ ccNC caveat:** even "cached" reads ping the real car and can drain the 12V battery. Do **not** loop or poll. Run the read **once**. Only send a lock command if explicitly told.

## Steps

1. `python3 -m venv .venv && source .venv/bin/activate`
2. `pip install hyundai-kia-connect-api python-dotenv`
3. Create `.env`:
   ```
   BLUELINK_USERNAME=...
   BLUELINK_PASSWORD=...
   BLUELINK_PIN=...
   BLUELINK_REGION=3   # USA
   BLUELINK_BRAND=2    # Hyundai
   ```
4. Run the script below **once** (no `--lock` on first run):

```python
#!/usr/bin/env python3
"""One-shot Bluelink auth gate. READ ONLY unless --lock is passed."""
import argparse, os, sys
from dotenv import load_dotenv
from hyundai_kia_connect_api import VehicleManager

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lock", action="store_true",
                    help="send ONE real lock command (wakes the car)")
    args = ap.parse_args()
    load_dotenv()
    try:
        user = os.environ["BLUELINK_USERNAME"]
        pw   = os.environ["BLUELINK_PASSWORD"]
        pin  = os.environ["BLUELINK_PIN"]
        region = int(os.environ.get("BLUELINK_REGION", "3"))  # USA=3
        brand  = int(os.environ.get("BLUELINK_BRAND", "2"))   # Hyundai=2
    except KeyError as e:
        print(f"Missing env var {e}. Fill in .env."); return 2

    vm = VehicleManager(region=region, brand=brand,
                        username=user, password=pw, pin=pin)
    print("Authenticating..."); vm.check_and_refresh_token(); print("  auth ok")
    print("Fetching cached state (single read)...")
    vm.update_all_vehicles_with_cached_state()
    if not vm.vehicles:
        print("Auth ok but NO vehicles listed — STOP, report this."); return 1
    for vid, v in vm.vehicles.items():
        print(f"\nVehicle: {v.name} ({v.model}) id={vid}")
        print(f"  locked:   {v.is_locked}")
        print(f"  location: {v.location_latitude}, {v.location_longitude}")
        if args.lock:
            print("  sending lock..."); vm.lock(vid); print("  lock sent")
    print("\nGATE PASSED."); return 0

if __name__ == "__main__":
    sys.exit(main())
```

## Report back verbatim

- Did `check_and_refresh_token()` succeed, or what exception / HTTP status? (Watch for 400 / reCAPTCHA / SSL "dh key too small".)
- Was the Ioniq 5 listed? Its name/model/id.
- Lock state and lat/long returned, or `None`?
- Full traceback if anything failed.

Do not troubleshoot beyond reporting. If auth fails with reCAPTCHA/400, note it and stop — that means we need the manual refresh-token flow (separate task).
