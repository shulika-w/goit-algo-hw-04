def parse_input(user_input): # Створення функції, яка приймає рядок вводу користувача як аргумент
    cmd, *args = user_input.split() # Розбиття рядку на дві складові, перше слово зберігається у змінній cmd, решта - в списку args
    cmd = cmd.strip().lower() # Видалення пробілів навколо команди і перетворення її на нижній регістр
    return cmd, *args # Повернення обробленого рядка в змінній cmd і списку args

def add_contact(args, contacts): # Створення функції додавання контакту
    name, phone = args # Приймання двох змінних як аргументів
    contacts[name] = phone # Запис значення phone до ключа name у словнику
    return "Contact added." 

def change_contact(args, contacts): # Створення функції зміни значення для існуючої пари ключ-значення
    name, phone = args # Приймання двох змінних як аргументів
    contacts[name] = phone # Запис нового значення phone до ключа name у словнику
    return "Contact updated."

def show_phone(args, contacts): # Створення функції виведення на екран значення за викликом ключа
    try: 
        name, _ = args # Приймання змінної як аргументу
    except ValueError: # Обробка помилки
        if len(args) == 0: 
            return 'No data'
        name = args[0] 
    return contacts[name] 

def show_all(args, contacts): # Створення функції виведення на екран всіх доданих пар ключ-значення
    return contacts

def main(): # Створення функції, яка управляє основним циклом обробки команд
    contacts = {} # Створення порожнього словника
    print("Welcome to the assistant bot!") # Виклик привітання при запуску
    while True: # Вхід в нескінченнний цикл
        user_input = input("Enter a command: ") # Очікування на введення від користувача
        command, *args = parse_input(user_input) # Виклик функції

        if command in ["close", "exit"]: 
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.") # Варіації команд і виклик відповідних функцій

if __name__ == "__main__": 
    main()