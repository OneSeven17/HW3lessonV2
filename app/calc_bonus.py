def calculate_bonuses(the_sum_of_current_purchase):

    the_sum_of_previous_purchases = 0
    blue_card_percent = 0.05
    silver_card_percent = 0.07
    gold_card_percent = 0.1
    magic_number = 1000 #бонусы начисляются за каждые 1000 руб, поэтому вводим данную переменную
    the_sum_of_all_purchases = the_sum_of_previous_purchases + the_sum_of_current_purchase

    if the_sum_of_all_purchases <1_000:
        bonus_for_purchase = 0
    if 1_000 <= the_sum_of_all_purchases <= 15_000:
        bonus_for_purchase = int(the_sum_of_current_purchase / magic_number) * blue_card_percent * magic_number

    if 15_001 <= the_sum_of_all_purchases < 150_000:
        bonus_for_purchase = int(the_sum_of_current_purchase / magic_number) * silver_card_percent * magic_number

    if the_sum_of_all_purchases >= 150_000:
        bonus_for_purchase = int(the_sum_of_current_purchase / magic_number) * gold_card_percent * magic_number

    return bonus_for_purchase

print(calculate_bonuses(150_000))
print(calculate_bonuses(15_000))
print(calculate_bonuses(1_000))
print(calculate_bonuses(900))
print(calculate_bonuses(1_100))
