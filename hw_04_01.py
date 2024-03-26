# Розробити функцію total_salary(path), яка аналізує текстовий файл з даними і повертає загальну та середню суму заробітної плати всіх розробників.

with open('hw_04_01.txt', 'w', encoding='utf-8') as emp_salary: # Відкриття (створення) текстового файлу
    emp_salary.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000') # Запис даних в текстовий файл

salary_amounts = [] # Створення порожнього списку

def total_salary(path): # Створення функції читання і обробки даних з текстового документа
    try:
        with open(path, 'r', encoding='utf-8') as emp_info: # Використання менеджера контексту при відкритті документа для читання
            while True:
                line = emp_info.readline() # Читання даних по рядку
                if not line: # Умова, якщо рядок порожній
                    break
                separator = line.split(',') # Розділення даних рядка за роздільником ','
                salary_amounts.append(int(separator[1])) # Додавання в список частини рядка після роздільника

        salary = sum(salary_amounts), int(sum(salary_amounts)/len(salary_amounts)) # Створення кортежу за даними словника
        print (f'Загальна сума з/п співробітників: {salary[0]}, Середня сума з/п співробітників: {salary[1]}') # Відображення результату виклику функції
    except FileNotFoundError: # Обробка винятку при помилці з шляхом до .txt файлу
        print("Неправильний шлях до файлу, або файл відсутній")

total_salary('hw_04_01.txt') # Виклик функції