import cgi
import sqlite3

form = cgi.FieldStorage()
text1 = form.getfirst("id_fiz",0)
text2 = form.getfirst("id_ur", 0)
text3 = form.getfirst("job","")
text4 = form.getfirst("type","Hired")
text5 = form.getfirst("data","1111-11-11")

text7 = form.getfirst("fio","")
text8 = form.getfirst("country","Russia")
text9 = form.getfirst("passport","")

text11 = form.getfirst("name","")
text12 = form.getfirst("place","")
text13 = form.getfirst("inn","")
con = sqlite3.connect('db01.db')
cur = con.cursor()
if text1 !=0 or text2 !=0 or text3!="" or text5 !="1111-11-11":
    var_list = [(text1, text2, text3, text4, text5)]
    sql = '''INSERT INTO trudoustroistvo (id_fiz, id_ur, job, type, data) VALUES(?,?,?,?,?)'''
    cur.executemany(sql, var_list)
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Trudoustroistvo</title>
        </head>
        <body>""")
    print("<h1>Trudoustroistvo</h1>")
    print("<p>id Физ Лица:  {}</p>".format(text1))
    print("<p>id Юр. Лица: {}</p>".format(text2))
    print("<p>Работа: {}</p>".format(text3))
    print("<p>Тип приема: {}</p>".format(text4))
    print("<p>Дата: {}</p>".format(text5))
    print("""</body> </html>""")
    cur.execute('SELECT * FROM trudoustroistvo')
    print(cur.fetchall())

if text7 !="" or text9 !="":
    var_list=[(text7,text8,text9)]
    sql='''INSERT INTO fiz_lica (fio, country, passport) VALUES(?,?,?)'''
    cur.executemany(sql,var_list)
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Fiz_lica</title>
            </head>
            <body>""")
    print("<h1>Fiz_lica</h1>")
    print("<p>fio:  {}</p>".format(text7))
    print("<p>country: {}</p>".format(text8))
    print("<p>passport: {}</p>".format(text9))
    print("""</body> </html>""")
    cur.execute('SELECT * FROM fiz_lica')
    print(cur.fetchall())

if text11 !="" or text12 !="" or text13 !="":
    var_list = [(text11, text12, text13)]
    sql = '''INSERT INTO ur_lica (name, place, inn) VALUES(?,?,?)'''
    cur.executemany(sql, var_list)
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <title>Ur_lica</title>
                </head>
                <body>""")
    print("<h1>Ur_lica</h1>")
    print("<p>name:  {}</p>".format(text11))
    print("<p>place: {}</p>".format(text12))
    print("<p>inn: {}</p>".format(text13))
    print("""</body> </html>""")
    cur.execute('SELECT * FROM ur_lica')
    print(cur.fetchall())
con.commit()
cur.close()
con.close()