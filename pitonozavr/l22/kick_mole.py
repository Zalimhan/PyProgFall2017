# Запуск приложения, запуск окна.
# Создаем 9 нор, 3х3, из которых высовывается крот.
# Эти норы должны хранить изображение норы и быть кликабельными.
# Крот должен высовываться.
# Игрок может колотить крота.
# Счетчик попаданий по голове крота



import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

UNACTIVE = "bo1.png"
ACTIVE = "bo2.png"

class MyWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		grid = QGridLayout()
		grid.setSpacing(10)

		self.holes = []
		k, n = 0, 0

		for i in range(9):
			self.holes.append(QPushButton("U", self))
			self.holes[i].setIcon(QIcon(UNACTIVE))
			self.holes[i].setIconSize(QSize(200, 200))

			grid.addWidget(self.holes[i], k, n)

			if k < 2:
				k += 1
			else:
				n += 1
				k = 0



		self.setWindowTitle("Бей крота")
		self.setGeometry(50, 50, 1024, 800)
		self.show()

		

if __name__ == "__main__":
	base_app = QApplication(sys.argv)
	window = MyWindow()
	sys.exit(base_app.exec_())