import sqlite3
import codewars_test as test

con = sqlite3.connect("/tmp/movies.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS MOVIES(Name, Year, Rating)")
cur.execute("""
    INSERT INTO MOVIES VALUES
        ('Rise of the Planet of the Apes', 2011, 77),
        ('Dawn of the Planet of the Apes', 2014, 91),
        ('Alien', 1979, 97),
        ('Aliens', 1986, 98),
        ('Mad Max', 1979, 95),
        ('Mad Max 2: The Road Warrior', 1981, 100)
""")
con.commit()

from contextlib import closing

test.describe("Fetching movies from /tmp/movies.db")
with sqlite3.connect('/tmp/movies.db') as db:
    with closing(db.cursor()) as cursor:
        cursor.execute('SELECT name FROM sqlite_master WHERE type = "table" ')
        test.it("""There's just one table, called 'MOVIES'""")
        test.assert_equals(list(cursor.fetchall()), [(u'MOVIES',)])
