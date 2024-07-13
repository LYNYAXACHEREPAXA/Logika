from PyQt5.QtCore import Qt   # основні модулі підключаєм
from PyQt5.QtWidgets import *


app = QApplication([]) 

menu_win = QWidget() 
menu_win.resize(400,300) # змінюємо розмір віджета

txt_Question = QLineEdit('') #поля для ВВЕДЕННЯ запитання (вписуватиме користувач)
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_form = QFormLayout() #створюємо форму куди буде вводити користувач

layout_form.addRow('Питання', txt_Question) # тексти до поля (вони будуть зліва)
layout_form.addRow('Правильна відповідь:', txt_Answer)
layout_form.addRow('НЕправильна відповідь 1:', txt_Wrong1)
layout_form.addRow('НЕправильна відповідь 2:', txt_Wrong2)
layout_form.addRow('НЕправильна відповідь 3:', txt_Wrong3)

btn_back = QPushButton('Назад') #кнопки на які можна натискати
btn_add_q = QPushButton('Додати питання')
btn_clear = QPushButton('Очистити')

hbtn = QHBoxLayout() # горизонтальна лінія на якій будуть розміщені інші
hbtn.addWidget(btn_back) # додаємо кнопки на лінію
hbtn.addWidget(btn_add_q)
hbtn.addWidget(btn_clear)

vline = QVBoxLayout() 
vline.addLayout(layout_form) # форму накладаєм на вертикальну лінію
vline.addLayout(hbtn)  # з'єднуємо горизонтальну та вертикальну лінії 

menu_win.setLayout(vline) 
