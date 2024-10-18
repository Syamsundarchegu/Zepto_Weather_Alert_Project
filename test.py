import sqlite3

def clear_database():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('DELETE FROM weather')
    conn.commit()
    conn.close()
    print("Database cleared.")

if __name__ == '__main__':
    clear_database()

