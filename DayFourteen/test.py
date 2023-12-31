import random
countries = [
    {"country": "USA", "population": 331002651},
    {"country": "China", "population": 1439323776},
    {"country": "India", "population": 1380004385},
    {"country": "Brazil", "population": 212559417},
    {"country": "Russia", "population": 145934462}
]

random_country = random.choice(countries)
print(random_country["country"])
