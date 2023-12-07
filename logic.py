from PyQt6.QtWidgets import *
from gui import *
from formulas import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ADD.setChecked(True)
        
        self.RESPONSE.setText('''Conditions \n1)Please do not seperate using commas. Use Spaces. \n2)You need two or more values\n3)Do not use characters. Valid types include ints and floats.\nOperators Guide:\nAdd: Add positive numbers only.\nSubtract: Add negative numbers only.\nMultiply: Multiply either positive or negative values. \nDivide: Divide either positive  or negative values. \nChoose: Randomly picks between entered values.''')    
                
                
        self.SUBMIT.clicked.connect(lambda: self.submit())
        self.CLEAR.clicked.connect(lambda: self.clear())
    def submit(self):
        invalid = False
        value_set = list(self.VALUES.text().split())
        print(value_set)
        for value in value_set:
            try:
                float(value)
            except ValueError:
                if ',' in value:
                    invalid = True
                    self.RESPONSE.setText('Please do not seperate using commas.\nUse spaces.\nExample: 1 2 3 ')
                else:
                    invalid = True
                    self.RESPONSE.setText('Avoid using characters.\nValid types include ints and floats.\nSeperate using spaces not commas.')
        if len(value_set) < 2:
            invalid = True
            self.RESPONSE.setText('You need two or more values. Please do not seperate using commas.\nUse spaces.\nExample: 1 2 3 ')
        if invalid == False:
            if self.ADD.isChecked():
                self.RESPONSE.setText(f"Answer = {add(value_set):.2f}")
            elif self.SUBTRACT.isChecked():
                self.RESPONSE.setText(f"Answer = {subtract(value_set):.2f}")
            elif self.MULTIPLY.isChecked():
                self.RESPONSE.setText(f"Answer = {multiply(value_set):.2f}")
            elif self.DIVIDE.isChecked():
                self.RESPONSE.setText(f"Answer = {divide(value_set):.2f}")
            elif self.CHOOSE.isChecked():
                self.RESPONSE.setText(f"Answer = {choose(value_set):.2f}")

    def clear(self): 
        self.VALUES.setText('')
        #self.ADD.setChecked(True)
        self.RESPONSE.setText('''Conditions \n1)Please do not seperate using commas. Use Spaces. \n2)You need two or more values\n3)Do not use characters. Valid types include ints and floats.\nOperators Guide:\nAdd: Add positive numbers only.\nSubtract: Add negative numbers only.\nMultiply: Multiply either positive or negative values. \nDivide: Divide either positive  or negative values. \nChoose: Randomly picks between entered values.''') 
 
