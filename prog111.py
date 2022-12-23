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
	try:
		count = int(input("Количество студентов: "))
	except ValueError:
		print("Количество студентов должно быть целочисленным")
		get_students()
	response = []
	for i in range(1,count+1):
		response.append(input_student(i))
	return response

if __name__ == "__main__":
	students = get_students()
	dvoechniki = []
	troechniki = []
	horoshisty = []
	otlichniki = []
	for surname, marks in students:
		student = []
		student.append(surname)
		student+=marks
		if 2 in marks or 1 in marks:
			dvoechniki.append(student)
		elif 3 in marks:
			troechniki.append(student)
		elif 4 in marks:
			horoshisty.append(student)
		else:
			otlichniki.append(student)
	headers = ['Фамилия', 'Математика', 'Русский', 'Английский', 'Информатика']
	print('Двоечники')
	write_csv(headers, sorted(dvoechniki, key=lambda x:x[0]))
	print('Троечники')
	write_csv(headers, sorted(troechniki, key=lambda x:x[0]))
	print('Хорошисты')
	write_csv(headers, sorted(horoshisty, key=lambda x:x[0]))
	print('Отличники')
	write_csv(headers, sorted(otlichniki, key=lambda x:x[0]))