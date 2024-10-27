import hashlib

import psycopg2
# from dotenv import DotEnv
from psycopg2 import sql
import os
# import dotenv
import logging
import config

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
DB_NAME='postgres'
DB_PORT=5432
DB_PASSWORD='postgres'
DB_USER='postgres'
DB_HOST='localhost'
# DotEnv("/home/setqbyte/PycharmProjects/dispatch_backend/deploy/.env")
db_config = {
    'dbname':  DB_NAME,
    'user':  DB_USER,
    'password':  DB_PASSWORD,
    'host':  DB_HOST,
    'port':  DB_PORT,
}


def db_connection():
    return psycopg2.connect(**db_config)


def create_table():
    connection = db_connection()
    cursor = connection.cursor()

    try:
        create_table_query = sql.SQL("""
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR,
            last_name VARCHAR,
            father_name VARCHAR,
            login VARCHAR unique,
            hashed_pwd VARCHAR,
            profession VARCHAR
        )
        """)

        cursor.execute(create_table_query)
        connection.commit()
        logger.info("Table created successfully")

    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logger.info('Database connection closed.')
            # logger.debug("-" * 40)


def drop_table():
    connection = db_connection()
    cursor = connection.cursor()

    try:
        drop_table_query = sql.SQL("""
        DROP TABLE IF EXISTS employees
        """)

        cursor.execute(drop_table_query)
        connection.commit()
        logger.info("Table dropped successfully")

    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logger.info('Database connection closed.')
            # logger.debug("-" * 40)


async def get_employee(employee_id):
    connection = db_connection()
    cursor = connection.cursor()

    try:
        get_user_query = sql.SQL("""
        SELECT name, last_name, father_name, profession FROM employees WHERE id = %s
        """)
        cursor.execute(get_user_query, (employee_id,))

        rows = cursor.fetchmany(size=4)

        employees = [
            {"name": row[0], "last_name": row[1], "father_name": row[2], "profession": row[3]}
            for row in rows
        ]

        logger.info("Database fetched successfully")
        return employees

    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logger.info('Database connection closed.')
            # logger.debug("-" * 40)


async def create_employee(login, password, name, last_name, father_name, profession):
    connection = db_connection()
    cursor = connection.cursor()

    hashed_pwd = hashlib.sha256(password.encode()).hexdigest()

    try:
        create_employee_query = sql.SQL("""
            INSERT INTO employees (login, hashed_pwd, name, last_name, father_name, profession) VALUES (%s, %s, %s, %s, %s, %s) returning id
            """)
        cursor.execute(create_employee_query, (login, hashed_pwd, name, last_name, father_name, profession))

        employee_id = cursor.fetchone()[0]

        connection.commit()
        logger.info("Created employee successfully")

        return employee_id

    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logger.info('Database connection closed.')
            # logger.debug("-" * 40)


async def login_employee(login, password):
    connection = db_connection()
    cursor = connection.cursor()

    try:
        login_employee_query = sql.SQL("""
            SELECT id, hashed_pwd FROM employees WHERE login = %s
            """)
        cursor.execute(login_employee_query, (login,))

        rows = cursor.fetchmany(size=2)

        employees = [
            {"id": item[0], "hashed_pwd": item[1]}
            for item in rows
        ]

        hashed_pwd = hashlib.sha256(password.encode()).hexdigest()

        if hashed_pwd == employees[0]["hashed_pwd"]:
            connection.commit()
            logger.info("Login successful")
            return employees[0]["id"]
        else:
            logger.error("Invalid password")
            return None

    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logger.info('Database connection closed.')
            # logger.debug("-" * 40)


db_config = {
    'dbname':  DB_NAME,
    'user':  DB_USER,
    'password':  DB_PASSWORD,
    'host':  DB_HOST,
    'port':  DB_PORT,
}


# create table if not exists reports(
#     id serial primary key,
#     date timestamp,
#     c_workers int,
#     c_wagons int,
#     c_excavator int,
#     c_cars int,
#     c_bigwagons int
# );


async def get_report(date):
    connection = db_connection()
    cursor = connection.cursor()

    try:
        get_report_query = sql.SQL("""
        SELECT id, c_workers, c_wagons, c_excavator, c_cars, c_bigwagons FROM reports WHERE date = %s
        """)
        cursor.execute(get_report_query, (date,))

        rows = cursor.fetchmany(size=4)

        employees = [
            {"id": row[0], "c_workers": row[1], "c_wagons": row[2], "c_excavator": row[3], "c_cars": row[4],
             "c_bigwagons": row[5]}
            for row in rows
        ]

        return employees

    except (Exception, psycopg2.DatabaseError) as error:
        return error

    finally:
        if connection:
            cursor.close()
            connection.close()


async def update_report(c_workers, c_wagons, c_excavator, c_cars, c_bigwagons, date):
    connection = db_connection()
    cursor = connection.cursor()

    try:
        create_report_query = sql.SQL("""
            UPDATE reports SET (%s, %s, %s, %s, %s) WHERE date = %s
        """)
        cursor.execute(create_report_query, (c_workers, c_wagons, c_excavator, c_cars, c_bigwagons, date))

        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        return error

    finally:
        if connection:
            cursor.close()
            connection.close()


async def add_new_report(c_workers, c_wagons, c_excavator, c_cars, c_bigwagons, date):
    connection = db_connection()
    cursor = connection.cursor()

    try:
        add_new_report_query = sql.SQL("""
            INSERT INTO reports (c_workers, c_wagons, c_excavator, c_cars, c_bigwagons, date) VALUES (%s, %s, %s, %s, %s, %s)
            """)
        cursor.execute(add_new_report_query, (c_workers, c_wagons, c_excavator, c_cars, c_bigwagons, date))

        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        return error

    finally:
        if connection:
            cursor.close()
            connection.close()
