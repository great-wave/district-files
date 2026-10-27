import sys

# A little below the counts in logs/run_log.csv (13, 42, 15, 18, 99, 6, 5).
EXPECTED_MIN_RECORDS = {
    "assembly": 10, "bids_city_clerk": 30, "city_council": 12,
    "congressional": 15, "neighborhood_council": 90, "senate": 1000, "supervisors": 5,
}

def check_district(district, data):
    """Return a list of problems found in one district's response."""
    features = data.get("features")
    if features is None:
        return [f"{district}: response has no 'features' key"]
    minimum = EXPECTED_MIN_RECORDS.get(district, 1)
    if len(features) < minimum:
        return [f"{district}: {len(features)} records, expected at least {minimum}"]
    return []

def fail_if_problems(problems):
    """Exit non-zero so GitHub Actions marks the run as failed."""
    if problems:
        print("[VALIDATION FAILED]", *problems, sep="\n  - ")
        sys.exit(1)
    print("[VALIDATION PASSED]")