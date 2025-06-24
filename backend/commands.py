import sqlite3

con = sqlite3.connect("./database/ecommerce.db")
cursor = con.cursor()

# cursor.execute("drop table Cards")
# # cursor.execute("INSERT INTO pedidos (id, product, user, quant)SELECT id, product, user, quant FROM pedidos_old;")
# cursor.execute("""
#     CREATE TABLE Cards (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER NOT NULL,
#         CardType TEXT NOT NULL,
#         Num TEXT NOT NULL,
#         Mes INTEGER NOT NULL,
#         Ano INTEGER NOT NULL,
#         CVV TEXT NOT NULL,
#         Nome TEXT NOT NULL,
#         FOREIGN KEY (user_id) REFERENCES Users(id)
#     )
# """)
sql = "INSERT INTO pedidos (product, user,quant,status) VALUES (?, ?, ?, ?)"
values = (1, 4, 10, "Completed")
cursor.execute(sql, values)
# columns = cursor.fetchall()

con.commit()

# Exibir os detalhes das colunas
# for column in columns:
#     print(column)