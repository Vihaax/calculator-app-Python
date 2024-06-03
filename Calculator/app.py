from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='#D4D4D2')
        master.resizable(False, False)
        
        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=24, bg='#1C1C1C', fg='white', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)
        
        # Define common button parameters
        button_params = {'width': 11, 'height': 4, 'relief': 'flat', 'bg': 'gray', 'fg': 'white', 'font': ('Arial', 12, 'bold')}
        operator_params = {'width': 11, 'height': 4, 'relief': 'flat', 'bg': '#FF9500', 'fg': 'white', 'font': ('Arial', 12, 'bold')}
        other_params = {'width': 11, 'height': 4, 'relief': 'flat', 'bg': '#505050', 'fg': 'white', 'font': ('Arial', 12, 'bold')}
        
        # Add buttons with updated parameters
        Button(**other_params, text='(', command=lambda: self.show('(')).place(x=0, y=50)
        Button(**other_params, text=')', command=lambda: self.show(')')).place(x=90, y=50)
        Button(**other_params, text='%', command=lambda: self.show('%')).place(x=180, y=50)
        Button(**button_params, text='1', command=lambda: self.show(1)).place(x=0, y=125)
        Button(**button_params, text='2', command=lambda: self.show(2)).place(x=90, y=125)
        Button(**button_params, text='3', command=lambda: self.show(3)).place(x=180, y=125)
        Button(**button_params, text='4', command=lambda: self.show(4)).place(x=0, y=200)
        Button(**button_params, text='5', command=lambda: self.show(5)).place(x=90, y=200)
        Button(**button_params, text='6', command=lambda: self.show(6)).place(x=180, y=200)
        Button(**button_params, text='7', command=lambda: self.show(7)).place(x=0, y=275)
        Button(**button_params, text='8', command=lambda: self.show(8)).place(x=90, y=275)
        Button(**button_params, text='9', command=lambda: self.show(9)).place(x=180, y=275)
        Button(**button_params, text='0', command=lambda: self.show(0)).place(x=90, y=350)
        Button(**button_params, text='.', command=lambda: self.show('.')).place(x=180, y=350)
        Button(**operator_params, text='+', command=lambda: self.show('+')).place(x=270, y=275)
        Button(**operator_params, text='-', command=lambda: self.show('-')).place(x=270, y=200)
        Button(**operator_params, text='/', command=lambda: self.show('/')).place(x=270, y=50)
        Button(**operator_params, text='*', command=lambda: self.show('*')).place(x=270, y=125)
        Button(**operator_params, text='=', command=self.solve).place(x=270, y=350)
        Button(**other_params, text='AC', command=self.clear).place(x=0, y=350)
        
    def show(self, value):   
        self.entry_value += str(value)
        self.equation.set(self.entry_value)
         
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)
         
    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set('Error')
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()
