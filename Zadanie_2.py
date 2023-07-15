# Максим Мусулезный 15.07.2023
# Напишите однострочный генератор словаря.
# Который принимает на вход три списка одинаковой длины:
# Имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

def generate_salary_dict(names_list, salaries_list, bonuses_list):
    return {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary, bonus in zip(names_list, salaries_list, bonuses_list)}

names = ["Максим", "Мария", "Роман"]
salaries = [10000, 15000, 20000]
bonuses = ["10%", "15%", "20%"]

salary_dict = generate_salary_dict(names, salaries, bonuses)
print(salary_dict)