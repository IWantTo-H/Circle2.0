import random
import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication
from PyQt6.QtGui import QPainter, QPen, QColor


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 534, 528)
        self.btn = QPushButton('Нажать', self)
        self.btn.move(210, 440)
        self.btn.resize(101, 31)
        self.painter = Painter(self)
        self.circles = []
        self.btn.clicked.connect(self.draw)

    def draw(self):
        width = self.width()
        height = self.height()
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        x = random.randint(50, width - 50)
        y = random.randint(50, height - 50)
        radius = random.randint(20, 80)
        self.circles.append((x, y, radius, r, g, b))
        self.painter.update()

class Painter(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(0, 0, 534, 434)

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, radius, r, g, b in self.parent().circles:
            painter.setPen(QPen(QColor(r, g, b), 2))
            painter.drawEllipse(x - radius, y - radius, 2 * radius, 2 * radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())