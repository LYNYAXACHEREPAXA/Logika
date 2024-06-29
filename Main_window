from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
 
app = QApplication([])
 
# головне вікно:
my_win = QWidget()
my_win.setWindowTitle('Визначник переможця')
my_win.move(100, 100)
my_win.resize(400, 200)


#віджети вікна: кнопка та напис
button = QPushButton('Згенерувати')
text = QLabel('Натисніть, щоб дізнатися переможця')
winner = QLabel('?')


#розташування віджетів
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
my_win.setLayout(line)
 
#функція, яка генерує та показує число
def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Переможець:')
 
#обробка натискання на кнопку
button.clicked.connect(show_winner)


my_win.show()
app.exec_()
