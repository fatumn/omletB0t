import json
import os
import random

banWordsPath = "settings\\banWords.json"
helloWordsPath = "settings\\helloMessages.json"
autoMessagesPath = "settings\\autoMessages.json"
intervalSetting = "settings\\interval.json"
firstMessagePath = "settings\\firstMessage.json"

print("\nПривет, это программа настройки бота для стримов на платформе Omlet Arcade")
print("Что-бы продолжить, выбери действие:\n")
print("\t1 - Настройка плохих сообщений, на которые бот будет отвечать (BanWords)")
print("\t2 - Настройка приветственных сообщений, на которые бот будет отвечать приветствием (ку,привет,здарова и т.д.)")
print("\t3 - Настройка автоматических сообщений, которые будут выводится со временем")
print("\t4 - Настройка интервала авто-сообщений")
print("\t5 - Очистить одну из баз-данных")
print("\t6 - Настроить первое сообщение, которое будет выводится при старте бота")
print("\n[!] В случае, если вы введёте число, которого нет в списке настроек, программа закроется!")

choose = str(input("[?] Ваш выбор: "))


if "1" in choose:
	print("[*] Начинаем настройку бан-вордов...")

	try:
		with open(banWordsPath, 'r') as bW:
			banWords = json.load(bW)
			print("[+] Найден предыдущий список! Продолжаем настройку!")
			bW.close()
	except json.decoder.JSONDecodeError:
		print("[-] Список не найдён, создаём новый...")
		banWords = list()
		print("[+] Готово! Продолжаем настройку!\n")



	print("[*] Вводите по одному слову, как закончите, нажмите Enter с пустым полем.")

	banWord = str(input("\n[1] Введите слово: "))
	if len(banWord) == 0:
		print("[*] Пока =)")
		exit()
	banWords.append(banWord)
	count = 2
	while True:
		banWord = str(input(f"[{count}] Введите слово: "))
		if len(banWord) == 0:
			if len(banWords) == 0:
				print("[!] Вы не записали ни одного слова!")
			else:
				with open(banWordsPath, 'w') as bW:
					json.dump(banWords, bW)
					print("[+] Бан-ворды загружены!")
			print("[*] Пока =)")
			exit()
		banWords.append(banWord)
		count+= 1
elif "2" in choose:
	print("[*] Начинаем настройку приветственных сообщений...")

	try:
		with open(helloWordsPath, 'r') as hWP:
			helloWords = json.load(hWP)
			print("[+] Найден предыдущий список! Продолжаем настройку!")
			hWP.close()
	except json.decoder.JSONDecodeError:
		print("[-] Список не найдён, создаём новый...")
		helloWords = list()
		print("[+] Готово! Продолжаем настройку!\n")



	print("[*] Вводите по одному слову, как закончите, нажмите Enter с пустым полем.")

	helloWord = str(input("\n[1] Введите слово: "))
	if len(helloWord) == 0:
		print("[*] Пока =)")
		exit()
	helloWords.append(helloWord)
	count = 2
	while True:
		helloWord = str(input(f"[{count}] Введите слово: "))
		if len(helloWord) == 0:
			if len(helloWords) == 0:
				print("[!] Вы не записали ни одного слова!")
			else:
				with open(helloWordsPath, 'w') as bW:
					json.dump(helloWords, bW)
					print("[+] Сообщения, на которые будет отвечать бот приветствием загружены!")
			print("[*] Пока =)")
			exit()
		helloWords.append(helloWord)
		count+= 1
elif "3" in choose:
	print("[*] Начинаем настройку авто-сообщений...")

	try:
		with open(autoMessagesPath, 'r') as aM:
			autoMessages = json.load(aM)
			print("[+] Найден предыдущий список! Продолжаем настройку!")
			aM.close()
	except json.decoder.JSONDecodeError:
		print("[-] Список не найдён, создаём новый...")
		autoMessages = list()
		print("[+] Готово! Продолжаем настройку!\n")



	print("[*] Вводите по одному сообщению, как закончите, нажмите Enter с пустым полем.")

	autoMessage = str(input("\n[1] Введите сообщение: "))
	if len(autoMessage) == 0:
		print("[*] Пока =)")
		exit()
	autoMessages.append(autoMessage)
	count = 2
	while True:
		autoMessage = str(input(f"[{count}] Введите сообщение: "))
		if len(autoMessage) == 0:
			if len(autoMessages) == 0:
				print("[!] Вы не записали ни одного сообщения!")
			else:
				with open(autoMessagesPath, 'w') as aM:
					json.dump(autoMessages, aM)
					print("[+] Сообщения, на которые будет отвечать бот приветствием загружены!")
			print("[*] Пока =)")
			exit()
		autoMessages.append(autoMessage)
		count+= 1
elif "4" in choose:
	intval = int(input("[?] Введите интервал между авто-сообщениями в секундах: "))
	with open(intervalSetting, 'w') as iS:
		json.dump(intval, iS)
		iS.close()
elif "5" in choose:
	os.system("cls")
	print("1 - Очистить бан-ворды")
	print("2 - Очистить приветственные сообщения")
	print("3 - Очистить авто-сообщения\n")
	choose_2 = input("[?] Ваш выбор: ")
	if "1" in choose_2:
		rand = random.randint(1000,10000)
		print(f"[!] Это действие нельзя будет отменить, если вы уверенны, введите число {rand}")
		randAccept = int(input("[?] Подтвердить: "))
		if randAccept == rand:
			clear = list()
			with open(banWordsPath, 'w') as bW:
				json.dump(clear, bW)
				print("[-] База уничтожена.")
				bW.close()
	elif "2" in choose_2:
		rand = random.randint(1000,10000)
		print(f"[!] Это действие нельзя будет отменить, если вы уверенны, введите число {rand}")
		randAccept = int(input("[?] Подтвердить: "))
		if randAccept == rand:
			clear = list()
			with open(helloWordsPath, 'w') as hWP:
				json.dump(clear, hWP)
				print("[-] База уничтожена.")
				hWP.close()
	elif "3" in choose_2:
		rand = random.randint(1000,10000)
		print(f"[!] Это действие нельзя будет отменить, если вы уверенны, введите число {rand}")
		randAccept = int(input("[?] Подтвердить: "))
		if randAccept == rand:
			clear = list()
			with open(autoMessagesPath, 'w') as aMP:
				json.dump(clear, aMP)
				print("[-] База уничтожена.")
				aMP.close()
elif "6" in choose:
	print("[*] Начинаем настройку первого сообщения...")

	try:
		with open(firstMessagePath, 'r') as fM:
			firstMessages = json.load(fM)
			print("[+] Найден предыдущий список! Продолжаем настройку!")
			print("[!] Внимание! Если вы продолжите настройку, прошлое сообщение будете перезаписано!")
			fM.close()
	except json.decoder.JSONDecodeError:
		print("[-] Список не найдён, создаём новый...")
		firstMessages = list()
		print("[+] Готово! Продолжаем настройку!\n")


	firstMessage = str(input("\n[?] Введите сообщение: "))
	if len(firstMessage) == 0:
		print("[*] Пока =)")
		exit()
	firstMessages.append(firstMessage)
	if len(firstMessages) == 0:
		print("[!] Вы не записали ни одного сообщения!")
	else:
		with open(firstMessagePath, 'w') as fM:
			json.dump(firstMessages, fM)
			print("[+] Стартовое сообщение загруженно!")
	print("[*] Пока =)")
	exit()
