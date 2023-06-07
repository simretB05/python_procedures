import dbcreds
import mariadb

conn = mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()
cursor.execute('CALL get_items()')
results = cursor.fetchall()
cursor.close()
conn.close()

for result in results:
    print(result) 


def get_price_input():
    num=input('add a price>>')
    num= float(num)
    return num

def add_price(num):
    conn = mariadb.connect(**dbcreds.conn_params)
    cursor = conn.cursor()
    cursor.execute('CALL get_items_by_price(?)',[num])
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    
    for result in results:
        print('Name:', str(result[1], 'utf-8'), 'Price:', result[2])

  
user_num= get_price_input()
get=add_price(user_num)

print(get)


