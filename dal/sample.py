"""

pip install pymysql
pip install cryptography


# if you want to create new user and want to grant to root permissions to him

CREATE USER adam@localhost IDENTIFIED BY 'qwerty@123';
GRANT ALL PRIVILEGES ON *.* TO adam WITH GRANT OPTION;
SHOW GRANTS FOR adam;

"""

import pymysql


def get_db_conn():
    # connection to database
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="Ash@95kh",
        database="starwarsdb"
    )

    return connection


if __name__ == "__main__":
    connection = get_db_conn()
    print("Connected to MySQL".center(60, "-"))
    cursor1 = connection.cursor()
    sql = "select * from species_sample;"
    print(f"No. of rows - {cursor1.execute(sql)}")
    result = cursor1.fetchall()
    print("Table- species_sample")
    for row in result:
        print(row)

    cursor2 = connection.cursor()
    sql2 = "describe species_sample;"
    cursor2.execute(sql2)
    result2 = cursor2.fetchall()
    print("show species_sample")
    print(result2)

    connection.close()
    cursor1.close()
    cursor2.close()
    print("MySQL connection closed".center(60, "-"))
