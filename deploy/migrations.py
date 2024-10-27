import psycopg2
from psycopg2 import sql

import config
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT

db_config = {
    'dbname': config.DB_NAME,
    'user': config.DB_USER,
    'password': config.DB_PASSWORD,
    'host': config.DB_HOST,
    'port': config.DB_PORT,
}


# create table if not exists reports(
#     id serial primary key,
#     date timestamp,
#     c_workers int,
#     c_vagons int,
#     c_excavator int,
#     c_cars int,
#     c_bigvagons int
# );

def db_connection():
    return psycopg2.connect(**db_config)


async def get_report(date):
    connection = db_connection()
    cursor = connection.cursor()

    try:
        get_report_query = sql.SQL("""
        SELECT id, c_workers, c_vagons, c_excavator, c_cars, c_bigvagons FROM reports WHERE date = %s
        """)
        cursor.execute(get_report_query, (date,))

        rows = cursor.fetchmany(size=4)

        employees = [
            {"id": row[0], "c_workers": row[1], "c_vagons": row[2], "c_excavator": row[3], "c_cars": row[4],
             "c_bigvagons": row[5]}
            for row in rows
        ]

        return employees

    except (Exception, psycopg2.DatabaseError) as error:
        return error

    finally:
        if connection:
            cursor.close()
            connection.close()


async def update_report(c_workers, c_vagons, c_excavator, c_cars, c_bigvagons, date):
    connection = db_connection()
    cursor = connection.cursor()

    try:
        create_report_query = sql.SQL("""
            UPDATE reports SET (%s, %s, %s, %s, %s) WHERE date = %s
        """)
        cursor.execute(create_report_query, (c_workers, c_vagons, c_excavator, c_cars, c_bigvagons, date))

        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        return error

    finally:
        if connection:
            cursor.close()
            connection.close()


async def add_new_report(c_workers, c_vagons, c_excavator, c_cars, c_bigvagons, date):
    connection = db_connection()
    cursor = connection.cursor()

    try:
        add_new_report_query = sql.SQL("""
            INSERT INTO reports (c_workers, c_vagons, c_excavator, c_cars, c_bigvagons, date) VALUES (%s, %s, %s, %s, %s, %s)
            """)
        cursor.execute(add_new_report_query, (c_workers, c_vagons, c_excavator, c_cars, c_bigvagons, date))
        connection.commit()


    except (Exception, psycopg2.DatabaseError) as error:
        return error

    finally:
        if connection:
            cursor.close()
            connection.close()
