import sqlite3



MIN_CHOICE=1
MAX_CHOICE=6
SHOW_ALL_TABLES=1
SHOW_TABLES_VALUES=2
READ_CSV=3
WRITE_VALUES_TO_DATABASE_CSV_FILE=4
ADD_VALUE_TO_DATABASE_FROM_FILEWRITER=5


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
        elif choise ==ADD_VALUE_TO_DATABASE_FROM_FILEWRITER:
            add_value_to_database_from_filewriter()



def add_value_to_database_from_filewriter():
    fileread = open('filewrite.csv','r')
    file_contents=fileread.read()
    fileread.close()
    file_contents2 = file_contents.split('\n')
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    idWebsearchOut = ''
    idWebsearchIn = ''
    idWebsearchWay= ''
    inOutWebsearch =''
    idWebsearchBaseCabe=''

    for i in range(len(file_contents2)-2):
        i=i+1
        a = file_contents2[i].split(";")
        cur.execute(f''' SELECT * FROM websearch_basecabelmarking WHERE label ='{a[0]}'; ''')
        result = cur.fetchall()
        if not result:
            idWebsearchOut = selectIdFromWebsearch_out(a[8], a[9], a[10])
            if idWebsearchOut=='':
                addWebsearch_out(a[8], a[9], a[10],a[11])
                idWebsearchOut = selectIdFromWebsearch_out(a[8], a[9], a[10])
            idWebsearchIn = selectIdFromWebsearch_in(a[1],a[2],a[3],a[4],a[5],a[6])
            if idWebsearchIn=='':
                addWebsearch_in(a[1],a[2],a[3],a[4],a[5],a[6],a[7])
                idWebsearchIn = selectIdFromWebsearch_in(a[1],a[2],a[3],a[4],a[5],a[6])
            if a[12]=='NULL' and a[13]=='NULL' and a[14]=='NULL':
                idWebsearchWay = 'NULL'
            else:
                idWebsearchWay = selectIdFromWebsearch_way(a[12],a[13],a[14])
                if idWebsearchWay=='':
                    addWebsearch_way(a[12],a[13],a[14],a[15])
                    idWebsearchWay = selectIdFromWebsearch_way(a[12],a[13],a[14])
            addWebsearchBaseCabelMarking(a[0],idWebsearchIn,idWebsearchOut,idWebsearchWay)
        else:
            idWebsearchWay = selectIdFromWebsearch_way(a[12],a[13],a[14])
            idWebsearchBaseCabe=idWebsearchBaseCabelMarking(a[0])
            if idWebsearchWay != idWebsearchBaseCabe:
                if idWebsearchWay=='':
                    addWebsearch_way(a[12],a[13],a[14],a[15])
                    idWebsearchWay = selectIdFromWebsearch_way(a[12],a[13],a[14])
                inOutWebsearch = inOutWebsearchBaseCabelMarking(a[0])
                addWebsearchBaseCabelMarking(a[0],inOutWebsearch[0][0],inOutWebsearch[0][1],idWebsearchWay)
            else:
                print("This cabel have a data base")
    conn.commit()
    conn.close()



def write_values_to_database_csv_file():
    fileread = open('test.csv','r')
    file_contents=fileread.read()
    fileread.close()

    file_contents2 = file_contents.split('\n')

    test3=file_contents2[0:len(file_contents2)-1]
    for i in range(len(file_contents2)-1):
        if i == 0:
            test3[i]= 'label;'+file_contents2[i]
        else:
            # print(file_contents2)
            # print('\n')
            # print(file_contents2[0]+'\n')
            a = file_contents2[i].split(";")
            # print(a)
            # print(a[7][0])
            # b = a[0].split(',')
            # print(b)
            # print(file_contents2[i][0]+'\n')
            test3[i]= a[7][0]
            if a[8] == 'Magnet Yoke':
                test3[i]=test3[i]+'MR'
            else:
                test3[i]=test3[i]+a[8][0:2]
            test3[i]=test3[i]
            if len(a[9])==1:
                test3[i]=test3[i]+'0'+a[9]
            else:
                test3[i]=test3[i]+a[9]
            test3[i]=test3[i]+"R"+a[0][0]+a[1]+a[2][0]
            if len(a[3])==1:
                test3[i]=test3[i]+'0'+a[3]
            else:
                test3[i]=test3[i]+a[3]

            test3[i]=test3[i]+'-'

            if a[4] == 'Thermostabilizzation':
                test3[i] = test3[i]+'TS'
            elif a[4] == 'TPC centerl membrane':
                test3[i] = test3[i]+'CM'
            elif a[4] == 'Sensors':
                test3[i] = test3[i]+'SN'
            elif a[4] == 'ROC Chamber':
                test3[i] = test3[i]+'RC'
            elif a[4] == 'DAQ':
                test3[i] = test3[i]+'DQ'
            else:
                b = a[4].split()
                test3[i] = test3[i]+b[0][0]+b[1][0]
            if len(a[5])==1:
                test3[i]=test3[i]+'00'+a[5]
            elif len(a[5])==2:
                test3[i]=test3[i]+'0'+a[5]
            else:
                test3[i]=test3[i]+a[5]
            test3[i]=test3[i]+ ';'+file_contents2[i]

    filewrite = open('filewrite.csv','w')
    for test in test3:
        filewrite.write(test+'\n')
    filewrite.close()
    

def read_csv():

    namefilecsv = scaner('название файла csv')
    file = open(f'{namefilecsv}','r')

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
    print('4. Считать csv файл и создать filewrite с маркировкой')
    print('5. Добавить все данные с файла filewrite в базу данных')
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


