from xml.dom import minidom
import sqlite3

# Создание соедиения с базой
connection = sqlite3.connect("Z:\\CGI-SERVER\\land_transport.db")
# Создание курсора
cursor = connection.cursor()

docTree = minidom.parse("Z:\\CGI-SERVER\\cgi-bin\\gfg.xml")


tables = docTree.getElementsByTagName("table")

# Ходим по таблицам
for table in tables:

    name_table = str(table.getAttribute("name"))

    entrys = table.getElementsByTagName("entry")

    for entry in entrys:

        fields = entry.getElementsByTagName("field")

        cartezh = list()

        for field in fields:
            cartezh.append(field.childNodes[0].data)

        cursor.execute(f"INSERT INTO {name_table} VALUES {tuple(cartezh)}")

        connection.commit()
connection.close()