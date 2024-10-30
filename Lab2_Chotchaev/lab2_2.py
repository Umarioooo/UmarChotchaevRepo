money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months = 0
current_spend = spend

while money_capital + salary >= current_spend:
    months += 1
    money_capital += salary - current_spend
    current_spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)
