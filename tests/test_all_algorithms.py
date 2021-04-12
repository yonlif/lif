from cython_api import trial_division, pollards_rho


def test_trial_division_simple_numbers():
    assert trial_division(2) == [2]
    assert trial_division(5) == [5]
    assert trial_division(10) == [2, 5]
    assert trial_division(12) == [2, 2, 3]
    assert trial_division(13) == [13]
    assert trial_division(16) == [2, 2, 2, 2]
    assert trial_division(25) == [5, 5]
    assert trial_division(10403) == [101, 103]


def test_pollards_rho_simple_numbers():
    assert pollards_rho(13) == 13
    assert pollards_rho(10403) == 101
    assert pollards_rho(21019 * 61613) == 21019
