from random import randint
n = int(input('Введите количество камней в куче? --'))
count = 0
while n > 0:
    print('-----------------------')
    count = count + 1
    if count % 2 == 0:
        comp = randint(1, 3)
        print(f'Компьютер взял {comp} камней')
        n = n - comp
        print(f'Количество камней осталось {n}')
        if n <= 0:
            print('Компютер победил')
    else:
        player = int(input('Введите количество камней (от 1 до 3): '))
        while player < 1 or player > 3:
            print('Вы ошиблись')
            player = int(input('Введите количество камней (от 1 до 3): '))
        n = n - player
        print(f'Количество камней осталось {n}')
        if n <= 0:
            print('Вы победили!')
