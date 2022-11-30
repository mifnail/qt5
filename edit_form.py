import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLCDNumber, QLineEdit

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('ПерваяПрограмма')
        self.btn1=QPushButton('Кнопка1',self)
        self.btn1.resize(self.btn.sizeHint())
        self.btn1.move(90,40)
        self.btn1.clicked.connect(self.run)

        self.btn2 = QPushButton('Кнопка2', self)
        self.btn2.resize(self.btn.sizeHint())
        self.btn2.move(90, 80)
        self.btn2.clicked.connect(self.run)

        self.label = QLabel(self)

    def run(self):
        self.label.setText(self.sender())




if __name__ =='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    ex.show()
    sys.exit(app.exec())