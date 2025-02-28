# Содержимое файла UI/main_ui.py

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CoffeeApp(object):
    def setupUi(self, CoffeeApp):
        CoffeeApp.setObjectName("CoffeeApp")
        CoffeeApp.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CoffeeApp)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.verticalLayout.addWidget(self.pushButtonAdd)
        self.pushButtonEdit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.verticalLayout.addWidget(self.pushButtonEdit)
        CoffeeApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CoffeeApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        CoffeeApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CoffeeApp)
        self.statusbar.setObjectName("statusbar")
        CoffeeApp.setStatusBar(self.statusbar)

        self.retranslateUi(CoffeeApp)
        QtCore.QMetaObject.connectSlotsByName(CoffeeApp)

    def retranslateUi(self, CoffeeApp):
        _translate = QtCore.QCoreApplication.translate
        CoffeeApp.setWindowTitle(_translate("CoffeeApp", "CoffeeApp"))
        self.pushButtonAdd.setText(_translate("CoffeeApp", "Добавить запись"))
        self.pushButtonEdit.setText(_translate("CoffeeApp", "Редактировать запись"))
