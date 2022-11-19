from pprint import pprint as pp
import os
import glob


country_to_capital = {
    'United Kingdom': 'London',
    'Brazil': 'Brasilia',
    'Morocco': 'Rabat',
    'Sweden': 'Stockholm'
}
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
print(capital_to_country)  # {'London': 'United Kingdom', 'Brasilia': 'Brazil', 'Rabat': 'Morocco', 'Stockholm': 'Sweden'}
pp(capital_to_country)
"""
{'Brasilia': 'Brazil',
 'London': 'United Kingdom',
 'Rabat': 'Morocco',
 'Stockholm': 'Sweden'}
"""


file_size = {os.path.realpath(p):os.stat(p).st_size for p in glob.glob('*.py')}
pp(file_size)
"""
{'/Users/Rail.zakirov/PycharmProjects/PluralSight/01_Getting_started/09_iterations_and_iterables/List_set_comprehensions.py': 331,
 '/Users/Rail.zakirov/PycharmProjects/PluralSight/01_Getting_started/09_iterations_and_iterables/dictianary_comprehensions.py': 627}
"""
