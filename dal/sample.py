"""

pip install pymysql
pip install cryptography


# if you want to create new user and want to grant to root permissions to him

CREATE USER adam@localhost IDENTIFIED BY 'qwerty@123';
GRANT ALL PRIVILEGES ON *.* TO adam WITH GRANT OPTION;
SHOW GRANTS FOR adam;

"""

import pymysql


# connection to database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Ash@95kh",
    database="starwarsdb"
)
print("Connected to MySQL".center(60, "-"))
cursor = connection.cursor()
sql = "select * from species_sample;"
print(f"No. of rows - {cursor.execute(sql)}")
result = cursor.fetchall()
for row in result:
    print(row)

connection.close()
cursor.close()
print("MySQL connection closed.".center(60, "-"))
