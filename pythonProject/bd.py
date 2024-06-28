import sqlite3
import xml.dom.minidom

con = sqlite3.connect('db01.db')
cur = con.cursor()
# cur.execute('CREATE TABLE IF NOT EXISTS fiz_lica'
#             '(id INTEGER PRIMARY KEY,'
#             'fio VARCHAR2,'
#             'country VARCHAR2,'
#             'passport VARCHAR2)')
# cur.execute('CREATE TABLE IF NOT EXISTS ur_lica'
#             '(id INTEGER PRIMARY KEY,'
#             'name VARCHAR2,'
#             'place VARCHAR2,'
#             'inn VARCHAR2)')
# cur.execute('CREATE TABLE IF NOT EXISTS trudoustroistvo'
#             '(id INTEGER PRIMARY KEY,'
#             'id_fiz INTEGER REFERENCES fiz_lica(id),'
#             'id_ur INTEGER REFERENCES ur_lica(id),'
#             'job VARCHAR2,'
#             'type VARCHAR2,'
#             'data DATE)')
# var_list = [("Makarchuk Anton Pavlovich", "Russia", "1234 423456"),
#             ("Pavlova Alla Vladimirovna", "Russian Empire", "1234 433333"),
#             ("Egorov Vadim Mihaylovich", "China", "4321 654324")]
# sql = '''INSERT INTO fiz_lica (fio, country, passport) VALUES (?,?,?)'''
# cur.executemany(sql, var_list)
# var_list = [("IT_Tech", "Russia", "2345678"),
#             ("KubSU", "Russia", "2334444"),
#             ("Pole_Chudes", "Germany", "2555555")]
# sql = '''INSERT INTO ur_lica (name, place, inn) VALUES (?,?,?)'''
# cur.executemany(sql, var_list)
# var_list = [(1, 1, "Cleaner", "Hired", "2023-16-09"),
#             (2, 2, "Worker", "Fired", "2021-15-09"),
#             (1, 3, "Cleaner", "Fired", "2023-14-10")]
# sql = '''INSERT INTO trudoustroistvo (id_fiz, id_ur, job, type, data) VALUES(?,?,?,?,?)'''
# cur.executemany(sql, var_list)
# cur.execute('SELECT * FROM trudoustroistvo')
# print(cur.fetchall())
# cur.execute('SELECT trudoustroistvo.id, trudoustroistvo.id_fiz, fiz_lica.fio, trudoustroistvo.type, '
#             'trudoustroistvo.data FROM trudoustroistvo JOIN fiz_lica ON trudoustroistvo.id_fiz=fiz_lica.id')
# print(cur.fetchall())
# cur.execute('SELECT type, COUNT(*) FROM trudoustroistvo GROUP BY type')
# print(cur.fetchall())
cur.execute('SELECT * FROM fiz_lica')
fiz_lica = cur.fetchall()
keys = ["id", "fio", "country", "passport"]
fiz_lica = list(map(lambda x: dict((keys[i], v) for i, v in enumerate(x)), fiz_lica))
cur.execute('SELECT * FROM ur_lica')
ur_lica = cur.fetchall()
keys = ["id", "name", "place", "inn"]
ur_lica = list(map(lambda x: dict((keys[i], v) for i, v in enumerate(x)), ur_lica))
cur.execute('SELECT * FROM trudoustroistvo')
trudoustroistvo = cur.fetchall()
keys = ["id", "id_fiz", "id_ur", "job", "type", "data"]
trudoustroistvo = list(map(lambda x: dict((keys[i], v) for i, v in enumerate(x)), trudoustroistvo))

# Создаем XML-документ
doc = xml.dom.minidom.Document()
# Создаем корневой элемент
root = doc.createElement('fiz_lica')
doc.appendChild(root)
for row in fiz_lica:
    record = doc.createElement('fiz_lico')
    root.appendChild(record)

    for key, value in row.items():
        element = doc.createElement(key)
        element.appendChild(doc.createTextNode(str(value)))
        record.appendChild(element)

with open('fiz_lica.xml', 'w') as f:
    f.write(doc.toprettyxml())

# Создаем XML-документ
doc = xml.dom.minidom.Document()
# Создаем корневой элемент
root = doc.createElement('ur_lica')
doc.appendChild(root)
for row in ur_lica:
    record = doc.createElement('ur_lico')
    root.appendChild(record)

    for key, value in row.items():
        element = doc.createElement(key)
        element.appendChild(doc.createTextNode(str(value)))
        record.appendChild(element)

