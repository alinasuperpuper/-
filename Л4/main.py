import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from database import Database


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.init_ui()
        self.setWindowTitle('Пример приложения')

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel('Записи:')
        layout.addWidget(self.label)

        button_open = QPushButton('Показать записи')
        button_open.clicked.connect(self.show_view)
        layout.addWidget(button_open)

        self.setLayout(layout)

    def show_view(self):
        self.label.setText(", ".join(self.db.records))

    def is_record_visible(self, record):
        return record in self.label.text()

    def is_window_open(self):
        return self.isVisible()

    def open_window(self):
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.open_window()
    sys.exit(app.exec())
