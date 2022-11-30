import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
from from_staff import Ui_Form
class MyWidget(QWidget,Ui_Form):
    def __init__(self):
        super(MyWidget,self).__init__()
        self.setupUi(self)
        self.pushButtonOpen.clicked.connect(self.open)
        self.pushButtonAdd.clicked.connect(self.insert)
        self.pushButtonDelete.clicked.connect(self.delete)
        self.pushButtonFind.clicked.connect(self.find_for_val())
    def open(self):
        try:
            self.conn=sqlite3.connect('staff_db.db')
            cur=self.conn.cursor()
            data=cur.execute("select * from staff")
            col_name = [i[0] for i in data.description]
            data_rows=data.fetchall()
        except Exception as e:
            print(f'Ошибка подключение к БД{e}')
            return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        self.cb_Find.addItems(col_name)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount()+1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i,j,QTableWidgetItem(str(elem)))
        self.twStaff.resizeColumnsToConnect
        self.avg_age()

    def insert(self):
        row=[self.lineFio, 'муж' if self.radioButton.isChecked() else 'жен', self.lineAge]
        cur=self.conn.cursor()
        cur.execute(f"")


        try:
            cur=self.conn.cursor()
            cur.execute()
            pass
        except Exception as e:
            print('Ошибка добавления записи')
            return e
        self.update()
    def update(self, query="select * from staff"):
        pass

    def delete_staff(self):
        row = self.twStaffs.currentRow()
        num = self.twStaffs.item(row, 0).text()
        try:
            cur = self.conn.cursor()
            cur.execute(f"delete from staff where num = {num}")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(f"Исключение: {e}")
            return e
        self.update_twStaffs()
    def avg_age(self):
        try:
            cur = self.conn.cursor()
            avg = cur.execute("select avg(age) as avg from staff").fetchone()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.label_SrAge.setText(f"Средний возрст {round(avg[0], 2)}")

#STAFF_POS=['бух','дир','инж']
    def find_for_val(self):
        val = self.lineFind.text()
        col = self.cbColNames.itemText(self.cbColNames.currentIndex())
        self.update_twStaffs(f"select * from staff where {col} like '{val}%'")
        # try:
        #     cur = self.conn.cursor()
        #     avg = cur.execute(f"select * from staff where {col} like '{val}%'").fetchone()
        # except Exception as e:
        #     print(f"Проблемы с подключением к БД. {e}")
        #     return e
        # self.lblAvgAge.setText(f"Средний возрст {round(avg[0], 2)}")

    def closeEvent(self, event):
        if self.conn is not None:
            self.conn.close()
        event.accept()


if __name__ =='__main__':
    app=QApplication(sys.argv)
    ex=MyWidget()
    ex.show()
    sys.exit(app.exec())