# Розробити функцію get_cats_info(path), яка читає .txt файл з даними та повертає список словників з інформацією про кожного кота.

with open('hw_04_02.txt', 'w', encoding='utf-8') as cats_stat: # Вікриття (створення) текстового файлу
    cats_stat.write('''60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
''') # Запис даних у текстовий файл

def get_cats_info(path): # Створення функції, яка приймає шлях до файлу як аргумент
    try: 
        with open(path, 'r', encoding='utf-8') as cat_info: # Відкриття файлу для читання
            lines = cat_info.readlines() # Відокремлення кожного рядку у файлі
        
        cat_dicts = [] # Створення порожнього списку
        for line in lines: # Ітерація по відокремленому рядку
            line_part = line.strip().split(',') # "Розбиття" рядка на частини за роздільником ","
            cats_dict = {
                'id': line_part[0],
                'name': line_part[1],
                'age': line_part[2]
            } # Створення словника з трьома ключами, аргументами яких є частини рядка
            cat_dicts.append(cats_dict) # Додавання словника в список
        print(cat_dicts) # Виведення списку словників, кожен з яких починається з нового рядка

    except FileNotFoundError: # Обробка винятку при помилці з шляхом до .txt файлу
        print("Неправильний шлях до файлу, або файл відсутній")

get_cats_info('hw_04_02.txt') # Виклик функції