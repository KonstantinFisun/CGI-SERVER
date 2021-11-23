#!/usr/bin/python

# Импорт модулей для обработки CGI
import cgi, cgitb
import html
import sqlite3

# Создание соедиения с базой
connection = sqlite3.connect("C:\\Users\\kosty\\OneDrive\\Рабочий стол\\" +
                             "3 курс 5 семестр\\Интерпритируемые языки программирования\\БД\\land_transport.db")
# Создание курсора
cursor = connection.cursor()

# Создание экземпляра FieldStorage
form = cgi.FieldStorage()

# Получение данных из полей
table = form.getvalue('Таблицы')
addTable = form.getvalue('table')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<meta charset=""UTF-8"">")
print ("<title>Наземный транспорт</title>")
print ("</head>")
print ("<body bgcolor = #5F9EA0> ")
print("<div  <div>")
print ("<h1 align = 'center'>Наземный транспорт</h1>")



# Форма выбора таблиц для вывода
print("""<form action = "/cgi-bin/View.py" method = "post">
<select name = "Таблицы">
<option value = "Type_transport">Тип транспорта</option>
<option value = "Firm">Фирмы</option>
<option value = "Transport">Транспорт</option>
</select>
<input type = "submit" value = "Вывести" />
</form>""")

# Форма выбора таблиц для добавления данных
print("""<form action = "/cgi-bin/View.py" method = "post">
<input type = 'radio' name = 'table' value = 'Type_transport' /> Тип транспорта <br>
<input type = 'radio' name = 'table' value = 'Firm' /> Фирмы <br>
<input type = 'radio' name = 'table' value = 'Transport' /> Транспорт <br>
<input type = "submit" value = "Добавить данные" />
</form>""")

# Вывод таблиц на экран
if table == 'Type_transport':
    # Запрос таблицы Тип транспорта
    cursor.execute("""SELECT TypeID, Title
                   FROM Type_transport """)
    type_transport = cursor.fetchall()

    # Таблица Фотоаппараты
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
    # Запрос таблицы Видеокамеры
    cursor.execute("""SELECT FirmID, Title, Country
                       FROM Firm """)
    firm = cursor.fetchall()

    # Таблица Видеокамеры
    print("<table cellspacing = '10'>"
          "<caption><h2>Видеокамеры</h2></caption>"
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
    # Запрос таблицы Экшн-камеры
    cursor.execute("""SELECT CarID, Model, Power, Weight, Firm.Title, Type_transport.Title
                    FROM Transport 
                    JOIN Type_transport ON Transport.TypeID = Type_transport.TypeID
                    JOIN Firm ON Firm.FirmID = Transport.FirmID""")
    actionCams = cursor.fetchall()

    # Таблица Экшн-камеры
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
              "</td><td align = 'center'>", row[4],   "</td><td align = 'center'>", row[5])
    print("</table>")


# Добавление данных в таблицы (просто формочка, когда сюда заходит сначала выполнялся наш запрос,
# а уже потом с формочек читались данные, которые вводили

if addTable == 'Type_transport':
    print("""<form action = "/cgi-bin/View.py" method = "post">
    Название: <input type = "text" name = "Title" /> 
    <input type = 'submit' value = 'Добавить'>
    </form>""")

# elif addTable == 'Firm':
#     print("""<form action = "/cgi-bin/View.py" method = "post">
#         Производитель: <input type = "text" name = "manufacturer" />
#         Модель: <input type = "text" name = "model" />
#         Разрешение: <input type = "text" name = "resolutionID" />
#         Цена: <input type = "text" name = "price" />
#         <input type = 'submit' value = 'Добавить'>
#         </form>""")

# Получение данных из полей
title = form.getvalue('Title')

# Добавление данных в таблицы
if title:
    cursor.execute("INSERT INTO Type_transport(Title) VALUES(?)",
                   (title,))
    connection.commit()



print ("</body>")
print ("</html>")

# Nikon, D3500 Kit 18-55mm VR AF-P, 5, 39999

# Sony, FDR-AX700, 7, 124990