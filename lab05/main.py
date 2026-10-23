from pathlib import Path

from logstats import parse_event, count_levels, top_errors, format_report

def main():
    filename = input().strip()
    log_path = Path(filename)

    with log_path.open("r", encoding="utf-8") as log:
        counts = count_levels(log)

    with log_path.open("r", encoding="utf-8") as log:
        errors = top_errors(log, 3)

    total = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    print(total)
    print(error_count)
    print(broken_count)

    report = format_report(counts, errors)
    report_path = Path(__file__).resolve().parent / "report.txt"

    with report_path.open("w", encoding="utf-8") as file:
        file.write(report)


if __name__ == "__main__":
    main()
