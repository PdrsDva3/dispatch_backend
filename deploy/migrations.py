import hashlib

import psycopg2
from dotenv import DotEnv
from psycopg2 import sql
import os
import dotenv
import logging
from deploy import config


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger(__name__)



# DotEnv("/home/setqbyte/PycharmProjects/dispatch_backend/deploy/.env")
db_config = {
    'dbname': config.DB_NAME,
    'user': config.DB_USER,
    'password': config.DB_PASSWORD,
    'host': config.DB_HOST,
    'port': config.DB_PORT,
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
            logger.debug("-" * 40)


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
            logger.debug("-" * 40)


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
            logger.debug("-" * 40)


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
            logger.debug("-" * 40)


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
            logger.debug("-" * 40)