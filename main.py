cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (i for j in range(10**6) for i in cities)
for i in range(20): print(next(gen))