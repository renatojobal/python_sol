import sys
from calculator import Ui_Dialog
from PyQt5 import QtWidgets, QtCore, uic
import operations


class DialogApplication(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        # Set up the dialog
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)

        # Setup buttons
        self.setup_buttons()


        # Present the dialog
        self.show()


    def setup_buttons(self):
        self.dialog.pushButton_0.clicked.connect(self.handle_0_clicked)
        self.dialog.pushButton_1.clicked.connect(self.handle_1_clicked)
        self.dialog.pushButton_2.clicked.connect(self.handle_2_clicked)
        self.dialog.pushButton_3.clicked.connect(self.handle_3_clicked)
        self.dialog.pushButton_4.clicked.connect(self.handle_4_clicked)
        self.dialog.pushButton_5.clicked.connect(self.handle_5_clicked)
        self.dialog.pushButton_6.clicked.connect(self.handle_6_clicked)
        self.dialog.pushButton_7.clicked.connect(self.handle_7_clicked)
        self.dialog.pushButton_8.clicked.connect(self.handle_8_clicked)
        self.dialog.pushButton_9.clicked.connect(self.handle_9_clicked)

        self.dialog.pushButton_plus.clicked.connect(self.handle_plus_clicked)
        self.dialog.pushButton_minus.clicked.connect(self.handle_minus_clicked)
        self.dialog.pushButton_multiplication.clicked.connect(self.handle_multiplication_clicked)
        self.dialog.pushButton_division.clicked.connect(self.handle_division_clicked)

        self.dialog.pushButton_delete.clicked.connect(self.handle_delete_clicked)
        self.dialog.pushButton_info.clicked.connect(self.handle_info_clicked)

        self.dialog.pushButton_equal.clicked.connect(self.handle_equal_clicked)



    def handle_equal_clicked(self):
        input_string = self.dialog.lineEditInput.text()
        self.calculate_result(input_string)
  

    def handle_delete_clicked(self):
        self.dialog.lineEditResult.setText('')
        self.dialog.lineEditInput.setText('')
        self.dialog.labelOperator.setText('')

    def handle_info_clicked(self):
        pass

    def handle_operator_clicked(self, operator: str):

        # Update the ui

        input_string = self.dialog.lineEditInput.text()

        if self.valid_input(input_string):

            # Udpate the labelOperator
            self.dialog.labelOperator.setText(operator)

            # Update the ui
            
            
            self.calculate_result(input_string)

                
        else:
            self.throw_error()



        # Clean the lineEditInput
        self.dialog.lineEditInput.setText('')

        print(operator)
        return

    def handle_number_clicked(self, number: int):

        # Update the ui
        previous_string = self.dialog.lineEditInput.text()
        self.dialog.lineEditInput.setText(previous_string+str(number))
    
        pass

    def handle_plus_clicked(self):
        self.handle_operator_clicked('+')

    def handle_minus_clicked(self):
        self.handle_operator_clicked('-')
    
    def handle_multiplication_clicked(self):
        self.handle_operator_clicked('*')

    def handle_division_clicked(self):
        self.handle_operator_clicked('/')

    def handle_0_clicked(self):
        self.handle_number_clicked(0)
    
    def handle_1_clicked(self):
        self.handle_number_clicked(1)

    def handle_2_clicked(self):
        self.handle_number_clicked(2)

    def handle_3_clicked(self):
        self.handle_number_clicked(3)

    def handle_4_clicked(self):
        self.handle_number_clicked(4)

    def handle_5_clicked(self):
        self.handle_number_clicked(5)

    def handle_6_clicked(self):
        self.handle_number_clicked(6)

    def handle_7_clicked(self):
        self.handle_number_clicked(7)

    def handle_8_clicked(self):
        self.handle_number_clicked(8)

    def handle_9_clicked(self):
        self.handle_number_clicked(9)


    def valid_input(self, input_string : str):
        try:
            int(input_string)
            return True
        except:
            return False


    def throw_error(self):
        """

        """
        self.dialog.lineEditResult.setText('')
        self.dialog.lineEditInput.setText('')
        self.dialog.labelOperator.setText('Syntx Error')
    
    def calculate_result(self, new_input: str):

        if self.dialog.lineEditResult.text() == '':
            self.dialog.lineEditResult.setText(new_input)

        else:
            cache_number = int(self.dialog.lineEditResult.text())
            target_operator = self.dialog.labelOperator.text()
            try:
                new_number = int(new_input)

                if target_operator == '+':
                    result = operations.addition(cache_number, new_number)            
                elif target_operator == '-':
                    result = operations.minus(cache_number, new_number)    
                elif target_operator == '*':
                    result = operations.multiplication(cache_number, new_number)    
                elif target_operator == '/':
                    if new_number == 0:
                        self.throw_error()
                    else:
                        result = operations.division(cache_number, new_number)

                self.dialog.lineEditInput.setText('')
                self.dialog.lineEditResult.setText(str(result))
            except:
                self.throw_error()

        

        


    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = DialogApplication()
    dialog.show()
    sys.exit(app.exec_())