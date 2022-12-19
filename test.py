import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Ash@95kh",
    database="starwarsdb")

cursor1 = connection.cursor()
# data = (101, "2 cm", "70 days", "common")
# sql = f"insert into species_sample values {data}"
# print(cursor1.execute(sql))
# print(cursor1.fetchall())
# cursor1.execute("select * from species_sample")
# print(cursor1.fetchall())

data = {'species_id': 103, 'average_height': "2 cm", 'average_lifespan': "70 days", 'classification': "common"}
sql = f"insert into species_sample values {tuple(data.values())}"
print(cursor1.execute(sql))
connection.commit()
print(cursor1.fetchall())
cursor2 = connection.cursor()
cursor2.execute("select * from species_sample")
print(cursor2.fetchall())
cursor2.close()
cursor1.close()
connection.close()

