import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QHeaderView

class HealthDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Widgets
        self.stepsInput = QLineEdit(self)
        self.heartRateInput = QLineEdit(self)
        self.sleepInput = QLineEdit(self)
        
        self.submitButton = QPushButton('Submit Data', self)
        self.submitButton.clicked.connect(self.updateTable)

        self.table = QTableWidget(self)
        self.table.setRowCount(0)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Steps", "Heart Rate", "Sleep Hours"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Daily Steps:'))
        layout.addWidget(self.stepsInput)
        layout.addWidget(QLabel('Heart Rate:'))
        layout.addWidget(self.heartRateInput)
        layout.addWidget(QLabel('Sleep Hours:'))
        layout.addWidget(self.sleepInput)
        layout.addWidget(self.submitButton)
        layout.addWidget(self.table)

        centralWidget = QWidget(self)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # Window properties
        self.setWindowTitle('Fitness and Health Dashboard')
        self.setGeometry(300, 300, 400, 400)

    def updateTable(self):
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)

        self.table.setItem(rowPosition, 0, QTableWidgetItem(self.stepsInput.text()))
        self.table.setItem(rowPosition, 1, QTableWidgetItem(self.heartRateInput.text()))
        self.table.setItem(rowPosition, 2, QTableWidgetItem(self.sleepInput.text()))

        # Clear input fields
        self.stepsInput.clear()
        self.heartRateInput.clear()
        self.sleepInput.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = HealthDashboard()
    mainWin.show()
    sys.exit(app.exec_())
