import sqlite3

def main():


    fileread = open('filewrite.csv','r')
    file_contents=fileread.read()
    fileread.close()
    file_contents2 = file_contents.split('\n')




    conn = sqlite3.connect('db.sqlite3')

    cur = conn.cursor()

    # websearch_basecabelmarking    websearch_way   websearch_out   websearch_in
    # cur.execute(''' SELECT name FROM sqlite_master WHERE type='table'; ''')
    # result = cur.fetchall()
    # print(result)
    # print('\n')

    # cur.execute(''' SELECT * FROM websearch_out; ''')
    # result = cur.fetchall()

    # print(result)
    # print('\n')
    
    # cur.execute(''' SELECT * FROM websearch_basecabelmarking; ''')
    # result = cur.fetchall()

    # print(result)
    # print("\n")

    # data  = cur.execute(''' SELECT * FROM websearch_basecabelmarking; ''')
 
    # for column in data.description:
    #     print(column[0],end=" ")
    # print("\n")
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


            
        # if result2:
        #     print(result2[0][0])
            
        # if not result:
        #     cur.execute(f''' SELECT id FROM websearch_out WHERE side ='{file_contents2[i]}' AND detector = '{}' AND cameranumber = {}; ''')




    # cur.execute(''' SELECT * FROM websearch_basecabelmarking WHERE label ='WTO05R12C3LV4'; ''')
    # result = cur.fetchall()

    # print(not result)
    # print('\n')
    # if not result:
    #     print("It is empty")

    conn.commit()
    conn.close()

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
    cur.execute(f''' INSERT INTO websearch_basecabelmarking (id, label, ininfo_id, outinfo_id,tray_id) VALUES('{result[0][0]+1}', '{a}', '{b}', '{c}', '{d}'); ''')
    result = cur.fetchall()
    conn.commit()
    conn.close()

def addWebsearch_way(a,b,c,d):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f''' SELECT MAX(id) FROM websearch_way; ''')
    result = cur.fetchall()
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