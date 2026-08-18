# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl1 = QLabel(self.centralwidget)
        self.lbl1.setObjectName(u"lbl1")
        self.lbl1.setEnabled(True)
        self.lbl1.setGeometry(QRect(0, 130, 1911, 371))
        font = QFont()
        font.setFamilies([u"Monotype Corsiva"])
        font.setPointSize(56)
        font.setItalic(True)
        self.lbl1.setFont(font)
        self.lbl1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl2 = QLabel(self.centralwidget)
        self.lbl2.setObjectName(u"lbl2")
        self.lbl2.setGeometry(QRect(0, 230, 1921, 181))
        self.lbl2.setFont(font)
        self.lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt1 = QLineEdit(self.centralwidget)
        self.txt1.setObjectName(u"txt1")
        self.txt1.setGeometry(QRect(760, 460, 411, 171))
        font1 = QFont()
        font1.setFamilies([u"Monotype Corsiva"])
        font1.setPointSize(41)
        self.txt1.setFont(font1)
        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setGeometry(QRect(760, 660, 411, 51))
        self.btn2.setFont(font1)
        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(760, 460, 411, 171))
        font2 = QFont()
        font2.setFamilies([u"Monotype Corsiva"])
        font2.setPointSize(48)
        font2.setItalic(True)
        self.btn1.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0430\u043d\u0438\u0435 \u043d\u0430\u043b\u0438\u0447\u0438\u044f \u0441\u0435\u0440\u0434\u0435\u0447\u043d\u043e-\u0441\u043e\u0441\u0443\u0434\u0438\u0441\u0442\u044b\u0445 \u0437\u0430\u0431\u043e\u043b\u0435\u0432\u0430\u043d\u0438\u0439", None))
        self.lbl2.setText("")
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
    # retranslateUi

