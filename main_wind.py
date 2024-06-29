from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint

app = QApplication([])

main_wind = QWidget()
main_wind.resize(600, 500)
main_wind.move(300,300)
main_wind.setWindowTitle('Memory card')

#____________________________________________________
 #Створюємо потрібні віджети: кнопки - таймер - надписи
#____________________________________________________

btn_Menu = QPushButton('Меню')

btn_Sleep = QPushButton('Відпочити')
box_Minutes = QSpinBox()
box_Minutes.setValue(30)

btn_OK = QPushButton('Відповісти')

lb_Question = QLabel('')

#____________________________________________________
# Створюємо панель з варіантами відповідей - групуємо
#____________________________________________________

# Рамка для групи кнопок
RadiogroupBox = QGroupBox('Варіанти відповідей')

# всі кнопки в 1 віджет
Radiogroup = QButtonGroup()

# кнопки
rbtn_1 = QRadioButton('a')
rbtn_2 = QRadioButton('b')
rbtn_3 = QRadioButton('c')
rbtn_4 = QRadioButton('d')

# додаємо кнопки до групи
Radiogroup.addButton(rbtn_1)
Radiogroup.addButton(rbtn_2)
Radiogroup.addButton(rbtn_3)
Radiogroup.addButton(rbtn_4)

#____________________________________________________
# Лінії вирівнення (макет)
#____________________________________________________

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() # вертикальні в горизонтальній
layout_ans3 = QVBoxLayout()


# розміщуємо відповіді на лініях
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

# до горизонтальної лінії додаємо вертикальні
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

# На блок накладаємо лінії з віджетами
RadiogroupBox.setLayout(layout_ans1)

#____________________________________________________
# Створюємо блок з результатом тесту
#____________________________________________________

AnsGroupBox = QGroupBox('Результат тесту') 
lb_Result = QLabel('') # надпис результата
lb_Correct = QLabel('') # правильно чи неправильно

# Розміщуємо на рамці

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)

AnsGroupBox.setLayout(layout_res) #
AnsGroupBox.hide()

#____________________________________________________
# Розміщуємо всі віджети у вікні
#____________________________________________________

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

# об'єкти на першій лінії (кнопки меню, сну та надпис)
layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('хвилин'))

# надпис питання
layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

# рамки
layout_line3.addWidget(RadiogroupBox)
layout_line3.addWidget(Radiogroup)

# наступне питання
layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch= 2)
layout_line4.addStretch(1)

# 4 горизонтальні на 1 вертикальну
layout_cards = QVBoxLayout()
layout_cards.addLayout(layout_line1, stretch=1)
layout_cards.addLayout(layout_line2, stretch=2)
layout_cards.addLayout(layout_line3, stretch=8)

layout_cards.addStretch(1)
layout_cards.addLayout(layout_line4, stretch=1)
layout_cards.addStretch(1)
layout_cards.addSpacing(5) # прогалини між вмістом

main_wind.setLayout(layout_cards) # передаємо на головне вікно основний макет
main_wind.show()
app.exec_()
