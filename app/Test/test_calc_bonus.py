from calc_bonus import calculate_bonuses

def test_calculate_bonuses():
    result = calculate_bonuses(1_000)

    assert 50 == result

