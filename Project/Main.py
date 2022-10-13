from optparse import Option
from tkinter import *
from turtle import bgcolor

#Fonts
SMALL_FONT_STYLE = ('Arial', 16)
LARGE_FONT_STYLE = ('Arial', 40, 'bold')
DIGITS_FONT_STYLE = ('Arial', 24, 'bold')
OPERATORS_FONT_STYLE = ('Arial', 20)

#Colors
WHITE = '#FFFFFF'
OFF_WHITE = '#F8FAFF'
LABEL_COLOR = '#25265E'
LIGHT_GRAY = '#F5F5F5'
LIGHT_BLUE = '#CCDEFF'


class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('375x667')
        self.window.config(bg='#1c1c1c')
        self.window.resizable(0,0)
        self.window.title('Made by @manoelteofilo3')
        self.window.iconbitmap('Sabugao.ico')

        self.totalexp = ""
        self.currentexp = ""

        self.displayf = self.create_display_frame()
        self.buttonsf = self.create_buttons_frame()

        self.total_label, self.label = self.create_labels()

        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), '.':(4,1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}    

        self.buttonsf.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttonsf.rowconfigure(x, weight=1)
            self.buttonsf.columnconfigure(x, weight=1)

        self.create_digits(WHITE, '#cfcfcf')
        self.create_operators(OFF_WHITE, '#cfcfcf')
        self.create_Clear(OFF_WHITE, '#cfcfcf')
        self.create_equals(LIGHT_BLUE, '#cfcfcf')
        self.create_square(OFF_WHITE, '#cfcfcf')
        self.create_sqrt(OFF_WHITE, '#cfcfcf')

        self.themes = [
            'White',
            'Black'
        ]
        self.valueinside = StringVar(self.window)
        self.valueinside.set("White")
        self.theme = self.create_Choose(WHITE)
    
    #Beuty
    def create_digits(self, color, ac):
        for digit, grid_value in self.digits.items():
            button = Button(self.buttonsf, text=str(digit), bg=color, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=lambda x = digit: self.add_to_exp(x), activebackground=ac)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)

    def create_operators(self, color, ac):
        i = 0
        for operator, symbol in self.operations.items():
            button = Button(self.buttonsf, text = symbol, bg=color, fg=LABEL_COLOR, font=OPERATORS_FONT_STYLE, borderwidth=0, command= lambda x=operator: self.append_opertation(x), activebackground=ac)
            button.grid(row=i, column=4, sticky=NSEW)
            i += 1

    def create_Clear(self, color, ac):
        button = Button(self.buttonsf, text = 'C', bg=color, fg=LABEL_COLOR, font=OPERATORS_FONT_STYLE, borderwidth=0, command= self.clear, activebackground=ac)
        button.grid(row=0, column=1, columnspan=1, sticky=NSEW)

    def create_equals(self, color, ac):
        button = Button(self.buttonsf, text = "=", bg=color, fg=LABEL_COLOR, font=OPERATORS_FONT_STYLE, borderwidth=0, command= self.evaluate, activebackground=ac)
        button.grid(row=4, column=3, columnspan=2,sticky=NSEW)

    def create_square(self, color, ac):
        button = Button(self.buttonsf, text = 'x\u00b2', bg=color, fg=LABEL_COLOR, font=OPERATORS_FONT_STYLE, borderwidth=0, command= self.square, activebackground=ac)
        button.grid(row=0, column=2, columnspan=1, sticky=NSEW)
    
    def create_sqrt(self, color, ac):
        button = Button(self.buttonsf, text = '\u221ax', bg=color, fg=LABEL_COLOR, font=OPERATORS_FONT_STYLE, borderwidth=0, command= self.sqrt, activebackground=ac)
        button.grid(row=0, column=3, columnspan=1, sticky=NSEW)

    def create_labels(self):
        total_label = Label(self.displayf, text=self.totalexp, anchor=E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font= SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = Label(self.displayf, text=self.currentexp, anchor=E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font= LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label   

    def create_display_frame(self):
        frame = Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill='both')
        return frame
    
    def create_buttons_frame(self):
        frame = Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame

    #Theme Methods
    def create_Choose(self, color):
        dropbox = OptionMenu(self.displayf, self.valueinside, *self.themes, command=lambda theme=self.valueinside.get(): self.Change_Theme(theme))
        dropbox.config(bg=WHITE, fg=LABEL_COLOR, borderwidth=0, highlightthickness=0)
        dropbox["menu"].config(bg=color)
        dropbox.pack(anchor=NW)

        return dropbox

    def Change_Theme(self, theme):
        if theme == 'White':
            print()
            WHITE = '#FFFFFF'
            OFF_WHITE = '#F8FAFF'
            LIGHT_BLUE = '#CCDEFF'
            self.displayf.config(bg='#F5F5F5')
            self.total_label.config(bg='#F5F5F5')
            self.label.config(bg='#F5F5F5')

            self.buttonsf.destroy()
            self.buttonsf = self.create_buttons_frame()
            self.buttonsf.rowconfigure(0, weight=1)
            for x in range(1,5):
                self.buttonsf.rowconfigure(x, weight=1)
                self.buttonsf.columnconfigure(x, weight=1)

            self.create_digits(WHITE, '#cfcfcf')
            self.create_operators(OFF_WHITE, '#cfcfcf')
            self.create_Clear(OFF_WHITE, '#cfcfcf')
            self.create_equals(LIGHT_BLUE, '#cfcfcf')
            self.create_square(OFF_WHITE, '#cfcfcf')
            self.create_sqrt(OFF_WHITE, '#cfcfcf')

            self.theme.config(bg=WHITE)

        if theme == 'Black':
            print()
            WHITE = '#212121'
            OFF_WHITE = '#242424'
            LIGHT_BLUE = '#1c1c1c'
            self.displayf.config(bg='#1c1c1c')
            self.total_label.config(bg='#1c1c1c')
            self.label.config(bg='#1c1c1c')

            self.buttonsf.destroy()
            self.buttonsf = self.create_buttons_frame()
            self.buttonsf.rowconfigure(0, weight=1)
            for x in range(1,5):
                self.buttonsf.rowconfigure(x, weight=1)
                self.buttonsf.columnconfigure(x, weight=1)
            
            self.create_digits(WHITE, '#171717')
            self.create_operators(OFF_WHITE, '#171717')
            self.create_Clear(OFF_WHITE,'#171717')
            self.create_equals(LIGHT_BLUE, '#171717')
            self.create_square(OFF_WHITE, '#171717')
            self.create_sqrt(OFF_WHITE, '#171717')

            self.theme.config(bg=WHITE)

    #Function methods
    def update_total(self):
        expression = self.totalexp
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f'{symbol}')
        self.total_label.config(text=expression[:10])

    def update_sub(self):
        self.label.config(text=self.currentexp[:10])

    def add_to_exp(self, value):
            self.currentexp += str(value)
            self.update_sub()

    def append_opertation(self, operator):
        self.currentexp += " " + operator + " "
        self.totalexp += self.currentexp
        self.currentexp = ""
        self.update_sub()
        self.update_total()
    
    def clear(self):
        self.currentexp = ""
        self.totalexp = ""
        self.update_sub()
        self.update_total()

    def evaluate(self):
        self.totalexp += self.currentexp
        self.update_total()

        try:
            self.currentexp = str(eval(self.totalexp))
            self.totalexp = ""
        except Exception as e:
            self.currentexp = "fuck you"
        finally:
            self.update_sub()

    def square(self):
        self.currentexp = str(eval(f"{self.currentexp}**2"))
        self.update_sub()

    def sqrt(self):
        self.currentexp = str(eval(f"{self.currentexp}**0.5"))
        self.update_sub()

    #Run Method
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()