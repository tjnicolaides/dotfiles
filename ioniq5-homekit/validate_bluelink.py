#!/usr/bin/env python3
"""Step 0 gate: prove the car authenticates and responds before building HA.

Reads credentials from .env. By default only READS (auth + list + lock state +
location). Pass --lock to send one real lock command (wakes the car).
"""
import argparse
import os
import sys

from dotenv import load_dotenv
from hyundai_kia_connect_api import VehicleManager


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lock",
        action="store_true",
        help="send a real lock command to test write access (wakes the car)",
    )
    args = parser.parse_args()

    load_dotenv()
    try:
        username = os.environ["BLUELINK_USERNAME"]
        password = os.environ["BLUELINK_PASSWORD"]
        pin = os.environ["BLUELINK_PIN"]
        region = int(os.environ.get("BLUELINK_REGION", "3"))
        brand = int(os.environ.get("BLUELINK_BRAND", "2"))
    except KeyError as exc:
        print(f"Missing env var {exc}. Copy .env.example to .env and fill it in.")
        return 2

    vm = VehicleManager(
        region=region, brand=brand, username=username, password=password, pin=pin
    )

    print("Authenticating...")
    vm.check_and_refresh_token()
    print("  ok")

    print("Fetching cached vehicle state...")
    vm.update_all_vehicles_with_cached_state()

    if not vm.vehicles:
        print("No vehicles returned. Auth worked but no car is listed — STOP here.")
        return 1

    for vehicle_id, vehicle in vm.vehicles.items():
        print(f"\nVehicle: {vehicle.name} ({vehicle.model})  id={vehicle_id}")
        print(f"  locked:   {vehicle.is_locked}")
        print(f"  location: {vehicle.location_latitude}, {vehicle.location_longitude}")

        if args.lock:
            print("  sending lock command...")
            vm.lock(vehicle_id)
            print("  lock command sent")

    print("\nGate PASSED. Safe to proceed to Home Assistant setup.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
