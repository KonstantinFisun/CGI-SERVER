import sqlite3

# Создание соедиения с базой
connection = sqlite3.connect("Z:\\CGI-SERVER\\land_transport.db")
# Создание курсора
cursor = connection.cursor()
#
# Создание таблиц
# cursor.execute("""CREATE TABLE IF NOT EXISTS Type_transport
#                   (TypeID INTEGER PRIMARY KEY AUTOINCREMENT,
#                   Title VARCHAR(20));
#                """)
# connection.commit()
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS Firm
#                     (FirmID INTEGER PRIMARY KEY AUTOINCREMENT,
#                     Title VARCHAR(30),
#                     Country VARCHAR(40));
#                 """)
# connection.commit()
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS Transport
#                     (CarID INTEGER PRIMARY KEY AUTOINCREMENT,
#                     Model VARCHAR(20),
#                     Power INTEGER,
#                     Weight INTEGER,
#                     TypeID INTEGER,
#                     FirmID INTEGER,
#                     FOREIGN KEY (TypeID) REFERENCES Type_transport(TypeID),
#                     FOREIGN KEY (FirmID) REFERENCES Firm(FirmID));
#                 """)


# types = [('Camera with interchangeable optics'),
#          ('Film camera'),
#          ('Instant printing camera'),
#          ('Compact camera'),
#          ('Slr camera')]
#
# resolutions = [('720x480'),
#                ('1920x1080'),
#                ('2560x1440'),
#                ('2688x1520'),
#                ('2704x1520'),
#                ('2880x2160'),
#                ('3840x2160')]
#
# cameras = [('Fujifilm', 'QuickSnap CD20', '2', '1799'),
#            ('Canon', 'Zoemini C', '3', '6299'),
#            ('Fujifilm', 'Instax mini 9', '3', '5999'),
#            ('DEXP', 'Kid`s Printing Cam', '3', '5299'),
#            ('DEXP', 'Kid`s Cam', '4', '1650'),
#            ('Rekam', 'iLook K410i', '4', '1199'),
#            ('Sony', 'Alpha ILCE-6000B Body', '1', '47999')]
#
# videoCameras = [('Canon', 'XA11', '2', '106999'),
#                 ('Sony', 'FDR-AX53', '7', '89999'),
#                 ('Panasonic', 'V260', '2', '22999'),
#                 ('Rekam', 'DVC-560', '4', '6299')]
#
# actionCameras = [('Aceline', 'S-60', '7', '2699'),
#                  ('Digma', 'DiCam 300', '7', '1899'),
#                  ('Aceline', 'S-40', '2', '1499'),
#                  ('Digma', 'DiCam 170', '2', '1299'),
#                  ('SJCAM', 'FUNCAM', '2', '1199')]

# connection.commit()
#
# # Данные таблиц
# # Данные таблицы Type_transport
# cursor.execute("INSERT INTO Type_transport(Title) VALUES('Мотоцикл');")
# cursor.execute("INSERT INTO Type_transport(Title) VALUES('Легковая');")
# cursor.execute("INSERT INTO Type_transport(Title) VALUES('Грузовая');")
# cursor.execute("INSERT INTO Type_transport(Title) VALUES('Трактор');")
# cursor.execute("INSERT INTO Type_transport(Title) VALUES('Автобус');")
# connection.commit()
#
# # Данные таблицы Firm
# cursor.execute("INSERT INTO Firm(Title, Country) VALUES('Марседес', 'Германия');")
# cursor.execute("INSERT INTO Firm(Title, Country) VALUES('Тойота', 'Япония');")
# cursor.execute("INSERT INTO Firm(Title, Country) VALUES('BMW', 'Германия');")
# cursor.execute("INSERT INTO Firm(Title, Country) VALUES('Lada', 'РОССИЯ');")
#
# connection.commit()
#
#
# # Данные таблицы Transport
# cursor.execute("INSERT INTO Transport(Model, Weight, Power, TypeID, FirmID) VALUES('Camry', '2500', '200', '2', '2');")
# cursor.execute("INSERT INTO Transport(Model, Weight, Power, TypeID, FirmID) VALUES('Vesta', '1770', '100', '4', '4');")
# cursor.execute("INSERT INTO Transport(Model, Weight, Power, TypeID, FirmID) VALUES('I8', '1855', '231', '2', '3');")
#
# connection.commit()


# cursor.execute("DELETE FROM cameras WHERE cameraID = 9")
#cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ = 7 WHERE NAME = 'cameras';")
#connection.commit()
# manufact = 'Hi'
# mode = 'huy'
# typ = '10'
# pric = '100'

#cursor.execute("INSERT INTO cameras(manufacturer, model, typeID, price) VALUES(?, ?, ?, ?)", (manufact, mode, typ, pric))
# cursor.execute("SELECT * FROM cameras")
# print(cursor.fetchall())
#
# # Закрытие соединения

cursor.execute("Delete from Transport where Model = 'None'")
connection.commit()

connection.close()