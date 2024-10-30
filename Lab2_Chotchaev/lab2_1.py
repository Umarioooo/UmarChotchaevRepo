salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

months = 10
current_spend = spend
total_deficit = 0

for month in range(months):
    deficit = max(0, current_spend - salary)
    total_deficit += deficit
    current_spend *= (1 + increase)

money_capital = round(total_deficit)
print(money_capital)