import csv

MAX_SPEED = 25
MAX_ALT_JUMP = 10

def check_telemetry(file_path):
    with open(file_path) as f:
        data = list(csv.DictReader(f))

    print("\nZEUS – Telemetry Analysis Report")
    print("=" * 85)
    print(f"{'Time':<6}{'Speed(m/s)':<12}{'AltDiff(m)':<12}"
          f"{'SpeedCheck':<20}{'AltitudeCheck'}")
    print("-" * 85)

    speed_warnings = 0
    alt_warnings = 0

    for i in range(1, len(data)):
        prev = data[i - 1]
        curr = data[i]

        time = curr["time"]
        speed = float(curr["speed"])
        alt_diff = abs(float(curr["alt"]) - float(prev["alt"]))

        speed_status = "OK"
        alt_status = "OK"

        if speed > MAX_SPEED:
            speed_status = "HIGH"
            speed_warnings += 1

        if alt_diff > MAX_ALT_JUMP:
            alt_status = "JUMP"
            alt_warnings += 1

        print(f"{time:<6}{speed:<12.1f}{alt_diff:<12.1f}"
              f"{speed_status:<20}{alt_status}")

    print("-" * 85)
    print("Summary")
    print(f"• Speed warnings   : {speed_warnings}")
    print(f"• Altitude warnings: {alt_warnings}")
    print(f"• Total checks     : {len(data) - 1}")
    print("=" * 85)
    print("Legend: HIGH = speed limit exceeded | JUMP = sudden altitude change\n")



if __name__ == "__main__":
    check_telemetry("data.csv")
