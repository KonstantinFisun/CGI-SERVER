#!/usr/bin/python

# Импорт модулей для обработки CGI
import cgi, cgitb
import html
import sqlite3

# Создание соедиения с базой
connection = sqlite3.connect("Z:\\CGI-SERVER\\land_transport.db")
# Создание курсора
cursor = connection.cursor()

# Создание экземпляра FieldStorage
form = cgi.FieldStorage()


# addTable = form.getvalue('table')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<meta charset=""UTF-8"">")
print ("<title>Наземный транспорт</title>")
print ("</head>")
print ("<body bgcolor = #5F9EA0> ")
print("<div  <div>")
print ("<h1 align = 'center'>Наземный транспорт</h1>")

# Получение данных из полей
table = form.getvalue('Таблицы')
but = form.getvalue('Button')

# Форма выбора таблиц для вывода
print("""<form action = "/cgi-bin/View.py" method = "post">
<select name = "Таблицы">
<option value = "Type_transport">Тип транспорта</option>
<option value = "Firm">Фирмы</option>
<option value = "Transport">Транспорт</option>
</select>
<input type = "submit" name = 'Button' value = "Вывести" />
<input type = "submit" name = 'Button' value = "Добавить" />
</form>""")


# Форма выбора таблиц для добавления данных
# print("""<form action = "/cgi-bin/View.py" method = "post">
# <input type = 'radio' name = 'table' value = 'Type_transport' /> Тип транспорта <br>
# <input type = 'radio' name = 'table' value = 'Firm' /> Фирмы <br>
# <input type = 'radio' name = 'table' value = 'Transport' /> Транспорт <br>
# <input type = "submit" value = "Добавить данные" />
# </form>""")

# Вывод таблиц на экран
if but == 'Вывести':
    if table == 'Type_transport':
        # Запрос таблицы Тип транспорта
        cursor.execute("""SELECT TypeID, Title
                       FROM Type_transport """)
        type_transport = cursor.fetchall()

        # Таблица Тип транспорта
        print("<table cellspacing = '10'>"
              "<caption><h2>Тип транспорта</h2></caption>"
              "<tr>"
              "<th>ID</th>"
              "<th>Название</th>"
              "</tr>")
        for row in type_transport:
            print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1])
        print("</table>")

    elif table == 'Firm':
        # Запрос таблицы Фирмы
        cursor.execute("""SELECT FirmID, Title, Country
                           FROM Firm """)
        firm = cursor.fetchall()

        # Таблица Фирмы
        print("<table cellspacing = '10'>"
              "<caption><h2>Фирмы</h2></caption>"
              "<tr>"
              "<th>ID</th>"
              "<th>Название</th>"
              "<th>Страна</th>"
              "</tr>")
        for row in firm:
            print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1],
                  "</td><td align = 'center'>", row[2])
        print("</table>")

    elif table == 'Transport':
        # Запрос таблицы Транспорта
        cursor.execute("""SELECT CarID, Model, Power, Weight, Firm.Title, Type_transport.Title
                        FROM Transport 
                        JOIN Type_transport ON Transport.TypeID = Type_transport.TypeID
                        JOIN Firm ON Firm.FirmID = Transport.FirmID""")
        actionCams = cursor.fetchall()

        # Таблица Транспорта
        print("<table cellspacing = '10'>"
              "<caption><h2>Транспорт</h2></caption>"
              "<tr>"
              "<th>ID</th>"
              "<th>Модель</th>"
              "<th>Мощность</th>"
              "<th>Вес</th>"
              "<th>Фирма</th>"
              "<th>Тип</th>"
              "</tr>")
        for row in actionCams:
            print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1],
                  "</td><td align = 'center'>", row[2], "</td><td align = 'center'>", row[3],
                  "</td><td align = 'center'>", row[4], "</td><td align = 'center'>", row[5])
        print("</table>")

# Добавление данных в таблицы (просто формочка, когда сюда заходит сначала выполнялся наш запрос,
# а уже потом с формочек читались данные, которые вводили
if but == 'Добавить':
    if table == 'Transport':
        print("""<form action = "/cgi-bin/View.py" method = "post">
        Модель: <input type = "text" name = "Model" />
        Вес: <input type = "text" name = "Weight" /> 
        Мощность: <input type = "text" name = "Power" />
        Тип транспорта(номер): <input type = "text" name = "TypeID" />
        Фирма(номер): <input type = "text" name = "FirmID" />
        <input type = 'submit' value = 'Добавить в базу данных'>
        </form>""")

        # Вывод доп таблиц
        # Запрос таблицы Фирмы
        cursor.execute("""SELECT FirmID, Title, Country
                                   FROM Firm """)
        firm = cursor.fetchall()

        # Таблица Фирмы
        print("<table cellspacing = '10'>"
              "<caption><h2>Фирмы</h2></caption>"
              "<tr>"
              "<th>ID</th>"
              "<th>Название</th>"
              "<th>Страна</th>"
              "</tr>")
        for row in firm:
            print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1],
                  "</td><td align = 'center'>", row[2])
        print("</table>")

        # Запрос таблицы Тип транспорта
        cursor.execute("""SELECT TypeID, Title
                              FROM Type_transport """)
        type_transport = cursor.fetchall()

        # Таблица Тип транспорта
        print("<table cellspacing = '10'>"
              "<caption><h2>Тип транспорта</h2></caption>"
              "<tr>"
              "<th>ID</th>"
              "<th>Название</th>"
              "</tr>")
        for row in type_transport:
            print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1])
        print("</table>")


 # Получение данных из полей
model = form.getvalue('Model')
weight = form.getvalue('Weight')
power = form.getvalue('Power')
firm = form.getvalue('FirmID')
type = form.getvalue('TypeID')

# Добавление данных в таблицы
cursor.execute("INSERT INTO Transport(Model,Weight,Power,FirmID,TypeID) VALUES(?,?,?,?,?)",
                (model, weight, power, firm, type,))
connection.commit()



print ("</body>")
print ("</html>")