def get_price(count: int) -> int:
	"""
		Возвращает цену за товар

		:param count: - количество товара
		:return int:
	"""
	response = 0
	for i in range(count):
		response += 2.95 if response else 10.95

	return round(response,2)

if __name__ == "__main__":
	print(f"Цена за товары: ${get_price(count=int(input('Кол-во товаров: ')))}")