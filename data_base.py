import sqlite3
def creat_table():
    conn = sqlite3.connect('./books.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS books(
        uid INTEGER PRIMARY KEY,
        name VARCHAR(50),
        family VARCHAR(50),
        book VARCHAR(50),
        price INTEGER);
       """)
    conn.commit()
    conn.close()




def add_book(name, family, book, price):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO books(name, family, book, price)VALUES (?,?,?,?)""",(name, family, book, price))

    conn.commit()
    conn.close()

def select_name_book(book):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM books WHERE book = ?
    """,(book,))
    rest = cursor.fetchall()
    conn.close()
    conn.close()
    return rest






if __name__ == '__main__':
    creat_table()










