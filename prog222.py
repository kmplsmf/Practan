from tabulate import tabulate
def write_csv(headers: list, data: list):
	"""
	Записывает данные в CSV файл и выводит
	структурированные данные, введенные пользователем

	:param headers: - Заголовки выводимой таблицы
	:param data: - Пользовательские данные
	"""
	print(tabulate(data,headers,tablefmt="grid"))
	with open('response1.csv', 'w') as f:
		for elem in data:
			line = ','.join([str(i) for i in elem])+'\n'
			f.write(line)
def input_student(num: int):
	"""
	Возвращает кортеж студента,
	где первый элемент - фамилия,
	второй - оценка

	:param num: - Номер студента
	"""
	surname = input(f"Фамилия студента №{num}: ")
	marks = []
	while not len(marks):
		for subj in ['Математика', 'Русский', 'Английский', 'Информатика']:
			try:
				marks.append(int(input(f"{subj}: Оценка студента №{num}: ")))
			except:
				marks = []
				print("Оценка должна быть целым числом")
				break
	response = (surname, marks)

	return response
	
def get_students():
	"""
	Функция возвращает массив кортежей, где
	хранятся фамилии студентов и их оценки
	"""
	response = []
	try:
		count = int(input("Количество студентов: "))
	except ValueError:
		print("Количество студентов должно быть целочисленным")
		response = get_students()
	for i in range(1,count+1):
		response.append(input_student(i))
	return response
if __name__ == "__main__":
	response = get_students()
	headers = ["Предмет", "Количество оценок"]
	subjects = ['Математика', 'Русский', 'Английский', 'Информатика']
	data = []
	for num in range(4):
		data.append((subjects[num], len([i[1][num] for i in response if i[1][num] > 2])))
	data.append(("Все предметы", sum(i[1] for i in data)))
	data = sorted(data, key=lambda x: x[1], reverse = True)
	write_csv(headers, data)