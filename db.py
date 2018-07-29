#!/usr/bin/env python3

import psycopg2
import psycopg2.extras


class ConnectToNewsDB:
    def __init__(self, username='vagrant', password=''):
        self.username = username
        self.password = password
        self.host = 'localhost'

    def ConnectToDB(self, dbname='news'):
        self.dbname = dbname
        self.con = psycopg2.connect(dbname=self.dbname, user=self.username,
                                    host=self.host, password=self.password)
        self.cursor = self.con.cursor(
                            cursor_factory=psycopg2.extras.DictCursor
                            )
        return self.cursor

    def PopularArtciles(self):
        self.cursor.execute("""SELECT a.title, count(*) as views
        from articles a inner join log l on l.path LIKE ('%'  || a.slug || '%')
        and l.method='GET' and l.status like ('%200%')
        GROUP BY title order by views desc limit 3""")
        rows = self.cursor.fetchall()
        return rows

    def DisplayArticles(self, rows):
        for row in rows:
            print("- %s--%d views" % (row['title'], row['views']))

    def DisplayHorBar(self):
        print("----------------------------------------------")

    def PopularAuthors(self):
        self.cursor.execute("""SELECT at.name as title,
        count(*) as Views from articles a inner join log l
        on l.path LIKE ('%'  || a.slug || '%')
        and l.method='GET' and l.status like ('%200%')
        inner join authors at on at.id = a.author
        GROUP BY at.name order by Views desc;""")
        rows = self.cursor.fetchall()
        return rows

    def ErrorPercentage(self):
        self.cursor.execute("""SELECT to_char(time, 'FMMonth DD, YYYY') Date,
        to_char((count(*) * 100.00) / (SELECT count(*) FROM log
        where status not like '%200%'), 'FM99.99') as Error
        FROM log where status not like '%200%'
        Group by Date order by Error desc limit 1;""")
        rows = self.cursor.fetchall()
        return rows


my_db = ConnectToNewsDB('vagrant', 'example')
cur = my_db.ConnectToDB()
rows = my_db.PopularArtciles()
print("1. What are the most popular three articles of all time?")
my_db.DisplayArticles(rows)
my_db.DisplayHorBar()

rows = my_db.PopularAuthors()
print("2. Who are the most popular article authors of all time?")
my_db.DisplayArticles(rows)
my_db.DisplayHorBar()

rows = my_db.ErrorPercentage()
print("3. On which days did more than 1%% of requests lead to errors?")
for row in rows:
    print("- %s--%s errors" % (row['date'], row['error']))
my_db.DisplayHorBar()
