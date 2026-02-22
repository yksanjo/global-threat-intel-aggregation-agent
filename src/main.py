from datetime import datetime, timezone


def main() -> None:
    print("global-threat-intel-aggregation-agent initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
