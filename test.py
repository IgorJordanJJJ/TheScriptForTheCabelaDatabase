import sqlite3



MIN_CHOICE=1
MAX_CHOICE=6
SHOW_ALL_TABLES=1
SHOW_TABLES_VALUES=2
READ_CSV=3
WRITE_VALUES_TO_DATABASE_CSV_FILE=4


EXIT=MAX_CHOICE



def main():
    choise=0
    while choise != EXIT:
        display_menu()
        choise = get_choice()

        if choise == SHOW_ALL_TABLES:
            show_all_tables()
        elif choise ==SHOW_TABLES_VALUES:
            show_tables_values()
        elif choise ==READ_CSV:
            read_csv()
        elif choise ==WRITE_VALUES_TO_DATABASE_CSV_FILE:
            write_values_to_database_csv_file()



def write_values_to_database_csv_file():
    file = open('test.csv','r')

    file_contents=file.read()

    file.close()

    print(file_contents)
    

def read_csv():
    file = open('websearch_in.csv','r')

    file_contents=file.read()

    file.close()

    print(file_contents)


def show_tables_values():
    conn = sqlite3.connect('db.sqlite3')
    bd = scaner('название базы данных')

    cur = conn.cursor()
    data  = cur.execute(f''' SELECT * FROM {bd}; ''')
    print("\n")
    for column in data.description:
        print(column[0],end=" ")
    print("\n")
    result = cur.fetchall()
    for res in result:
        print(res)
    conn.commit()
    conn.close()

def show_all_tables():
    conn = sqlite3.connect('db.sqlite3')

    cur = conn.cursor()
    cur.execute(''' SELECT name FROM sqlite_master WHERE type='table'; ''')
    result = cur.fetchall()
    print(result)
    conn.commit()
    conn.close()



def display_menu():
    print('\n--------МЕНЮ-------')
    print('1. Показать все таблицы')
    print('2. Показать значения таблицы')
    print('3. Показать значения CSV файла')
    print('4.')
    print('5.')
    print('6. Выход')

def get_choice():
    choice=int(input('Введите ваш вариант: '))

    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print('Допустимые варинаты таковы: {MIN_CHOICE} - {MAX_CHOICE}')
        choice=int(input('Введите ваш вариант: '))

    return choice


def scaner(str):
    choice=input(f'Введите {str}: ')
    return choice



if __name__=="__main__":
    main()