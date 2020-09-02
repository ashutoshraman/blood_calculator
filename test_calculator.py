import pytest
@pytest.mark.parametrize("num1, expected", [
    (70, "Normal"),
    (45, "borderline low"),
    (5, "low"),
    ])
def test_check_HDL(num1, expected):
    from calculator import check_HDL
    answer= check_HDL(num1)
    assert answer == expected
    #not good if first test fails, since only first one runs
    # you could also make multiple differently named functions to do same conditional testing