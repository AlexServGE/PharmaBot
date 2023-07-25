from Controller import Controller
import datetime

start_time = datetime.datetime.now()
print(f'Начало сбора - {start_time}')
controller = Controller()

finish_time = datetime.datetime.now()
print(f'Окончание сбора - {finish_time}. Длительность - {finish_time - start_time}')

"""Комментарии:
1 Необходимо изменить VARCHAR для дат, сумм


"""
