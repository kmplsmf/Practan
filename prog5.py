import random
def car_number() -> str:
	"""
	Вощвращает случайный номерной знак

	:return str:
	"""
	letters = "АВЕКМНОРСТУХ"
	if random.randint(0,1):
		number, letter = 3, 3
	else:
		number, letter = 4, 3

	response = ""
	response += ''.join([random.choice(letters) for i in range(letter)])
	response += ''.join([str(random.choice(range(10))) for i in range(number)])
	return response

if __name__ == "__main__":
	print(car_number())