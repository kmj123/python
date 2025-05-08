import oracledb

## db 연결
def connections():
    try: conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn
        
def stuPrintAll():
    
    conn = connections()
    cursor = conn.cursor()
    sql = "select * from stuscore2"
    cursor.execute(sql)
    conn.commit()
    
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    cursor.close()
    conn.close()