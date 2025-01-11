from datetime import *

#получение и вывод сегодняшней даты в нужном формате
current_date_obj=datetime.now()
current_date = current_date_obj.strftime("%d-%m-%Y")
print("Текущая дата:",current_date)

#ввод пользователем даты дедлайна и проверка ее коректности
while True:
    try:
        issue_date_str=input("Введите дату дедлайна в формате дд-мм-гггг: ")
        issue_date_obj = datetime.strptime(issue_date_str, "%d-%m-%Y")
        break
    except:
        print("Неверный формат даты. Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024")

date_difference=abs((issue_date_obj-current_date_obj).days) #расчитывает разницу между датами

#проверка дедлайнов
if issue_date_str==current_date:
    print("Дедлайн сегодня!")
elif issue_date_obj<current_date_obj:
    print("Дедлайн истёк",date_difference,"день(дня) назад.")
else:
    print("До дедлайна осталось",date_difference,"дня(дней).")