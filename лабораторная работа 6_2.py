#усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
print('Юноша хранит вещи в разных шкафах,он перфекционист и в каждом шкафе его вещи разделены на 3 части по цветам:черный,белый,синий')
p , g ,r , b = int(input('Введите количество пиджаков у юноши в гардеробе: ')),int(input('Введите количество галстуков у юноши в гардеробе: ')),int(input('Введите количество рубашек у юноши в гардеробе: ')),int(input('Введите количество брюк у юноши в гардеробе: '))
quest_P = int(input('Выберете цвет пиджака,если хотите черный,введите цифру 1,если белый-цифру 2,синий-цифру 3'))
quest_G = int(input('Выберете цвет галстука,если хотите черный,введите цифру 1,если белый-цифру 2,синий-цифру 3'))
quest_R = int(input('Выберете цвет рубашки,если хотите черный,введите цифру 1,если белый-цифру 2,синий-цифру 3'))
quest_B = int(input('Выберете цвет брюк,если хотите черный,введите цифру 1,если белый-цифру 2,синий-цифру 3'))

P = []
G = []
R = []
B = []
if p >= 3:
    if quest_P == 1:
        for i in range(1,(p//3)+1):
            P.append(f'Пиджак{(i)}')  
    elif quest_P == 2:
        if p%3 == 0:
            for i in range((p//3)+1,((p-(p//3)))+1):
                P.append(f'Пиджак{(i)}') 
        else:
            for i in range((p//3)+1,((p-(p//3)))):   
                P.append(f'Пиджак{(i)}')  
    elif quest_P == 3:
        if p%3 == 0:
            for i in range((((p-(p//3)))+1),p+1):
                P.append(f'Пиджак{(i)}') 
        else:
            for i in range(((p-(p//3))),p+1):
                P.append(f'Пиджак{(i)}') 
elif p == 2:
    if quest_P == 1:
        P.append('Пиджак 1')
    elif quest_P == 2:
        P.append('Пиджак 2')
    elif quest_P == 3:
        print('Синего пиджака у юноши нет.')
elif p == 1:
    if quest_P == 1:
        P.append('Пиджак 1')
    elif  quest_P == 2:
        print('Белого пиджака у юноши нет.')
    elif  quest_P == 3:
        print('Синего пиджака у юноши нет.')

if g >= 3:
    if quest_G == 1:
        for i in range(1,(g//3)+1):
            G.append(f'Галстук{(i)}')  
    elif quest_G == 2:
        if g%3 == 0:
            for i in range((g//3)+1,((g-(g//3)))+1):
                G.append(f'Галстук{(i)}') 
        else:
            for i in range((g//3)+1,((g-(g//3)))):   
                G.append(f'Галстук{(i)}')  
    elif quest_G == 3:
        if g%3 == 0:
            for i in range((((g-(g//3)))+1),g+1):
                G.append(f'Галстук{(i)}')  
        else:
            for i in range(((g-(g//3))),g+1):
                G.append(f'Галстук{(i)}') 
elif g == 2:
    if quest_G == 1:
        G.append('Галстук 1')
    elif quest_G == 2:
        G.append('Галстук 2')
    elif quest_G == 3:
        print('Синего галстука у юноши нет.')
elif g == 1:
    if quest_G == 1:
        G.append('Галстук 1')
    elif quest_G == 2:
        print('Белого галстука у юноши нет.')
    elif quest_G== 3:
        print('Синего галстука у юноши нет.')



if r >= 3:
    if quest_R == 1:
        for i in range(1,(r//3)+1):
            R.append(f'Рубашка{(i)}')  
    elif quest_R == 2:
        if r%3 == 0:
            for i in range((r//3)+1,((r-(r//3)))+1):
                R.append(f'Рубашка{(i)}') 
        else:
            for i in range((r//3)+1,((r-(r//3)))):   
                R.append(f'Рубашка{(i)}')  
    elif quest_R == 3:
        if r%3 == 0:
            for i in range((((r-(r//3)))+1),r+1):
                R.append(f'Рубашка{(i)}') 
        else:
            for i in range(((r-(r//3))),r+1):
                P.append(f'Рубашка{(i)}') 
elif r == 2:
    if quest_R == 1:
        R.append('Рубашка 1')
    elif quest_R == 2:
        R.append('Рубашка 2')
    elif quest_R == 3:
        print('Синей рубашки у юноши нет.')
elif r == 1:
    if quest_R == 1:
        R.append('Рубашка 1')
    elif quest_R == 2:
        print('Белой рубашки у юноши нет.')
    elif quest_R== 3:
        print('Синей рубашки у юноши нет.')



if b >= 3:
    if quest_B == 1:
        for i in range(1,(b//3)+1):
            B.append(f'Брюки{(i)}')  
    elif quest_B == 2:
        if b%3 == 0:
            for i in range((b//3)+1,((b-(b//3)))+1):
                B.append(f'Брюки{(i)}') 
        else:
            for i in range((b//3)+1,((b-(b//3)))):   
                B.append(f'Брюки{(i)}')  
    elif quest_B == 3:
        if b%3 == 0:
            for i in range((((b-(b//3)))+1),b+1):
                B.append(f'Брюки{(i)}') 
        else:
            for i in range(((b-(b//3))),b+1):
                B.append(f'Брюки{(i)}') 

elif b == 2:
    if quest_B == 1:
        B.append('Брюки 1')
    elif quest_B == 2:
        B.append('Брюки 2')
    elif quest_B == 3:
        print('Синих брюк у юноши нет.')
elif b == 1:
    if quest_B == 1:
        B.append('Брюки 1')
    elif quest_B == 2:
        print('Белых брюк у юноши нет.')
    elif quest_B== 3:
        print('Синих брюк у юноши нет.')


#------------------------------------------------

kost = []
kost_ob = []
for ii in P:
    for jj in G:
        for hh in R:
            for gg in B:
                kost.append(ii)
                kost.append(jj)
                kost.append(hh)
                kost.append(gg)
                kost_ob.append(kost)
                kost = []

print(f"Все варианты костюмов у юноши : {kost_ob}")
print(f"Общее количество костюв : {len(kost_ob)}")