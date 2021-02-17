import sys
from screen import *
import re

TEXT_CORRECT = 'Right! It is a vlid expression'
TEXT_INCORRECT = 'Incorrect! It is not a vlid expression'

pat = re.compile('''
\d+?                # one or more digits, taking as few as possible to match
\s?                 # one or zero space characters
\+                  # a literal plus sign
\s?                 # one or zero space characters
\(?                 # one or zero literal open parentheses
\s?                 # one or zero space characters
\d+?                # one or more digits, as before
''', re.X)

def is_valid_expression(target_expression: str):
    """
    Validate if is a valide expression
    :return: Boolean
    """
    pat.search(target_expression)
    try:
        eval(target_expression)
        return True
    except:
        return False


def calculate_result(expression):
    """
    Calcualte the result for the previous validate expression 
    :reutrn: str
    """
    return str(round(eval(expression), 2))

class DialogApplication(QtWidgets.QDialog):
    """
    Main class for interface
    """

    def __init__(self):
        super().__init__()

        # Set up the dialog
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)

        # Listener

        self.dialog.line_edit_expression.textChanged.connect(self.validate_expression)

        # Present the dialog
        self.show()

   
    def validate_expression(self):
        """
        Listener
        :return: None
        """
        # Get input expresseion
        target_expression = self.dialog.line_edit_expression.text()

        if is_valid_expression(target_expression):
            self.dialog.label_3.setText(TEXT_CORRECT)

            # Calculate result
            result = calculate_result(target_expression)

            self.dialog.line_edit_result.setText(result)
        else:
            self.dialog.label_3.setText(TEXT_INCORRECT)
            self.dialog.line_edit_result.setText('')
            


        print(target_expression)



if __name__ == '__main__':
    """
    Present the dialog application
    """

    app = QtWidgets.QApplication(sys.argv)
    dialog = DialogApplication()
    dialog.show()
    sys.exit(app.exec_())
