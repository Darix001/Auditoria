import psycopg2

conn = psycopg2.connect(database="exampledb",user="docker",password="docker",host="0.0.0.0")

cur=conn.cursor()
r:int=0

for r,row in enumerate(cur.execute('SELECT * FROM STUDENTS')):
    print(f"{r} - {row}")

if not r:
    print('No Rows were returned. The table is empty.')

cur.close()
conn.close()