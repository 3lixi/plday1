"""
PL202 - Day 1 (Period 1) Starter File
Task: Cloud Log Reader — Parse + Validate + Report (TXT)

You will:
1) Read logs.txt
2) Parse each line into: timestamp | level | service | message
3) Validate:
   - If a line does NOT have exactly 4 parts => invalid line
   - Normalize level to uppercase
   - Allowed levels: INFO, WARN, ERROR
   - Anything else => INVALID_LEVEL
4) Count totals and save the summary to period1_report.txt

IMPORTANT:
- Work independently (no teacher / classmates).
- Only fill the TODO parts. Do not delete other code.
"""

from pathlib import Path

LOG_FILE = Path("logs.txt")
OUTPUT_REPORT = Path("period1_report.txt")

ALLOWED_LEVELS = {"INFO", "WARN", "ERROR"}


def parse_line(line: str):
    """
    Parse one log line.
    Returns (timestamp, level, service, message) OR None if the line is bad.
    """

    # Step 1: Remove spaces and newlines from the line
    line = line.strip()

    # Step 2: If the line is empty, it’s not valid
    if not line:
        return None

    # Step 3: Split the line into parts using '|'
    parts = [p.strip() for p in line.split("|")]

    # Step 4: If we don’t get exactly 4 parts, it’s invalid
    if len(parts) != 4:
        return None

    # Step 5: Return the 4 parts
    return tuple(parts)


def normalize_level(level: str) -> str:
    """Make the log level uppercase."""
    # Step 6: Changes level to uppercase 
    return level.upper()


def main():
    # Step 7: Starts counters to keep track of totals
    total_lines = 0
    invalid_lines = 0

    level_counts = {
        "INFO": 0,
        "WARN": 0,
        "ERROR": 0,
        "INVALID_LEVEL": 0,
    }

    # Step 8: Check if the logs.txt exists
    if not LOG_FILE.exists():
        print(f"ERROR: Could not find {LOG_FILE}. Make sure logs.txt is in the same folder.")
        return

    # Step 9: Opens the logs.txt and reads each line
    with open(LOG_FILE, "r") as f:
        for line in f:
            total_lines += 1  # Count every line

            # Step 10: Try to split the line
            parsed = parse_line(line)

            # Step 11: If the parsing fails, it marks as invalid
            if parsed is None:
                invalid_lines += 1
                continue

            # Step 12: Get the fields and fix the level
            timestamp, level, service, message = parsed
            level = normalize_level(level)

            # Step 13: Count based on the level type
            if level in ALLOWED_LEVELS:
                level_counts[level] += 1
            else:
                level_counts["INVALID_LEVEL"] += 1

    # Step 14: Makes a summary text with all counts
    summary = (
        f"Total lines: {total_lines}\n"
        f"Invalid lines: {invalid_lines}\n"
        f"INFO count: {level_counts['INFO']}\n"
        f"WARN count: {level_counts['WARN']}\n"
        f"ERROR count: {level_counts['ERROR']}\n"
        f"INVALID_LEVEL count: {level_counts['INVALID_LEVEL']}\n"
    )

    # Step 15: Shows the summary on screen
    print(summary)

    # Step 16: Saves the summary into period1_report.txt
    with open(OUTPUT_REPORT, "w") as report:
        report.write(summary)


if __name__ == "__main__":
    main()
