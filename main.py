import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLCDNumber

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('ПерваяПрограмма')
        self.btn=QPushButton('Кнопка',self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100,150)
        self.btn.clicked.connect(self.inc_click)

        self.label=QLabel(self)
        self.label.setText('КОличество нажатий на кнопку:')
        self.LCD_count=QLCDNumber(self)
        self.LCD_count.move(110,80)
        self.count =0

    def inc_click(self):
        self.count+=1
        self.LCD_count.display(self.count)




if __name__ =='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    ex.show()
    sys.exit(app.exec())