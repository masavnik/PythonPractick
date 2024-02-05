import sqlite3

conn = sqlite3.connect('orders.db')
# ИЛИ conn = sqlite3.connect(r'ПУТЬ-К-ПАПКИ/orders.db')
cur = conn.cursor()

# Создание заблицы
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
""")
conn.commit()

# Добавление данных в таблицу

# cur.execute("""INSERT INTO users(userid, fname, lname, gender)
#    VALUES('00001', 'Alex', 'Smith', 'male');""")
# conn.commit()
#
# user = ('00002', 'Lois', 'Lane', 'Female')
#
# cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
# conn.commit()

# more_users = [('00003', 'Peter', 'Parker', 'Male'), ('00004', 'Bruce', 'Wayne', 'male')]
#
# cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
# conn.commit()

#  fetchone() - Получение одного результата
cur.execute("SELECT * FROM users;")
one_result = cur.fetchone()
print(one_result)

#  fetchmany() - получить много данных
cur.execute("SELECT * FROM users;")
three_results = cur.fetchmany(3)
print(three_results)

#  fetchall() можно использовать для получения всех результатов
cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()
print(all_results)

# Удаление данных

cur.execute("DELETE FROM users WHERE lname='Parker';")
conn.commit()
cur.execute("select * from users where lname='Parker'")
print(cur.fetchall())

# Объединение таблиц
cur.execute("""SELECT *, users.fname, users.lname FROM orders
    LEFT JOIN users ON users.userid=orders.userid;""")
print(cur.fetchall())

