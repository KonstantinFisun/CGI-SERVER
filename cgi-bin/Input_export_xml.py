from xml.dom import minidom
import sqlite3

# Подключаем бд
connection = sqlite3.connect("C:\\Users\\kosty\\OneDrive\\Документы\\GitHub\\CGI-SERVER\\land_transport.db")
# Создание курсора
cursor = connection.cursor()

# Экспортируем таблицу в xml

# Создаем документ
root = minidom.Document()

#Главный потомок
xml = root.createElement('Database')
root.appendChild(xml)



#Создаем потомка(таблицу)
table = root.createElement('table') # Таблица аблицы
table.setAttribute('name','Type_transport') # Название таблицы
xml.appendChild(table) # Добавляем



# Создаем id - записи
id = root.createElement('id')
id.setAttribute('id', 'pi')
table.appendChild(id)

# Создаем поля
field = root.createElement('field')
id.appendChild(field)

# Добавляем запись
text = root.createTextNode('lol')
field.appendChild(text)


# Добавляем табуляцию
xml_str = root.toprettyxml(indent="\t")

# Сохраняем
save_path_file = "gfg.xml"
with open(save_path_file, "w") as f:
    f.write(xml_str)