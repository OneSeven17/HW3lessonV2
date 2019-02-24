from calc_bonus import calculate_bonuses


def test_calculate_bonuses_0():
    result = calculate_bonuses(900)

    assert 0 == result

def test_bonus_over_limit():
    result = calculate_bonuses(1_000_000)

    assert 10_000.0 == result

def test_calculate_bonuses_blue():
    result = calculate_bonuses(10_000)

    assert 500.0 == result

def test_calculate_bonuses_silver():
    result = calculate_bonuses(20_000)

    assert 1400.0 == result
