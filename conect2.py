import sqlite3

def main():
    conn = sqlite3.connect('db.sqlite3')

    cur = conn.cursor()

    # cur.execute(''' SELECT name FROM sqlite_master WHERE type='table'; ''')
    # cur.execute(''' SELECT * FROM websearch_out; ''')
    # data = cur.execute(''' SELECT * FROM websearch_out; ''')
    # i =9
    # cur.execute(f''' INSERT INTO websearch_out (id, side, detector, cameranumber) VALUES({i},'West','TOF','03'); ''')
    label='WTO05R12C3LV4'
    label2='WTO05R17S7CM7'
    cur.execute(f''' SELECT * FROM websearch_basecabelmarking WHERE label IN ('{label}', '{label2}'); ''')

    result = cur.fetchall()

    print(result)
    

    conn.commit()

    conn.close()


if __name__=="__main__":
    main()