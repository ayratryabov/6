#black blue white
#pidj
from random import *
print('У юноши вещи 3 цветов,черные , синие и белые')
JAKET = []

def input_1():
    global lot_jak
    lot_jak = int(input('Введите кол-во пиджаков: '))
    if lot_jak < 0:
        print('Введите положительное значение ')
        input_1()
input_1()
def jaket():
    if lot_jak == 0:
        return JAKET.append('Пиджаков нет')
    quest_Jak = int(input("Выберите цвет: 1-черный,2-синий,3-белый "))
    if quest_Jak == 0 or quest_Jak > 3:
        print('Вы ввели неккоректную цифру,попробуйте еще раз!')
        jaket()
    
   
    black_jak =  lot_jak//3 #1
    blue_jak = (lot_jak - black_jak)//2 #2
    white_jak = (lot_jak - black_jak)-blue_jak  #3
    
    if quest_Jak == 1:
        for i in range(1,black_jak+1):
            JAKET.append(f'Пиджак{i}   ')
        if lot_jak == 1 or lot_jak == 2:
            JAKET.append(f"Пиджак1   ")
    elif quest_Jak == 2:
        if lot_jak == 1:
            JAKET.append('Пиджак1 ')
        if lot_jak == 2:
            JAKET.append('Пиджак2   ')
        else:
            for i in range(black_jak+1,(black_jak+blue_jak)+1):
                JAKET.append(f'Пиджак{i}   ')
        
    elif quest_Jak == 3:
        if lot_jak == 1 or lot_jak == 2:
                JAKET.append('Пиджак1')
        else:
            for i in range((black_jak+blue_jak)+1,black_jak+blue_jak+white_jak+1):
                JAKET.append(f'Пиджак{i}   ')
    fasons = ['Классический ','Спортивный ','Френч ','Блейзер ','Смокинг ']
    
    for i in range(len(JAKET)):
        JAKET[i] = choice(fasons) + JAKET[i]
jaket()   

 
TIES = []  
def input_2():
    global lot_tie
    lot_tie = int(input('Введите кол-во галстуков: '))
    if lot_tie < 0:
        print('Введите положительное значение ')
        input_2()
input_2()     
#galst
def ties():
    if lot_tie == 0:
        return TIES.append('Галстуков нет')
    quest_Tie = int(input("Выберите цвет: 1-черный,2-синий,3-белый "))
    black_tie =  lot_tie//3 #1
    blue_tie = (lot_tie - black_tie)//2 #2
    white_tie = (lot_tie - black_tie)-blue_tie  #3
    if quest_Tie == 0 or quest_Tie > 3:
        print('Вы ввели неккоректную цифру,попробуйте еще раз!')
        ties()
    
        
    if quest_Tie == 1:
        for i in range(1,black_tie+1):
            TIES.append(f'Галстук{i}   ')
        if lot_tie == 1 or lot_tie == 2:
            TIES.append(f"Галстук1   ")
    elif quest_Tie == 2:
        if lot_tie == 1:
            TIES.append('Галстук1 ')
        if lot_tie == 2:
            TIES.append('Галстук2   ')
        else:
            for i in range(black_tie+1,(black_tie+blue_tie)+1):
                TIES.append(f'Галстук{i}   ')
            
    elif quest_Tie == 3:
        if lot_tie == 1 or lot_tie == 2:
                TIES.append('Галстук1 ')
        else:
            for i in range((black_tie+blue_tie)+1,black_tie+blue_tie+white_tie+1):
                TIES.append(f'Галстук{i}   ')
    fasons = ['Бабочка-','Техасский-','Лаварьер-','Регат-','Скинни-', 'Платок-']
    knots = ['Бальтус-узел: ','Виктория-узел: ','Восточный узел: ','Двойной узел: ','Диагональный узел: ','Кент-узел: ','крестовый узел: ','Манхэттен-узел: ','Никки-узел: ','Простой узел: ']

    for i in range(len(TIES)):
        TIES[i] = choice(fasons) + TIES[i]
    for i in range(len(TIES)):
        TIES[i] = choice(knots) + TIES[i]
ties()    
   
