import cgi
import sqlite3
import xml.dom.minidom

form = cgi.FieldStorage()
text1 = form.getfirst("fullnamec", "")
text2 = form.getfirst("telc", "")
text3 = form.getfirst("fullnamet", "")
text4 = form.getfirst("telt", "")
text5 = form.getfirst("point", 0)
text6 = form.getfirst("date", "1111-11-11")
text7 = form.getfirst("client_id", 0)
text8 = form.getfirst("trainer_id", 0)
con = sqlite3.connect('db01.db')
cur = con.cursor()
if text1 != "" or text2 != "":
    var_list = [(text1, text2)]
    sql = '''INSERT INTO clients (fullname, tel) VALUES(?,?)'''
    cur.executemany(sql, var_list)
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="cp1251">
            <title>client</title>
        </head>
        <body>""")
    print("<h1>client</h1>")
    print("<p>fullname: {}</p>".format(text1))
    print("<p>tel: {}</p>".format(text2))
    print("""</body> </html>""")
    cur.execute('SELECT * FROM clients')
    print(cur.fetchall())

if text3 != "" or text4 != "" or text5 != 0:
    var_list = [(text3, text4, text5)]
    sql = '''INSERT INTO trainers (fullname, tel, point) VALUES(?,?,?)'''
    cur.executemany(sql, var_list)
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="cp1251">
            <title>trainer</title>
        </head>
        <body>""")
    print("<h1>trainer</h1>")
    print("<p>fullname: {}</p>".format(text3))
    print("<p>tel: {}</p>".format(text4))
    print("<p>point: {}</p>".format(text5))
    print("""</body> </html>""")
    cur.execute('SELECT * FROM trainers')
    print(cur.fetchall())

if text6 != "1111-11-11" or text7 != 0 or text8 != 0:
    var_list = [(text6, text7, text8)]
    sql = '''INSERT INTO trainings (date, client_id, trainer_id) VALUES(?,?,?)'''
    cur.executemany(sql, var_list)
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="cp1251">
            <title>trainings</title>
        </head>
        <body>""")
    print("<h1>trainings</h1>")
    print("<p>date: {}</p>".format(text6))
    print("<p>client id: {}</p>".format(text7))
    print("<p>trainer id: {}</p>".format(text8))
    print("""</body> </html>""")
    cur.execute('SELECT * FROM trainings')
    print(cur.fetchall())
con.commit()
cur.close()
con.close()
