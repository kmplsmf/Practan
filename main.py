from tabulate import tabulate
import json

def tabs(headers, data):
	text = ''
	print(headers)

	for i in data:
		text+=','.join([str(y) for y in i])
	with open('file.csv', 'w') as f:
		f.write(text)
	data = [(i['name'], i['desc'], i['prov'], i['price'], i['count']) for i in data]
	print(tabulate(data,headers,tablefmt='grid'))


def log_in(login: str, password: str):
	"""
	Вход в аккаунт
	"""
	with open("users.json") as f:
		users = json.loads(f.read())
	if login not in users:
		print("Логина нет")
		return None
	elif password != users[login]['password']:
		print("Пароли не совпадают")
		return None
	else:
		return users[login]['admin']

def regist(login: str, password: str, retyped_password: str):
	"""
	Регистрация
	"""
	with open("users.json") as f:
		users = json.loads(f.read())

	if login in users:
		print("Логин уже существует")
	elif password != retyped_password:
		print("Пароли не совпадают")
	else:
		users[login] = {'password':password, 'admin':False}
		return False

def get_products():
	"""
	Возвращает товары
	"""
	with open('prod.json') as f:
		products = json.loads(f.read())

	return products

def add_product():
	name = input("name: ")
	desc = input("desc: ")
	prov = input("prov: ")
	price = input("price: ")
	count = input("count: ")
	prods = get_products()
	prods.append({'name':name, 'desc':desc, 'prov':prov, 'price':price, 'count':count})
	with open('prod.json', 'w') as f:
		f.write(json.dumps(prods))

def edit_product():
	prods = get_products()
	for i in range(len(prods)):
		print(f'{i+1}. {prods[i]["name"]}')
	prod = int(input("Номер товара: "))-1
	elem = input("Колонка для редактирования: ")
	val = input("новое значение: ")
	if elem in ['name', 'desc', 'prov', 'count', 'price']:
		try:
			prods[prod][elem] = val
		except:
			print("ошибка изменения")
	else:
		print('несуществующая колонка')

	with open('prod.json', 'w') as f:
		f.write(json.dumps(prods))
	print('succ')

def remove_prod():
	prods = get_products()
	for i in range(len(prods)):
		print(f'{i+1}. {prods[i]["name"]}')
	prod = int(input("Номер товара: "))-1
	try:

		prods.pop(prod)
	except:
		print('bad val')
	with open('prod.json', 'w') as f:
		f.write(json.dumps(prods))
	print('succ')

def show_prods():
	prods = get_products()
	tabs(['name', 'desc', 'prov', 'price', 'count'], prods)

print('авторизация (reg / log)')
avt = input('тип авторизации: ')
status = None
while status == None:
	if avt == 'reg':
		login = input('login: ')
		password = input('passwd: ')
		retyped_password = input('passwd: ')
		status = regist(login,password,retyped_password)

	else:
		login = input('login: ')
		password = input('passwd: ')
		status = log_in(login,password)

while True:
	if status:
		print('1. показать все товары\n2. добавить товары\n3. редактирование товара\n4. Удаление товара')
	else:
		print('1. показать все товары')

	try:
		act = int(input('действие: '))
		if not status and act != 1: raise ValueError
		elif status and act not in range(1,5): raise ValueError
	except ValueError:
		continue

	if act == 1:
		show_prods()
	elif act == 2:
		add_product()
	elif act == 3:
		edit_product()
	else:
		remove_prod()