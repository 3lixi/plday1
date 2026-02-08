"""
PL202 - Day 1 (Period 2) Starter File
Task: Cloud Log Cleaner + JSON Summary (Mini Project)

You will:
1) Read logs.txt
2) Keep ONLY valid lines (4 parts AND level is INFO/WARN/ERROR)
3) Write clean logs to clean_logs.txt (same original format)
4) Create summary.json with:
   - total_lines, valid_lines, invalid_lines
   - levels: counts of INFO/WARN/ERROR (valid only)
   - top_services: top 3 services by valid log count
   - top_errors: top 3 ERROR messages by count (valid ERROR only)

IMPORTANT:
- Work independently (no teacher / classmates).
- You may copy your solutions from Period 1.
"""

import json
from pathlib import Path
from collections import Counter

LOG_FILE = Path("logs.txt")
CLEAN_FILE = Path("clean_logs.txt")
SUMMARY_FILE = Path("summary.json")

ALLOWED_LEVELS = {"INFO", "WARN", "ERROR"}


def parse_line(line: str):
    """
    Returns (timestamp, level, service, message) OR None if format invalid.
    """
    # Step 1: Removes spaces/newlines
    line = line.strip()
    if not line:
        return None

    # Step 2: Split by '|'
    parts = [p.strip() for p in line.split("|")]

    # Step 3: Must have exactly 4 parts
    if len(parts) != 4:
        return None

    # Step 4: Returns the 4 parts
    return tuple(parts)


def normalize_level(level: str) -> str:
    # Step 5: Makes level uppercase
    return level.upper()


def main():
    if not LOG_FILE.exists():
        print(f"ERROR: Could not find {LOG_FILE}. Make sure logs.txt is in the same folder.")
        return

    # Step 6: Starts counters
    total_lines = 0
    valid_lines = 0
    invalid_lines = 0
    level_counts = {"INFO": 0, "WARN": 0, "ERROR": 0}
    service_counter = Counter()
    error_message_counter = Counter()
    clean_lines = []  # store valid lines

    # Step 7: Reads logs.txt line by line
    with open(LOG_FILE, "r") as f:
        for line in f:
            total_lines += 1
            parsed = parse_line(line)

            if parsed is None:
                invalid_lines += 1
                continue

            timestamp, level, service, message = parsed
            level = normalize_level(level)

            if level not in ALLOWED_LEVELS:
                invalid_lines += 1
                continue

            # Step 8: Counts the valid lines
            valid_lines += 1
            level_counts[level] += 1
            service_counter[service] += 1
            if level == "ERROR":
                error_message_counter[message] += 1

            # Step 9: Saves cleaned line format
            clean_lines.append(f"{timestamp} | {level} | {service} | {message}")

    # Step 10: Write clean_logs.txt
    with open(CLEAN_FILE, "w") as cf:
        for cl in clean_lines:
            cf.write(cl + "\n")

    # Step 11: Builds summary dictionary
    summary = {
        "total_lines": total_lines,
        "valid_lines": valid_lines,
        "invalid_lines": invalid_lines,
        "levels": level_counts,
        "top_services": [{"service": s, "count": c} for s, c in service_counter.most_common(3)],
        "top_errors": [{"message": m, "count": c} for m, c in error_message_counter.most_common(3)],
    }

    # Step 12: Saves summary.json
    with open(SUMMARY_FILE, "w") as sf:
        json.dump(summary, sf, indent=2)

    # Step 13: Prints summary for quick check
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
