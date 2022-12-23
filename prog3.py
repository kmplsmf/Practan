def is_prime(num: int) -> bool:
	"""
		Возвращает True, если число является простым, False в ином случае

		:param num: - проверяемое число
		:return bool:
	"""
	return len([i for i in range(1,num+1) if num % i == 0]) == 2

if __name__ == "__main__":
	print(is_prime(num=int(input("Введите число: "))))