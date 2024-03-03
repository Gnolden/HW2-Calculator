import sys

from PyQt5 import QtWidgets
from calculator import Ui_MainWindow



class MainWidget(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        # loadUi('calculator.ui', self)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.main)
        self.select.clicked.connect(self.select_shape)
        self.back.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main))
        self.calculate.clicked.connect(self.calculate_clicked)

    def select_shape(self):
        shape_name = self.shape_group.checkedButton().objectName()
        self.stackedWidget.setCurrentWidget(
            getattr(self, f'{shape_name}_page', self.main)
        )

    def calculate_clicked(self):
        # Retrieve the values from the spin boxes and display them
        r1_value = self.r1.value()


        s1_value = self.s1.value()
        s2_value = self.s2.value()
        s3_value = self.s3.value()
        s_perimeter = s1_value+ s2_value + s3_value
        s_semi = s_perimeter/2


        trpz_1_value = self.trpz1.value()
        trpz_2_value = self.trpz2.value()
        trpz_3_value = self.trpz3.value()
        trpz_4_value = self.trpz4.value()
        trpz_perimeter = trpz_1_value + trpz_2_value + trpz_3_value + trpz_4_value
        try:
            trpz_h = (trpz_3_value ** 2 - ((
                                                       trpz_4_value ** 2 - trpz_2_value ** 2 - trpz_1_value ** 2 + 2 * trpz_1_value * trpz_2_value) ** 2) / (
                                  (2 * trpz_1_value - 2 * trpz_2_value) ** 2)) ** 0.5
        except ZeroDivisionError:
            trpz_h = 0
            print("Error: Division by zero occurred and has been dealt with!")

        sq1_value = self.sq1.value()



        # print("R1 value:", r1_value, "circumference:", 2 * 3.14 * r1_value, "area:", 3.14 * r1_value**2)

        self.lcd_r_perimeter.display(2 * 3.14 * r1_value)
        self.lcd_r_area.display(3.14 * r1_value**2)

        # print("S1 value:", s1_value, "perimeter:", s_perimeter, "area:",  (s_semi * (s_semi - s1_value) * (s_semi - s2_value) * (s_semi - s3_value))** 0.5)
        # print("S2 value:", s2_value)
        # print("S3 value:", s3_value)

        self.lcd_s_perimeter.display(s_perimeter)
        self.lcd_s_area.display((s_semi * (s_semi - s1_value) * (s_semi - s2_value) * (s_semi - s3_value))** 0.5)

        # print("trpz_1 value:", trpz_1_value, "perimeter:", trpz_perimeter, "area", (trpz_1_value + trpz_2_value) / 2.0 * trpz_h)
        # print("trpz_2 value:", trpz_2_value)
        # print("trpz_3 value:", trpz_3_value)
        # print("trpz_4 value:", trpz_4_value)

        self.trpz_height.display(trpz_h)
        self.trpz_perimeter.display(trpz_perimeter)
        self.trpz_area.display((trpz_1_value + trpz_2_value) / 2.0 * trpz_h)


        # print("sq1 value:", sq1_value, "perimeter:", sq1_value*4, "area:", sq1_value**2)

        self.sqr_area.display(sq1_value**2)
        self.sqr_perimeter.display(sq1_value*4)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidget()
    window.show()

    sys.exit(app.exec_())
