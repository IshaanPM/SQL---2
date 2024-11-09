import numpy as np
import pandas as pd
import sqlite3

conn = sqlite3.connect('database (2).sqlite')

tables = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table'""", conn)


joined_city = pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name
                            FROM country c
                            INNER JOIN city ci
                            ON c.Country_Id == ci.Country_id""", conn)

print("INNER JOIN: ", joined_city)


joined_left = pd.read_sql("""SELECT *
                            FROM player
                            LEFT JOIN season
                            ON player.Player_Id == season.Man_of_the_Series""", conn)

print("LEFT JOIN: ", joined_left)

joined_cross = pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name
                            FROM country c
                            CROSS JOIN city ci""", conn)

print("CROSS JOIN: ", joined_cross)

union = pd.read_sql("""SELECT Player_Name 
                      FROM player
                      UNION
                      SELECT Team_Name
                      FROM team""", conn)

print("UNION JOIN: ", union)
