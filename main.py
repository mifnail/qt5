import sys
from PyQt5.QtWidgets import QWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('ПерваяПрограмма')
if __name__ =='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    ex.show()
    sys.exit(app.exec())