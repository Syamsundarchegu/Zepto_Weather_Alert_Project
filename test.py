import sqlite3

# Connect to the database
conn = sqlite3.connect('weather.db')
c = conn.cursor()

# Insert test data
c.execute('''
    INSERT INTO weather (city, main, temp, feels_like, dt)
    VALUES ('Test City', 'Clear', 25.0, 25.0, strftime('%s', 'now'))
''')
c.execute('''
    INSERT INTO weather (city, main, temp, feels_like, dt)
    VALUES ('Test City', 'Clear', 26.0, 25.0, strftime('%s', 'now', '-5 minutes'))
''')

conn.commit()
conn.close()
