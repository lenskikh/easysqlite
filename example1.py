from easysqlite import *

conn = create_connection("new.db")

create_table_sql = """ CREATE TABLE IF NOT EXISTS projects (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    begin_date text,
                                    end_date text
                                ); """

create_table(conn, create_table_sql)
