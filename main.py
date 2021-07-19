import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import database as db
import messagebox as message


class LandingPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(LandingPage, self).__init__()
        loadUi('homepage.ui', self)

        self.addstudentbutton.clicked.connect(self.addstudentClicked)
        self.addcoursebutton.clicked.connect(self.addcourseClicked)

    def addstudentClicked(self):
        self.newWin = AddStudent()
        self.newWin.show()
        self.close()

    def addcourseClicked(self):
        self.newWin = AddCourse()
        self.newWin.show()
        self.close()


class AddStudent(QtWidgets.QMainWindow):
    def __init__(self):
        super(AddStudent, self).__init__()
        loadUi('students.ui', self)
        self.configureWidgets()

    def configureWidgets(self):
        self.fillTable()
        self.course.addItems(db.allCourseCode())
        self.addbutton.clicked.connect(self.addbuttonClicked)
        self.updatebutton.clicked.connect(self.updatestudentClicked)
        self.viewstudents.itemDoubleClicked.connect(self.itemDoubleclicked)
        self.searchbutton.clicked.connect(self.searchbuttonClicked)
        self.clearbutton.clicked.connect(self.clearbuttonClicked)
        self.deletebutton.clicked.connect(self.deletebuttonClicked)

    def fillTable(self, rows=db.allStudent()):
        data = rows
        self.viewstudents.setRowCount(len(data))
        row = 0

        self.viewstudents.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        for i in data:
            self.viewstudents.setItem(row, 0, QTableWidgetItem(str(i[0])))
            self.viewstudents.setItem(row, 1, QTableWidgetItem(str(i[1])))
            self.viewstudents.setItem(row, 2, QTableWidgetItem(str(i[2])))
            self.viewstudents.setItem(row, 3, QTableWidgetItem(str(i[3])))
            self.viewstudents.setItem(row, 4, QTableWidgetItem(str(i[4])))
            row += 1

    def addbuttonClicked(self):
        self.ID = self.studentID.text()
        self.NAME = self.name.text()
        self.GENDER = self.gender.text()
        self.YEAR = self.year.text()
        self.COURSE = self.course.currentText()

        # check for field completeness and validity
        if self.ID and self.ID not in db.existingID() and self.NAME and self.GENDER and self.YEAR and self.COURSE:
            db.recordNewStudent(self.ID, self.NAME, self.GENDER, int(self.YEAR), self.COURSE)
            self.clearEntry()
        else:
            message.invalidInfo(self)
        self.fillTable(rows=db.allStudent())

    # this will be called once a row is double-clicked in the tableWidget
    def itemDoubleclicked(self, item):
        id = self.viewstudents.item(self.viewstudents.currentRow(), 0).text()
        name = self.viewstudents.item(self.viewstudents.currentRow(), 1).text()
        gender = self.viewstudents.item(self.viewstudents.currentRow(), 2).text()
        year = self.viewstudents.item(self.viewstudents.currentRow(), 3).text()
        course = self.viewstudents.item(self.viewstudents.currentRow(), 4).text()

        self.studentID.setText(id)
        self.name.setText(name)
        self.gender.setText(gender)
        self.year.setText(year)
        self.course.setCurrentText(course)

    def updatestudentClicked(self):
        self.ID = self.studentID.text()
        self.NAME = self.name.text()
        self.GENDER = self.gender.text()
        self.YEAR = self.year.text()
        self.COURSE = self.course.currentText()

        # check for field completeness and validity
        if self.ID and self.NAME and self.GENDER and self.YEAR and self.COURSE:
            db.updateStudent(self.ID, self.NAME, self.GENDER, int(self.YEAR), self.COURSE)
            self.clearEntry()
        else:
            message.invalidInfo(self)

        self.fillTable(rows=db.allStudent())

    # this will clear all input in the lineEdit fields
    def clearEntry(self):
        self.studentID.clear()
        self.name.clear()
        self.gender.clear()
        self.year.clear()

    def searchbuttonClicked(self):
        inp = self.input.text()
        result = db.searchResult(inp)
        self.fillTable(result)

    def clearbuttonClicked(self):
        self.input.clear()
        self.fillTable()

    def deletebuttonClicked(self):
        self.ID = self.studentID.text()
        if self.ID in db.existingID():
            if message.confirmDelete():
                db.deleteStudent(self.ID)
                self.clearEntry()

        self.fillTable(rows=db.allStudent())


class AddCourse(QtWidgets.QMainWindow):
    def __init__(self):
        super(AddCourse, self).__init__()
        loadUi('courses.ui', self)
        self.widgets()

    def widgets(self):
        self.fillTable()
        self.coursetable.itemDoubleClicked.connect(self.itemDoubleclicked)
        self.addcourse.clicked.connect(self.addcourseClicked)
        self.updatecourse.clicked.connect(self.updatecourseClicked)
        self.deletecourse.clicked.connect(self.deletebuttonClicked)

    def addcourseClicked(self):
        print("works here")
        self.code = self.courseCode.text()
        self.name = self.courseName.text()

        print("works input")
        # check for field completeness and validity
        if self.code and self.code not in db.existingcode() and self.name:
            db.recordNewCourse(self.code, self.name)
            print("works if")
            self.fillTable()
            print("works fill")
        else:
            message.invalidInfo(self)
        print("works checker")
        self.fillTable(rows=db.allCourses())

    def fillTable(self, rows=db.allCourses()):
        print("workstable")
        data = rows
        self.coursetable.setRowCount(len(data))
        row = 0

        for i in data:
            self.coursetable.setItem(row, 0, QTableWidgetItem(str(i[0])))
            self.coursetable.setItem(row, 1, QTableWidgetItem(str(i[1])))
            row += 1

    def itemDoubleclicked(self, item):
        print("works")
        code = self.coursetable.item(self.coursetable.currentRow(), 0).text()
        name = self.coursetable.item(self.coursetable.currentRow(), 1).text()

        self.courseCode.setText(code)
        self.courseName.setText(name)

    def updatecourseClicked(self):
        self.code = self.courseCode.text()
        self.name = self.courseName.text()
        print("works")
        if self.code and self.name:
            db.updateCourse(self.code, self.name)
            print("works")
            self.clearEntry()
        else:
            message.invalidInfo(self)

        self.fillTable(rows=db.allCourses())


    def deletebuttonClicked(self):
        print("inside")
        self.code = self.courseCode.text()
        print("works input")
        if self.code in db.existingcode():
            print("works if")
            if message.confirmDelete():
                db.deleteCourse(self.code)
                self.clearEntry()
            print("deleted")

        self.fillTable(rows=db.allCourses())
        print("fill")


app = QApplication(sys.argv)
win = LandingPage()
win.show()
sys.exit(app.exec_())
