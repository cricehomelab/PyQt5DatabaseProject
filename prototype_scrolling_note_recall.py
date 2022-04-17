# This is an experiment modified from https://www.pythonguis.com/tutorials/qscrollarea/ I am looking to implement this
# idea into my code for the right-hand column in order to allow for any note to be recalled.

from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys

from database import Database
from os import getcwd

DB_PATH = f"{getcwd()}\\database.db"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.database = Database()
        self.scrollUI()


    def scrollUI(self):
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        list_of_notes = self.get_note_list(DB_PATH)
        print(list_of_notes)

        for num, note in enumerate(list_of_notes):
            note_object = QPushButton(note[1])
            self.vbox.addWidget(note_object)


        self.widget.setLayout(self.vbox)

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()

        return


    def get_note_list(self, conn):
        conn = self.database.create_connection(DB_PATH)
        self.db_notes = self.database.get_user_notes(conn)
        return self.db_notes

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
