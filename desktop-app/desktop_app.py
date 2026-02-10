import sys
import requests
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QGroupBox

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Desktop Dashboard")
        self.resize(400, 300)

        layout = QVBoxLayout()
        group = QGroupBox("Upload Data")
        v = QVBoxLayout()

        self.label = QLabel("No data uploaded")
        v.addWidget(self.label)

        btn = QPushButton("Upload CSV")
        btn.clicked.connect(self.upload_file)
        v.addWidget(btn)

        group.setLayout(v)
        layout.addWidget(group)
        self.setLayout(layout)

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV File")
        if file_path:
            files = {'file': open(file_path, 'rb')}
            res = requests.post("http://127.0.0.1:8000/api/upload/", files=files)
            data = res.json()

            self.label.setText(f"Total Equipment: {data['total_equipment']}")
            labels = list(data["type_distribution"].keys())
            values = list(data["type_distribution"].values())

            plt.bar(labels, values)
            plt.title("Equipment Type Distribution")
            plt.show()

app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())
