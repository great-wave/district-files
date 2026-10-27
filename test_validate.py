from validate import check_district


def fake_response(n):
    """Build a fake ArcGIS response with n features (only the count matters)."""
    feature = {"attributes": {"NAME": "Example"}, "geometry": {"rings": [[[0, 0], [1, 0], [1, 1], [0, 0]]]}}
    return {"features": [feature] * n}


def test_enough_records_passes():
    # senate expects at least 5
    assert check_district("senate", fake_response(6)) == []


def test_too_few_records_fails():
    problems = check_district("senate", fake_response(2))
    assert problems == ["senate: 2 records, expected at least 5"]


def test_missing_features_fails():
    problems = check_district("senate", {"error": {"code": 400}})
    assert problems == ["senate: response has no 'features' key"]