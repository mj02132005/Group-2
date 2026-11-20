is_weekend = input("Weekend? (yes/no): ").lower() == "yes"
is_holiday = input("Holiday? (yes/no): ").lower() == "yes"
print("Day off:", is_weekend or is_holiday)
