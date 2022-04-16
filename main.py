import sys
# pip install pyqt5, pip install pyqt5 tools
from PyQt5.QtWidgets import QApplication, QMainWindow
# just change the name
from chart import Ui_MainWindow
# pip install matplotlib
import matplotlib.pyplot as plt
# pip install mysql.connector-python
import mysql.connector

class MainWindow:
    def __init__(self):
        # the way app working
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        # khai bao nut an
        self.uic.Button_start.clicked.connect(self.show_diagram)
    def show_diagram(self):
        self.fig, self.ax = plt.subplots()
        plt.ion()
        while True:
            # load database
            db = mysql.connector.connect(user='root', password='1234',
                                         host='127.0.0.1', database='new_database')
            # command
            code_8 = 'SELECT name,km FROM distance'
            # run command
            mycursor = db.cursor()
            mycursor.execute(code_8)
            # result
            result = mycursor.fetchall()
            print(result)
            datas = (result[0][0], result[1][0], result[2][0], result[3][0], result[4][0])
            datas1 = (result[0][1], result[1][1], result[2][1], result[3][1], result[4][1])
            explode = (0.2, 0.1, 0, 0, 0)
            print("label: ", datas)
            print("data: ", datas1)

            self.ax.clear()
            self.ax.pie(datas1, labels=datas, autopct='%1.2f%%', explode=explode,
                        shadow=True, startangle=90)  # , explode=explode

            plt.pause(2)

    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
