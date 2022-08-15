# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 12:17:52 2022

@author: smassine
"""

import psycopg2

def db_connect(host, port, database, user, password):
    
    """
    Connect to the PostgreSQL database server.

    Parameters
    ----------
    host: <str>
        Database server address e.g., localhost or an IP address.
    port: <int>
        The port numbe (defaults 5432).
    database: <str>
        The name of the database that you want to connect.
    user <str>
        The username used to authenticate.
    password <str>
        Password used to authenticate.
    """

    conn = None
    
    try:
        # Connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password)
		
        # Create a cursor
        cur = conn.cursor()
        
	# Execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # Display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# Close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            