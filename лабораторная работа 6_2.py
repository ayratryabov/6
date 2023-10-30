#black blue white
#pidj
from random import *
print('У юноши вещи разделены на три части по цветам,черный,синий и белый')
JAKET = []

def input_1():
    global lot_jak
    lot_jak = int(input('Введите кол-во пиджаков: '))
    if lot_jak < 0:
        print('Введите положительное значение ')
        input_1()
input_1()
def jaket():
    
    quest_Jak = int(input("Выберите цвет: 1-черный,2-синий,3-белый "))
    if quest_Jak == 0 or quest_Jak > 3:
        print('Вы ввели неккоректную цифру,попробуйте еще раз!')
        jaket()
    
   
    black_jak =  lot_jak//3 #1
    blue_jak = (lot_jak - black_jak)//2 #2
    white_jak = (lot_jak - black_jak)-blue_jak  #3
    if lot_jak == 0:
        JAKET.append('Пиджаков нет')
    if quest_Jak == 1:
        for i in range(1,black_jak+1):
            JAKET.append(f'Пиджак{i}')
        if lot_jak == 1 or lot_jak == 2:
            JAKET.append(f"Пиджак1")
    elif quest_Jak == 2:
        if lot_jak == 1:
            JAKET.append('Cиний пиджак отсутствует')
        if lot_jak == 2:
            JAKET.append('Пиджак 2')
        else:
            for i in range(black_jak+1,(black_jak+blue_jak)+1):
                JAKET.append(f'Пиджак{i}')
        
    elif quest_Jak == 3:
        if lot_jak == 1 or lot_jak == 2:
            JAKET.append('Белый пиджак отсутствует')
        else:
            for i in range((black_jak+blue_jak)+1,black_jak+blue_jak+white_jak+1):
                JAKET.append(f'Пиджак{i}')
    
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
    quest_Tie = int(input("Выберите цвет: 1-черный,2-синий,3-белый "))
    black_tie =  lot_tie//3 #1
    blue_tie = (lot_tie - black_tie)//2 #2
    white_tie = (lot_tie - black_tie)-blue_tie  #3
    if quest_Tie == 0 or quest_Tie > 3:
        print('Вы ввели неккоректную цифру,попробуйте еще раз!')
        ties()
    if lot_tie == 0:
        TIES.append('Галстуков нет')
        
    if quest_Tie == 1:
        for i in range(1,black_tie+1):
            TIES.append(f'Галстук{i}')
        if lot_tie == 1 or lot_tie == 2:
            TIES.append(f"Галстук1")
    elif quest_Tie == 2:
        if lot_tie == 1:
            TIES.append('Cиний галстук отсутствует')
        if lot_tie == 2:
            TIES.append('Галстук 2')
        else:
            for i in range(black_tie+1,(black_tie+blue_tie)+1):
                TIES.append(f'Галстук{i}')
            
    elif quest_Tie == 3:
        if lot_tie == 1 or lot_tie == 2:
            TIES.append('Белый галстук отсутствует')
        else:
            for i in range((black_tie+blue_tie)+1,black_tie+blue_tie+white_tie+1):
                TIES.append(f'Галстук{i}')
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
    
    quest_T = int(input("Выберите цвет: 1-черный,2-синий,3-белый "))
    if quest_T == 0 or quest_T > 3:
        print('Вы ввели неккоректную цифру,попробуйте еще раз!')
        trousers()
    if lot_t == 0:
        TROU.append('брюк нет')
   
    black_t =  lot_t//3 #1
    blue_t = (lot_t - black_t)//2 #2
    white_t = (lot_t - black_t)-blue_t  #3
    
    if quest_T == 1:
        for i in range(1,black_t+1):
            TROU.append(f'Брюки{i}')
        if lot_t == 1 or lot_t == 2:
            TROU.append(f"Брюки1")
    elif quest_T == 2:
        if lot_t == 1:
            TROU.append('Cиние брюки отсутствуют')
        if lot_t == 2:
            TROU.append('Брюки 2')
        else:
            for i in range(black_t+1,(black_t+blue_t)+1):
                TROU.append(f'Брюки{i}')
    elif quest_T == 3:
        if lot_t == 1 or lot_t == 2:
            TROU.append('Белые брюки отсутствуют')
        else:
            for i in range((black_t+blue_t)+1,black_t+blue_t+white_t+1):
                TROU.append(f'Брюки{i}')
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
    
    quest_T = int(input("Выберите цвет: 1-черный,2-синий,3-белый "))
    if quest_T == 0 or quest_T > 3:
        print('Вы ввели неккоректную цифру,попробуйте еще раз!')
        shirts()
   
    if lot_t == 0:
        SHIR.append('Рубашек у юноши нет')
    black_t =  lot_t//3 #1
    blue_t = (lot_t - black_t)//2 #2
    white_t = (lot_t - black_t)-blue_t  #3
    
    if quest_T == 1:
        for i in range(1,black_t+1):
            SHIR.append(f'Рубашка{i}')
        if lot_t == 1 or lot_t == 2:
            SHIR.append(f"Рубашка1")
    elif quest_T == 2:
        if lot_t == 1:
            SHIR.append('Cиняя рубашка отсутствуют')
        if lot_t == 2:
            SHIR.append('Рубашка 2')
        else:
            for i in range(black_t+1,(black_t+blue_t)+1):
                SHIR.append(f'Рубашка{i}')
    elif quest_T == 3:
        if lot_t == 1 or lot_t == 2:
            SHIR.append('Белая рубашка отсутствуют')
        else:
            for i in range((black_t+blue_t)+1,black_t+blue_t+white_t+1):
                SHIR.append(f'Рубашка{i}')
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
            if j[-1].isdigit() == True:
                if 1<=int(j[-1])<=5:
                    count += randint(5,15)
                elif 5<=int(j[-1])<=15:
                    count += randint(15,25)
                else:
                    count += randint(25,50)
                
            else:
                count += 0
        print(*i,' ',f'цена костюма {count}$',end = '\n')
        count = 0   
price()
