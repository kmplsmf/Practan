def get_shorted(num1:int, num2:int) -> tuple:
	"""
		Возвращает сокращенные составные дроби
		:param num1: - Числитель дроби
		:param num2: - Знаменатель дроби
	"""
	for i in reversed(range(1,min(num1,num2)+1)):
		if num1 % i == num2 % i == 0:
			num1/=i
			num2/=i
	return (int(num1),int(num2))

num1 = int(input("Введите числитель: "))
num2 = int(input("Введите знаменатель: "))

response = get_shorted(num1=num1,num2=num2)
if __name__ == "__main__":
	print(response[0], response[1])