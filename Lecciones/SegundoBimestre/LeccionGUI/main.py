import sys
from dialog import Ui_Dialog
from PyQt5 import QtWidgets, QtCore, uic



class DialogApplication(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        # Set up the dialog
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)

        # Setup buttons
        self.dialog.radioButtonCelcius2Farenheit.clicked.connect(self.handle_change)
        self.dialog.radioButtonMeters2Centimeters.clicked.connect(self.handle_change)


        # Present the dialog
        self.show()

    def handle_change(self):

        string_input = self.dialog.lineEditInput.text()

        if self.get_option() == 1:
            result = self.meters2centimeters(string_input)
        else:
            result = self.celsius2fahrenheit(string_input)

        self.dialog.lineEditOutput.setText(result)
        
    def get_option(self):
        if self.dialog.radioButtonMeters2Centimeters.isChecked():
            return 1
        else:
            return 2

    def meters2centimeters(self, meters : str):
        target = int(meters)
        result = target * 100
        return str(result) + " cm"

    def celsius2fahrenheit(self, celsius: str):
        target = int(celsius)
        result = round(((target * 9 / 5) + 32), 2)
        return str(result) + " F"



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = DialogApplication()
    dialog.show()
    sys.exit(app.exec_())