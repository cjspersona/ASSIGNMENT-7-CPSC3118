# converter.py
# Student: CJ Hickson | Course: Graph User Interface Development | Project: Assignment 7 (PySide6) | Date: 04/01/26

import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox,
    QRadioButton, QMessageBox
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt


class ConverterWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Measurement Converter")
        self.setMinimumSize(500, 500)

        self.setup_ui()
        self.apply_styles()

    # ---------------- UI ----------------
    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Title
        self.lblTitle = QLabel("Measurement Converter")
        self.lblTitle.setAlignment(Qt.AlignCenter)
        self.lblTitle.setFont(QFont("Segoe UI", 16, QFont.Bold))

        # IMAGE (FIXED VERSION)
        self.lblImage = QLabel()
        self.lblImage.setAlignment(Qt.AlignCenter)
        self.lblImage.setObjectName("imageBox")

        # 🔥 Correct absolute path handling
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "house.png")

        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                self.lblImage.setPixmap(
                    pixmap.scaled(180, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                )
            else:
                self.lblImage.setText("Image failed to load")
        else:
            self.lblImage.setText("Image not found")

        # Input
        self.txtInput = QLineEdit()
        self.txtInput.setPlaceholderText("Enter a value...")
        self.txtInput.setFixedHeight(35)

        # Radio Buttons
        self.groupBox = QGroupBox("Choose Conversion")

        self.rbInToM = QRadioButton("Inches to Meters")
        self.rbMToIn = QRadioButton("Meters to Inches")
        self.rbInToM.setChecked(True)

        rb_layout = QVBoxLayout()
        rb_layout.addWidget(self.rbInToM)
        rb_layout.addWidget(self.rbMToIn)
        self.groupBox.setLayout(rb_layout)

        # Result
        self.lblResult = QLabel("Result will appear here")
        self.lblResult.setAlignment(Qt.AlignCenter)
        self.lblResult.setObjectName("resultLabel")

        # Buttons
        self.btnConvert = QPushButton("Convert")
        self.btnClear = QPushButton("Clear")
        self.btnExit = QPushButton("Exit")

        self.btnConvert.clicked.connect(self.convert)
        self.btnClear.clicked.connect(self.clear)
        self.btnExit.clicked.connect(QApplication.quit)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btnConvert)
        btn_layout.addWidget(self.btnClear)
        btn_layout.addWidget(self.btnExit)

        # Add everything
        layout.addWidget(self.lblTitle)
        layout.addWidget(self.lblImage)
        layout.addWidget(self.txtInput)
        layout.addWidget(self.groupBox)
        layout.addWidget(self.lblResult)
        layout.addLayout(btn_layout)

        central.setLayout(layout)

    # ---------------- LOGIC ----------------
    def convert(self):
        text = self.txtInput.text().strip()

        if text == "":
            self.show_error("Input cannot be empty.")
            return

        try:
            value = float(text)
        except:
            self.show_error("Value entered is not numeric.")
            return

        if value <= 0:
            self.show_error("Value must be greater than 0.")
            return

        if self.rbInToM.isChecked():
            result = value * 0.0254
            self.lblResult.setText(f"{value:.3f} inches = {result:.3f} meters")
        else:
            result = value / 0.0254
            self.lblResult.setText(f"{value:.3f} meters = {result:.3f} inches")

    def clear(self):
        self.txtInput.clear()
        self.lblResult.setText("Result will appear here")
        self.rbInToM.setChecked(True)
        self.txtInput.setFocus()

    def show_error(self, msg):
        QMessageBox.critical(self, "Error", msg)

    # ---------------- STYLE ----------------
    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #F3E5F5;
                font-family: Segoe UI;
                font-size: 12pt;
                color: #2D1B4E;
            }

            
            QLabel  {
                color: #2D1B4E;
            }
                           
            QLabel#resultLabel {
                background-color: white;
                border: 2px solid #7E57C2;
                border-radius: 10px;
                padding: 10px;
                font-weight: bold;
            }

            QLabel#imageBox {
                border: 2px solid #B39DDB;
                border-radius: 10px;
                background-color: white;
                padding: 5px;
            }

            QLineEdit {
                border: 2px solid #9575CD;
                border-radius: 8px;
                padding: 5px;
                background-color: white;
            }
                           
            QLineEdit::placeholder {
            color: #7E57C2;
            }
                           
            QGroupBox {
                border: 2px solid #7E57C2;
                border-radius: 10px;
                margin-top: 10px;
                padding: 10px;
                font-weight: bold;
                color: #2D1B4E;
            }
                           
            QRadioButton {
                color: #2D1B4E;
                spacing: 8px;
            }          
                 
            QRadioButton::indicator {
                width: 14px;
                height: 14px;
                border-radius: 7px;
                border: 2px solid #5E35B1;
                background-color: white;
            }   

            QRadioButton::indicator:checked {
                background-color: #7E57C2;
            }

            QPushButton {
                border-radius: 8px;
                padding: 8px;
                font-weight: bold;
            }

            QPushButton:hover {
                opacity: 0.9;
            }
        
            QPushButton:nth-child(1) {
                background-color: #7E57C2;
            }

            QPushButton:nth-child(2) {
                background-color: #B39DDB;
                color: #2D1B4E;
            }

            QPushButton:nth-child(3) {
                background-color: #EF5350;
            }
        """)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterWindow()
    window.show()
    sys.exit(app.exec())