with open('ur_lica.xml', 'w') as f:
    f.write(doc.toprettyxml())

# Создаем XML-документ
doc = xml.dom.minidom.Document()
# Создаем корневой элемент
root = doc.createElement('trudoustroistva')
doc.appendChild(root)
for row in trudoustroistvo:
    record = doc.createElement('trudoustroistvo')
    root.appendChild(record)

    for key, value in row.items():
        element = doc.createElement(key)
        element.appendChild(doc.createTextNode(str(value)))
        record.appendChild(element)

with open('trudoustroistva.xml', 'w') as f:
    f.write(doc.toprettyxml())

con.commit()
con.close()

con = sqlite3.connect('db01.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS fiz_lica2')
cur.execute('DROP TABLE IF EXISTS ur_lica2')
cur.execute('DROP TABLE IF EXISTS trudoustroistva2')
cur.execute('CREATE TABLE IF NOT EXISTS fiz_lica2'
            '(id INTEGER PRIMARY KEY,'
            'fio VARCHAR2,'
            'country VARCHAR2,'
            'passport VARCHAR2)')
cur.execute('CREATE TABLE IF NOT EXISTS ur_lica2'
            '(id INTEGER PRIMARY KEY,'
            'name VARCHAR2,'
            'place VARCHAR2,'
            'inn VARCHAR2)')
cur.execute('CREATE TABLE IF NOT EXISTS trudoustroistva2'
            '(id INTEGER PRIMARY KEY,'
            'id_fiz INTEGER REFERENCES fiz_lica2(id),'
            'id_ur INTEGER REFERENCES ur_lica2(id),'
            'job VARCHAR2,'
            'type VARCHAR2,'
            'data DATE)')

xml_file = 'fiz_lica.xml'
doc = xml.dom.minidom.parse(xml_file)
users = doc.getElementsByTagName('fiz_lico')

for user in users:
    user_id = user.getElementsByTagName('id')[0].childNodes[0].data
    fio = user.getElementsByTagName('fio')[0].childNodes[0].data
    country = user.getElementsByTagName('country')[0].childNodes[0].data
    passport = user.getElementsByTagName('passport')[0].childNodes[0].data
    var_list = [(user_id, fio, country, passport)]
    sql = '''INSERT INTO fiz_lica2 (id, fio, country, passport) VALUES(?, ?, ?, ?)'''
    cur.executemany(sql, var_list)
cur.execute('SELECT * FROM fiz_lica2')
ur_f = cur.fetchall()
print(ur_f)

xml_file = 'ur_lica.xml'
doc = xml.dom.minidom.parse(xml_file)
users = doc.getElementsByTagName('ur_lico')

for user in users:
    user_id = user.getElementsByTagName('id')[0].childNodes[0].data
    name = user.getElementsByTagName('name')[0].childNodes[0].data
    place = user.getElementsByTagName('place')[0].childNodes[0].data
    inn = user.getElementsByTagName('inn')[0].childNodes[0].data
    var_list = [(user_id, name, place, inn)]
    sql = '''INSERT INTO ur_lica2 (id, name, place, inn) VALUES(?, ?, ?, ?)'''
    cur.executemany(sql, var_list)
cur.execute('SELECT * FROM ur_lica2')
ur_l = cur.fetchall()
print(ur_l)

xml_file = 'trudoustroistva.xml'
doc = xml.dom.minidom.parse(xml_file)
users = doc.getElementsByTagName('trudoustroistvo')

for user in users:
    user_id = user.getElementsByTagName('id')[0].childNodes[0].data
    id_fiz = user.getElementsByTagName('id_fiz')[0].childNodes[0].data
    id_ur = user.getElementsByTagName('id_ur')[0].childNodes[0].data
    job = user.getElementsByTagName('job')[0].childNodes[0].data
    type = user.getElementsByTagName('type')[0].childNodes[0].data
    data = user.getElementsByTagName('data')[0].childNodes[0].data
    var_list = [(user_id, id_fiz, id_ur, job, type, data)]
    sql = '''INSERT INTO trudoustroistva2 (id, id_fiz, id_ur, job, type, data) VALUES(?, ?, ?, ?, ?, ?)'''
    cur.executemany(sql, var_list)
cur.execute('SELECT * FROM trudoustroistva2')
tr = cur.fetchall()
print(tr)

con.commit()
con.close()