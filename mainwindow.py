# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/sf_dik19/Documents/untitled13/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionSave_file = QtWidgets.QAction(MainWindow)
        self.actionSave_file.setObjectName("actionSave_file")
        self.actionAdd_row = QtWidgets.QAction(MainWindow)
        self.actionAdd_row.setObjectName("actionAdd_row")
        self.actionDelete_row = QtWidgets.QAction(MainWindow)
        self.actionDelete_row.setObjectName("actionDelete_row")
        self.actionAdd_column = QtWidgets.QAction(MainWindow)
        self.actionAdd_column.setObjectName("actionAdd_column")
        self.actionDelete_column = QtWidgets.QAction(MainWindow)
        self.actionDelete_column.setObjectName("actionDelete_column")
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.actionSave_file)
        self.menuEdit.addAction(self.actionAdd_row)
        self.menuEdit.addAction(self.actionDelete_row)
        self.menuEdit.addAction(self.actionAdd_column)
        self.menuEdit.addAction(self.actionDelete_column)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionOpen_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_file.setText(_translate("MainWindow", "Save file"))
        self.actionSave_file.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAdd_row.setText(_translate("MainWindow", "Add row"))
        self.actionDelete_row.setText(_translate("MainWindow", "Delete row"))
        self.actionAdd_column.setText(_translate("MainWindow", "Add column "))
        self.actionDelete_column.setText(_translate("MainWindow", "Delete column"))
