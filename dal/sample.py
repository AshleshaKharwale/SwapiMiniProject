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
    # breakpoint()
    print(f"Connected to MySQL database - '{(connection.db).decode()}'")

    return connection


def insert_resource(table_name, data):
    sql_query = f"insert into {table_name} ({', '.join(data.keys())}) values {tuple(data.values())}"
    with get_db_conn() as conn:
        cursor = conn.cursor()
        # breakpoint()
        result = cursor.execute(sql_query)
        conn.commit()
        print(f"Data inserted into {table_name} successfully!!")
    return result


if __name__ == "__main__":
    with get_db_conn() as connection:
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
        print("MySQL database connection closed")

    # insert_resource("species_sample", {'average_lifespan': '10 months', 'average_height':'7.3 cm'})