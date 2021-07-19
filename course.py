# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'courses.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_coursesui(object):
    def setupUi(self, coursesui):
        coursesui.setObjectName("coursesui")
        coursesui.resize(738, 373)
        coursesui.setStyleSheet("QWidget#MainWindow{\n"
"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.911, y2:1, stop:0 rgba(79, 255, 159, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.centralwidget = QtWidgets.QWidget(coursesui)
        self.centralwidget.setObjectName("centralwidget")
        self.coursetable = QtWidgets.QTableWidget(self.centralwidget)
        self.coursetable.setGeometry(QtCore.QRect(274, 11, 451, 311))
        self.coursetable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.coursetable.setObjectName("coursetable")
        self.coursetable.setColumnCount(2)
        self.coursetable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.coursetable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.coursetable.setHorizontalHeaderItem(1, item)
        self.coursetable.horizontalHeader().setStretchLastSection(True)
        self.coursecodelabel = QtWidgets.QLabel(self.centralwidget)
        self.coursecodelabel.setGeometry(QtCore.QRect(11, 11, 73, 16))
        self.coursecodelabel.setObjectName("coursecodelabel")
        self.addcourse = QtWidgets.QPushButton(self.centralwidget)
        self.addcourse.setGeometry(QtCore.QRect(10, 200, 251, 28))
        self.addcourse.setObjectName("addcourse")
        self.courselabel = QtWidgets.QLabel(self.centralwidget)
        self.courselabel.setGeometry(QtCore.QRect(11, 129, 40, 16))
        self.courselabel.setObjectName("courselabel")
        self.updatecourse = QtWidgets.QPushButton(self.centralwidget)
        self.updatecourse.setGeometry(QtCore.QRect(10, 240, 251, 28))
        self.updatecourse.setObjectName("updatecourse")
        self.deletecourse = QtWidgets.QPushButton(self.centralwidget)
        self.deletecourse.setGeometry(QtCore.QRect(10, 280, 251, 28))
        self.deletecourse.setObjectName("deletecourse")
        self.courseName = QtWidgets.QLineEdit(self.centralwidget)
        self.courseName.setGeometry(QtCore.QRect(10, 150, 251, 31))
        self.courseName.setObjectName("courseName")
        self.courseCode = QtWidgets.QLineEdit(self.centralwidget)
        self.courseCode.setGeometry(QtCore.QRect(10, 30, 251, 31))
        self.courseCode.setObjectName("courseCode")
        coursesui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(coursesui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 26))
        self.menubar.setObjectName("menubar")
        coursesui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(coursesui)
        self.statusbar.setObjectName("statusbar")
        coursesui.setStatusBar(self.statusbar)

        self.retranslateUi(coursesui)
        QtCore.QMetaObject.connectSlotsByName(coursesui)

    def retranslateUi(self, coursesui):
        _translate = QtCore.QCoreApplication.translate
        coursesui.setWindowTitle(_translate("coursesui", "MainWindow"))
        item = self.coursetable.horizontalHeaderItem(0)
        item.setText(_translate("coursesui", "Course Code"))
        item = self.coursetable.horizontalHeaderItem(1)
        item.setText(_translate("coursesui", "Course"))
        self.coursecodelabel.setText(_translate("coursesui", "Course Code"))
        self.addcourse.setText(_translate("coursesui", "ADD COURSE"))
        self.courselabel.setText(_translate("coursesui", "Course"))
        self.updatecourse.setText(_translate("coursesui", "UPDATE COURSE"))
        self.deletecourse.setText(_translate("coursesui", "DELETE COURSE "))