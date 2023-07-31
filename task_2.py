# Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа
# и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def award_gen(names: list, salaries: list, awards: list) -> dict:
    yield {names: salaries / 100 * awards for names, salaries, awards in
        zip(names, salaries, (float(i[:-1]) for i in awards))}


my_names = ['Alex', 'Gael', 'Yarik']
my_salaries = [6000, 2000, 4000]
my_awards = ['10.25%', '8.5%', '9.9%']

print(*award_gen(my_names, my_salaries, my_awards))

