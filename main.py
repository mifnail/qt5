import sys
import sqlite3
from PyQt5.QtWidgets import QApplication,QWidget
from from_staff import Ui_Form
class MyWidget(QWidget,Ui_Form):
    def __init__(self):
        super(MyWidget,self).__init__()
        self.setupUi(self)
        self.pushButtonOpen.clicked.connect(self.open())
    def open(self):
        try:
            self.conn=sqlite3.connect('staff_db.db')
            cur=self.conn.cursor()
            data=cur.execute("select * from staff")
            col_name = [i[0] for i in data.description]
            data_rows=data.fetchall()
        except Exception as e:
            print('Ошибка подключение к БД')
            return e
        self.twStaffs.setColumnCount(len(col_name))

        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount()+1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i,j,QTableWidgetItem(str(elem)))
        self.twStaff.resizeColumnsToConnect


if __name__ =='__main__':
    app=QApplication(sys.argv)
    ex=MyWidget()
    ex.show()
    sys.exit(app.exec())