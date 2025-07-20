import sqlite3

db = sqlite3.connect('online_store.db')
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    category_id INTEGER,
    FOREIGN KEY(category_id) REFERENCES categories(id)
)
""")

cur.execute("INSERT INTO categories (name) VALUES ('Книги')")
cur.execute("INSERT INTO categories (name) VALUES ('Авто')")
cur.execute("INSERT INTO categories (name) VALUES ('Взуття')")


cur.execute("INSERT INTO products (name, description, price, category_id) VALUES ('Теодор Драйзер ''Фінансист''', 'паперова книга', 300, 1)")
cur.execute("INSERT INTO products (name, description, price, category_id) VALUES ('BMW', 'X5', 30000, 2)")
cur.execute("INSERT INTO products (name, description, price, category_id) VALUES ('Adidas', 'zx', 300, 3)")

db.commit()

for row in cur.execute("""
SELECT products.id, products.name, categories.name
FROM products
JOIN categories ON products.category_id = categories.id
WHERE products.id IN (1, 3)"""):
    print(row)

db.close()
