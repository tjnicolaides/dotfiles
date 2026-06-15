# Ioniq 5 (Bluelink) → HomeKit auto-lock

Connect a Hyundai Ioniq 5 to Apple HomeKit via Home Assistant, and auto-lock the
car when it sits in the driveway for a minimum time.

## Why this design

No official public Bluelink API exists. The maintained reverse-engineered path is
the Python lib [`hyundai_kia_connect_api`](https://github.com/Hyundai-Kia-Connect/hyundai_kia_connect_api),
consumed by the Home Assistant HACS integration
[`kia_uvo`](https://github.com/Hyundai-Kia-Connect/kia_uvo). Home Assistant gives
both the integration *and* a real automation engine ("in driveway for N min"),
then re-exposes the car to Apple Home via its built-in HomeKit Bridge — so it
shows up next to the always-on Apple TV hub.

Homebridge plugins (`bluelinky`) are unmaintained and report breakage on newer
ccNC Ioniq 5s. Avoided.

```
Bluelink cloud ──kia_uvo/HACS──> Home Assistant ──HomeKit Bridge──> Apple Home (Apple TV = hub)
                                       │
                                       └─ automation: car in driveway zone ≥N min AND unlocked → lock
```

## ⚠️ Caveats for THIS car (2024+ ccNC, USA)

- **ccNC cars get pinged on every read.** On ccNC, even "cached" reads wake the
  car ([kia_uvo #1050](https://github.com/Hyundai-Kia-Connect/kia_uvo/issues/1050)),
  so frequent polling drains the **12V battery**. Use a long scan interval, keep
  force-refresh off, respect a night window. Reaction is minutes, not seconds.
- **USA support is "limited"** and Hyundai login changes (reCAPTCHA / 400s) can
  break plain user+pass, sometimes needing a manual refresh-token flow.
- **GPS isn't curb-accurate.** Use a generous driveway zone radius.
- **Unofficial API** — small risk of throttling/flagging.

## Steps (do them in order)

### 0. Validate auth FIRST — this is a gate
Don't build anything until the car authenticates and responds.

```bash
cd ioniq5-homekit
python3 -m venv .venv && source .venv/bin/activate   # pyenv: see CLAUDE.md
pip install -r requirements.txt
cp .env.example .env        # fill in BLUELINK_USERNAME / PASSWORD / PIN
python validate_bluelink.py # add --lock only after read works, to test a command
```

Pass = authenticates, lists the Ioniq 5, returns lock state + location.
Fail on auth / car not listed = STOP. Reassess (manual token flow) before Docker.

### 1. Home Assistant via Docker (Windows laptop / WSL2)
```bash
docker compose up -d   # see docker-compose.yml
```
Open `http://localhost:8123`, complete onboarding.

### 2. Install kia_uvo
Install HACS, then add the **Kia Uvo / Hyundai Bluelink** integration. Configure
region USA, brand Hyundai, your creds. Set a long scan interval; disable
aggressive force-refresh (ccNC battery).

### 3. Define the driveway zone
HA → Settings → Areas & Zones → add `Driveway` at your coordinates with a
generous radius (~100m to absorb GPS error).

### 4. Auto-lock automation
Copy `homeassistant/automations/auto_lock.yaml` into your HA config and fix the
entity ids / `LOCK_AFTER_MINUTES`.

### 5. Expose to HomeKit
HA → Settings → Devices & Services → add **HomeKit Bridge**, include the car's
lock. Scan the QR in Apple Home; the Apple TV acts as hub.
