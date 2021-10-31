# this function removes spaces and new lines for column from right and left
def strip(string):
    return string.strip()

# this function reads database from contacts.txt file
def read_database():
    file = open("C:\Работа/contacts.txt", encoding="utf-8")
    rows = []
    for row in file:
        rows.append(list(map(strip, row.split(", "))))
    return rows

# this function writes contacts to file
def write_database(db):
    file = open("C:\Работа/contacts.txt", mode="w", encoding="utf-8")
    rows = []
    for row in db: 
        rows.append(", ".join(row))
    file.write("\n".join(rows))
    file.close()

# this function prints all contacts from db that is in memory
def print_out_database(db):
    print("Index \t Name \t\t Phone \t\t Age \t Email")
    for i in range(0, len(db)):
        row = db[i]
        print(i, "\t", row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t")



def add(db):
    name = input("Введите имя контакта: ")
    phone = input("Введите телефон контакта: ")
    age = input("Введите возраст контакта: ")
    email = input("Введите почту контакта: ")
    new_db = {name, phone, age, email}
    db.append(new_db)
    write_database(db)
    print("Контакт добавлен")

def edit(db):
    row = int(input("Строка для изменения: "))
    column = int(input("Колонна: "))
    new_data = input("Новые данные: ")
    db[row][column] = new_data
    write_database(db)

def delete(db):
    row = int(input("Строка для удаления:"))
    new_row = ""
    db[row] = new_row
    write_database(db)

def print_out_commands(db):
    print("Commands are:")
    print("1. Список пользователей")
    print("2. Редактировать пользователя")
    print("3. Добавить пользователя")
    print("4. Удалить пользователя")
    while True:
        command = input("Введите цифру команды: ")
        if command == '1':
            print_out_database(db)
        elif command == '2':
            edit(db)
        elif command == '3':
            add(db)
        elif command == '4':
            delete(db)
        else:
            print("Цифра не найдена")

def main():
  db = read_database()
  print_out_database(db)
  print_out_commands(db)


main()
