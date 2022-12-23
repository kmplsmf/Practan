def taxi(distance: int) -> int:
	"""
		Возвращает цену поездки в такси

		:param distance: - расстояние поездки
		:return int:
	"""
	response = 4
	response += 0.25*(distance//140) + (0.25 if distance % 140 != 0 else 0)
	return response
distance = int(input("Введите дистанцию поездки: "))
if __name__ == "__main__":
	print(f"Цена поездки составит ${taxi(distance=distance)}")