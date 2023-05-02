import sqlite3

def main():
    conn = sqlite3.connect('db.sqlite3')

    cur = conn.cursor()

    # cur.execute(''' SELECT name FROM sqlite_master WHERE type='table'; ''')
    # cur.execute(''' SELECT * FROM websearch_out; ''')
    # data = cur.execute(''' SELECT * FROM websearch_out; ''')
    i =8
    cur.execute(f''' INSERT INTO websearch_out (id, side, detector, cameranumber, commentout) VALUES({i},'West','TOF','03',NULL); ''')
    cur.execute(''' SELECT * FROM websearch_out; ''')

    result = cur.fetchall()

    print(result)
    

    conn.commit()

    conn.close()


if __name__=="__main__":
    main()