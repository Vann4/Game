#Задача, создать игру камень ножницы бумага
print('\nДавайте сыграем в камень ножницы бумага, выберете что-то одно.')
Ruslan = input('\nРуслан выбирает: ').lower()
Timur = input('Тимур выбирает: ').lower()

rock_paper_scissors_game = {'камень': 0, 'ножницы': 1, 'бумага': 2}

Ruslan_value = rock_paper_scissors_game.get(Ruslan)
Timur_value = rock_paper_scissors_game.get(Timur)

if Ruslan_value == None or Timur_value == None:
    print('\nКто-то выбрал не существующий вариант')
elif Ruslan_value == Timur_value: #Ничья
    print('\nНичья')
elif Ruslan_value == 0 and Timur_value == 1: #Камень бьет ножницы
    print('\nПобеждает Руслан')
elif Ruslan_value == 1 and Timur_value == 2: #Ножницы режут бумагу
    print('\nПобеждает Руслан')
elif Ruslan_value == 2 and Timur_value == 0:  #Бумага бьет камень
    print('\nПобеждает Руслан')
else:
    print('\nПобеждает Тимур')