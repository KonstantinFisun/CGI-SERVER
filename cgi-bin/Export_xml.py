from xml.dom import minidom
import sqlite3

# Подключаем бд
connection = sqlite3.connect("Z:\\CGI-SERVER\\land_transport.db")
# Создание курсора
cursor = connection.cursor()

# Экспортируем таблицу в xml

# Создаем документ
root = minidom.Document()

#Главный потомок
xml = root.createElement('Database')
root.appendChild(xml)




#Создаем потомка(таблицу) Type_Transport
table = root.createElement('table') # Таблица аблицы
table.setAttribute('name', 'Type_transport') # Название таблицы
xml.appendChild(table) # Добавляем

cursor.execute("Select * FROM Type_transport")
type_transport = cursor.fetchall()

# Идем по строкам таблицы
for row in type_transport:
    # Создаем  - записи
    entry = root.createElement('entry')
    table.appendChild(entry)

    # Создаем поля
    field = root.createElement('field')
    entry.appendChild(field)
    # Добавляем запись
    text = root.createTextNode(str(row[0]))
    field.appendChild(text)

    field = root.createElement('field')
    entry.appendChild(field)
    # Добавляем запись
    text = root.createTextNode(str(row[1]))
    field.appendChild(text)




#Создаем потомка(таблицу) Firm
table = root.createElement('table') # Таблица аблицы
table.setAttribute('name', 'Firm') # Название таблицы
xml.appendChild(table) # Добавляем

cursor.execute("Select * FROM Firm")
firm = cursor.fetchall()


# Идем по строкам таблицы
for row in firm:
    # Создаем id - записи
    entry = root.createElement('entry')
    table.appendChild(entry)

    # Создаем поля
    field = root.createElement('field')
    entry.appendChild(field)

    # Добавляем запись
    text = root.createTextNode(str(row[0]))
    field.appendChild(text)

    # Создаем поля
    field = root.createElement('field')
    entry.appendChild(field)
    # Добавляем запись
    text = root.createTextNode(str(row[1]))
    field.appendChild(text)

    # Создаем поля
    field = root.createElement('field')
    entry.appendChild(field)
    # Добавляем запись
    text = root.createTextNode(str(row[2]))
    field.appendChild(text)



#Создаем потомка(таблицу) Transport
table = root.createElement('table') # Таблица аблицы
table.setAttribute('name', 'Transport') # Название таблицы
xml.appendChild(table) # Добавляем

cursor.execute("Select * FROM Transport")
transport = cursor.fetchall()


# Идем по строкам таблицы
for row in transport:
    if(row[3] != None):
        # Создаем - записи
        entry = root.createElement('entry')
        table.appendChild(entry)

        # Создаем поля
        field = root.createElement('field')
        entry.appendChild(field)
        # Добавляем запись
        text = root.createTextNode(str(row[0]))
        field.appendChild(text)

        # Создаем поля
        field = root.createElement('field')
        entry.appendChild(field)
        # Добавляем запись
        text = root.createTextNode(str(row[1]))
        field.appendChild(text)

        # Создаем поля
        field = root.createElement('field')
        entry.appendChild(field)
        # Добавляем запись
        text = root.createTextNode(str(row[2]))
        field.appendChild(text)

        # Создаем поля
        field = root.createElement('field')
        entry.appendChild(field)
        # Добавляем запись
        text = root.createTextNode(str(row[3]))
        field.appendChild(text)

        # Создаем поля
        field = root.createElement('field')
        entry.appendChild(field)
        # Добавляем запись
        text = root.createTextNode(str(row[4]))
        field.appendChild(text)

        # Создаем поля
        field = root.createElement('field')
        entry.appendChild(field)
        # Добавляем запись
        text = root.createTextNode(str(row[5]))
        field.appendChild(text)







# Добавляем табуляцию
xml_str = root.toprettyxml(indent="\t")

# Сохраняем
save_path_file = "gfg.xml"
with open(save_path_file, "w") as f:
    f.write(xml_str)