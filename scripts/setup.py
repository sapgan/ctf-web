import sqlite3

conn = sqlite3.connect('../users.db')
c = conn.cursor()
c.execute('CREATE TABLE users (username text, password text);')

ufp = "shell_details"
uf = open(ufp,"r").readlines()
for user in uf:
    u,p = user.strip().split(":")
    stmt = "INSERT INTO users VALUES ('{}','{}')".format(u,p)
    c.execute(stmt)
conn.commit()
conn.close()
