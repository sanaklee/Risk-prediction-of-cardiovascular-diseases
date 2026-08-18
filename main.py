from sys import exit, argv
from os import path, environ, chdir
import PySide6
from joblib import load
from subprocess import run
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow

dirname = path.dirname(PySide6.__file__)
plugin_path = path.join(dirname, 'plugins', 'platforms')
environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
chdir(path.dirname(__file__))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lbl2.hide()
        self.ui.txt1.hide()
        self.ui.btn2.hide()
        self.setStyleSheet("QPushButton { background-color: white; }")
        self.setStyleSheet("color: #DB7093;")
        self.ui.lbl1.setStyleSheet("color: #DB7093;") 
        self.ui.lbl1.setAlignment(PySide6.QtCore.Qt.AlignCenter)
        self.ui.lbl2.setAlignment(PySide6.QtCore.Qt.AlignCenter)
        self.ui.txt1.setAlignment(PySide6.QtCore.Qt.AlignCenter)
        self.ui.btn1.clicked.connect(self.on_btn1_clicked)
        self.ui.btn2.clicked.connect(self.on_btn2_clicked)

        self.threshold = load('best_threshold.pkl')
        self.medians = load('medians.pkl')
        self.model = load('tree_model.pkl')
        self.features = load('feature_names.pkl')
        self.user_data = {}
        self.questions = [
    ("Ваш пол (1-муж, 0-жен)?", "male", [0, 1]),
    ("Сколько вам лет?", "age", [0, 130]),
    ("Вы курите сейчас? (1-да, 0-нет)", "currentSmoker", [0, 1]),
    ("Сколько сигарет в день выкуриваете?", "cigsPerDay", [0, 100]),
    ("Принимаете ли лекарства от давления? (1-да, 0-нет)", "BPMeds", [0, 1]),
    ("Был ли у вас инсульт? (1-да, 0-нет)", "prevalentStroke", [0, 1]),
    ("Есть ли у вас гипертония? (1-да, 0-нет)", "prevalentHyp", [0, 1]),
    ("Есть ли у вас диабет? (1-да, 0-нет)", "diabetes", [0, 1]),
    ("Уровень общего холестерина", "totChol", [2, 30]),
    ("Систолическое давление", "sysBP", [50, 250]),
    ("Диастолическое давление", "diaBP", [30, 150]),
    ("Индекс массы тела (BMI) Вес (кг) / (Рост (м) * Рост (м))", "BMI", [11, 52]),
    ("Частота сердечных сокращений", "heartRate", [40, 200]),
    ("Уровень глюкозы", "glucose", [2, 50])
    ]

    def on_btn1_clicked(self):
        self.ui.btn1.hide()
        self.ui.lbl1.hide()

        self.ui.lbl2.show()
        self.ui.txt1.show()
        self.ui.btn2.show()

        first_q, a, b = self.questions[0]
        self.ui.lbl2.setText(first_q)
        
    def on_btn2_clicked(self):
        if self.questions:
            current_q_text, feature_name, borders = self.questions[0]
        value = self.ui.txt1.text().strip()

        if value == '-' or value == '':
          value = self.medians[feature_name]

        else:
            if ',' in value:
                value = value.replace(',', '.')
            try:
                value = float(value)
            except ValueError:
                self.ui.lbl2.setText('Введите число')
                return
            if value < borders[0] or value > borders[1]:
                self.ui.lbl2.setText('Неккоректное значение')
                return
            if feature_name in ['totChol', 'glucose']:
                value *= 18
            if feature_name == 'currentSmoker' and value == 0:
                self.questions.pop(0)
                self.user_data['cigsPerDay'] = 0
        self.user_data[feature_name] = value
        self.questions.pop(0)

        self.ui.txt1.clear()
        
        if self.questions:
            next_data = self.questions[0]
            self.ui.lbl2.setText(next_data[0])

        else:
            self.show_result()

    def show_result(self):
        x = pd.DataFrame([self.user_data], columns=self.features)
        prediction = self.model.predict_proba(x)[0][1]

        if prediction >= self.threshold:
            self.ui.lbl2.setText(f"Риск сердечно-сосудистого заболевания высокий: {prediction*100:.1f}%")
        else:
            self.ui.lbl2.setText(f"Риск сердечно-сосудистых заболеваний низкий: {prediction*100:.1f}%")

        self.ui.txt1.hide()
        self.ui.btn2.hide()

if __name__ == "__main__":
    run(["pyside6-uic", "MainWindow.ui", "-o", "mainwindow.py"])
    app = QApplication(argv)

    window = MainWindow()
    window.showFullScreen()
    exit(app.exec())