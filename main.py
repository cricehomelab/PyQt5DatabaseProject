import sys
import main_window
from database import Database
from PyQt5 import QtWidgets
from os.path import exists
from os import getcwd

DB_PATH = f"{getcwd()}\\database.db"

database = Database()

if __name__ == '__main__':

    if not exists(DB_PATH):
        for table in database.sql_create_tables:
            db_conn = database.create_connection(DB_PATH)
            database.create_table(db_conn, table)
    else:
        print("database already exists.")

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = main_window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