TROU = []
def input_3():
    global lot_t
    lot_t = int(input('Введите кол-во брюк: '))
    if lot_t < 0:
        print('Введите положительное значение ')
        input_3()
input_3() 
#bruki
def trousers():
    if lot_t == 0:
        return TROU.append('брюк нет')
    quest_T = int(input("Выберите цвет: 1-черный,2-синий,3-белый "))
    if quest_T == 0 or quest_T > 3:
        print('Вы ввели неккоректную цифру,попробуйте еще раз!')
        trousers()
    
   
    black_t =  lot_t//3 #1
    blue_t = (lot_t - black_t)//2 #2
    white_t = (lot_t - black_t)-blue_t  #3
    
    if quest_T == 1:
        for i in range(1,black_t+1):
            TROU.append(f'Брюки{i}   ')
        if lot_t == 1 or lot_t == 2:
            TROU.append(f"Брюки1   ")
    elif quest_T == 2:
        if lot_t == 1:
            TROU.append('Брюки1 ')
        if lot_t == 2:
            TROU.append('Брюки2   ')
        else:
            for i in range(black_t+1,(black_t+blue_t)+1):
                TROU.append(f'Брюки{i}   ')
    elif quest_T == 3:
        if lot_t == 1 or lot_t == 2:
                TROU.append('брюки1 ')
        else:
            for i in range((black_t+blue_t)+1,black_t+blue_t+white_t+1):
                TROU.append(f'Брюки{i}   ')

    fasons = ['Классические ','Чинос ','Карго ','Джлггеры ','Бананы ','Скинни ']
    for i in range(len(TROU)):
        TROU[i] = choice(fasons) + TROU[i]
trousers()    
def input_4():
    global lot_tie
    lot_tie = int(input('Введите кол-во рубашек: '))
    if lot_tie < 0:
        print('Введите положительное значение ')
        input_4()
input_4() 
SHIR = []    
#rubashka
def shirts():
    if lot_t == 0:
        return SHIR.append('Рубашек у юноши нет')
    quest_T = int(input("Выберите цвет: 1-черный,2-синий,3-белый "))
    if quest_T == 0 or quest_T > 3:
        print('Вы ввели неккоректную цифру,попробуйте еще раз!')
        shirts()
   
    
    black_t =  lot_t//3 #1
    blue_t = (lot_t - black_t)//2 #2
    white_t = (lot_t - black_t)-blue_t  #3
    
    if quest_T == 1:
        for i in range(1,black_t+1):
            SHIR.append(f'Рубашка{i}   ')
        if lot_t == 1 or lot_t == 2:
            SHIR.append(f"Рубашка1   ")
    elif quest_T == 2:
        if lot_t == 1:
            SHIR.append('Рубашка1   ')
        if lot_t == 2:
            SHIR.append('Рубашка 2   ')
        else:
            for i in range(black_t+1,(black_t+blue_t)+1):
                SHIR.append(f'Рубашка{i}   ')
    elif quest_T == 3:
        if lot_t == 1 or lot_t == 2:
                SHIR.append('Рубашка1   ')
        else:
            for i in range((black_t+blue_t)+1,black_t+blue_t+white_t+1):
                SHIR.append(f'Рубашка{i}   ')
    fasons = ['Свободного фасона ','Классического фасона ','Приталенного фасона ','Современного фасона ']
    
    for i in range(len(SHIR)):
        SHIR[i] = choice(fasons) + SHIR[i]
shirts() 
ALL = []
def all_costum():
    
    ol = []
    for i in JAKET:
        for q in TIES:
            for w in TROU:
                for ii in SHIR:
                    ol.append(i)
                    ol.append(q)
                    ol.append(w)
                    ol.append(ii)
                    ALL.append(ol)
                    ol = []
    

all_costum()


        
#-----------------Целевая функция---------------------------
def price():
    count = 0
    for i in ALL:
        for j in i:
            if j.rstrip()[-1].isdigit() == True:
                if 1<=int(j.rstrip()[-1])<=5:
                    count += randint(5,15)
                elif 5<=int(j.rstrip()[-1])<=15:
                    count += randint(15,25)
                else:
                    count += randint(25,50)
                
            else:
                count += 0
        print(*i,' ',f'цена костюма {count}$',end = '\n')
        count = 0   
price()