def idWebsearchBaseCabelMarking(a):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f''' SELECT tray_id FROM websearch_basecabelmarking WHERE label ='{a}'; ''')
    result = cur.fetchall()
    conn.commit()
    conn.close()
    if result:
        return result[0][0]
    else:
        return ''

def inOutWebsearchBaseCabelMarking(a):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f''' SELECT ininfo_id, outinfo_id, tray_id FROM websearch_basecabelmarking WHERE label ='{a}'; ''')
    result = cur.fetchall()
    conn.commit()
    conn.close()
    if result:
        return result
    else:
        return ''

def addWebsearchBaseCabelMarking(a,b,c,d):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f''' SELECT MAX(id) FROM websearch_basecabelmarking; ''')
    result = cur.fetchall()
    if d == "NULL":
        if result[0][0]==None:
            cur.execute(f''' INSERT INTO websearch_basecabelmarking (id, label, ininfo_id, outinfo_id) VALUES('0', '{a}', '{b}', '{c}'); ''')
        else:
            cur.execute(f''' INSERT INTO websearch_basecabelmarking (id, label, ininfo_id, outinfo_id) VALUES('{result[0][0]+1}', '{a}', '{b}', '{c}'); ''')
    else:
        if result[0][0]==None:
            cur.execute(f''' INSERT INTO websearch_basecabelmarking (id, label, ininfo_id, outinfo_id,tray_id) VALUES('0', '{a}', '{b}', '{c}', '{d}'); ''')
        else:
            cur.execute(f''' INSERT INTO websearch_basecabelmarking (id, label, ininfo_id, outinfo_id,tray_id) VALUES('{result[0][0]+1}', '{a}', '{b}', '{c}', '{d}'); ''')
    result = cur.fetchall()
    conn.commit()
    conn.close()

def addWebsearch_way(a,b,c,d):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f''' SELECT MAX(id) FROM websearch_way; ''')
    result = cur.fetchall()
    if result[0][0]==None:
        cur.execute(f''' INSERT INTO websearch_way (id, tray, numberofthewindowinbeam, numberointhepowerframe,commetnway) VALUES('0', '{a}', '{b}', '{c}', '{d}'); ''')
    else:
        cur.execute(f''' INSERT INTO websearch_way (id, tray, numberofthewindowinbeam, numberointhepowerframe,commetnway) VALUES('{result[0][0]+1}', '{a}', '{b}', '{c}', '{d}'); ''')
    result = cur.fetchall()
    conn.commit()
    conn.close()

def selectIdFromWebsearch_way(a,b,c):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f''' SELECT id FROM websearch_way WHERE tray ='{a}' AND numberofthewindowinbeam ='{b}' AND numberointhepowerframe ='{c}'; ''')
    result = cur.fetchall()
    conn.commit()
    conn.close()
    if result:
        return result[0][0]
    else:
        return ''

def addWebsearch_in(a,b,c,d,e,f,r):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f''' SELECT MAX(id) FROM websearch_in; ''')
    result = cur.fetchall()
    if result[0][0]==None:
        cur.execute(f''' INSERT INTO websearch_in (id, rack, rack_number, equipment,equipmentnumber,signal,signalnumber,commentin) VALUES('0', '{a}', '{b}', '{c}', '{d}', '{e}', '{f}', '{r}'); ''')
    else:
        cur.execute(f''' INSERT INTO websearch_in (id, rack, rack_number, equipment,equipmentnumber,signal,signalnumber,commentin) VALUES('{result[0][0]+1}', '{a}', '{b}', '{c}', '{d}', '{e}', '{f}', '{r}'); ''')
    result = cur.fetchall()
    conn.commit()
    conn.close()

def selectIdFromWebsearch_in(a,b,c,d,e,f):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f''' SELECT id FROM websearch_in WHERE rack ='{a}' AND rack_number = '{b}' AND equipment = '{c}' AND equipmentnumber = '{d}' AND signal = '{e}' AND signalnumber = '{f}'; ''')
    result = cur.fetchall()
    conn.commit()
    conn.close()
    if result:
        return result[0][0]
    else:
        return ''


def addWebsearch_out(a,b,c,d):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f''' SELECT MAX(id) FROM websearch_out; ''')
    result = cur.fetchall()
    if result[0][0]==None:
        cur.execute(f''' INSERT INTO websearch_out (id, side, detector, cameranumber,commentout) VALUES('0', '{a}', '{b}', '0{c}', '{d}'); ''')
    else:
        if len(c)==1:
            cur.execute(f''' INSERT INTO websearch_out (id, side, detector, cameranumber,commentout) VALUES('{result[0][0]+1}', '{a}', '{b}', '0{c}', '{d}'); ''')
        else:
            cur.execute(f''' INSERT INTO websearch_out (id, side, detector, cameranumber,commentout) VALUES('{result[0][0]+1}', '{a}', '{b}', '{c}', '{d}'); ''')
    conn.commit()
    conn.close()

def selectIdFromWebsearch_out(a,b,c):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    if len(c)==1:
        cur.execute(f''' SELECT id FROM websearch_out WHERE side ='{a}' AND detector = '{b}' AND cameranumber = '0{c}'; ''')
    else:
        cur.execute(f''' SELECT id FROM websearch_out WHERE side ='{a}' AND detector = '{b}' AND cameranumber = '{c}'; ''')
    result = cur.fetchall()
    conn.commit()
    conn.close()
    if result:
        return result[0][0]
    else:
        return ''



if __name__=="__main__":
    main()