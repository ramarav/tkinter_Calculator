import tkinter as tk
class Calc(object):
    def __init__(self, parent=tk.Tk()):
        self.parent = parent
        self.parent.title("Python - Calculadora")
        self.parent.option_add("*Font", "Verdana 12 normal")
        # control variable, used in key_press method

        self.decimal_point_open = False
# variable containing the expression ready for calculation
        self.math_expression = None
        #menubar
        menu_bar = tk.Menu(self.parent)
        menu_bar.add_command(label="About", command=self.about)
        self.parent.config(menu=menu_bar)
# display elements
        self.display_stringvar = tk.StringVar()
        display_entry_validate = (self.parent.register(self.only_number_entry), '%S','%d')
        self.display = tk.Entry(self.parent, font=("Verdana", 20, "normal"), validate="key",validatecommand=display_entry_validate, textvariable=self.display_stringvar)
        self.display.bind('<Return>', self.calc_expression)
#===================================================================================================================================
# number keypad creation
        self.bt0 = tk.Button(self.parent, text="0", command=lambda: self.button_press('0'))
        self.bt1 = tk.Button(self.parent, text="1", command=lambda: self.button_press('1'))
        self.bt2 = tk.Button(self.parent, text="2", command=lambda: self.button_press('2'))
        self.bt3 = tk.Button(self.parent, text="3", command=lambda: self.button_press('3'))
        self.bt4 = tk.Button(self.parent, text="4", command=lambda: self.button_press('4'))
        self.bt5 = tk.Button(self.parent, text="5", command=lambda: self.button_press('5'))
        self.bt6 = tk.Button(self.parent, text="6", command=lambda: self.button_press('6'))
        self.bt7 = tk.Button(self.parent, text="7", command=lambda: self.button_press('7'))
        self.bt8 = tk.Button(self.parent, text="8", command=lambda: self.button_press('8'))
        self.bt9 = tk.Button(self.parent, text="9", command=lambda: self.button_press('9'))
        self.bt_plus = tk.Button(self.parent, text="+", command=lambda: self.button_press('+'))
        self.bt_sub = tk.Button(self.parent, text="-", command=lambda: self.button_press('-'))
        self.bt_multi = tk.Button(self.parent, text="*", command=lambda: self.button_press('*'))
        self.bt_divide = tk.Button(self.parent, text="/", command=lambda: self.button_press('/'))
        self.bt_point = tk.Button(self.parent, text=".", command=lambda: self.button_press('.'))
        self.bt_equal = tk.Button(self.parent, text="=", command=lambda: self.button_press('='))
        self.bt_clear = tk.Button(self.parent, text="To clean", command=self.clear)
        self.bt_quit = tk.Button(self.parent, text="(Esc)",command=lambda:self.parent.destroy())
        self.parent.bind("<Escape>",lambda event=None:self.parent.destroy())
        self.mount_gui()
        self.parent.mainloop()
#=====================================================================================================================================

#mounts and configures graphics components
    def mount_gui(self):
        self.display.grid(row=0, column=0, columnspan=4, sticky="ewns", ipady=5, padx=2, pady=2)
        self.bt0.grid(row=4, column=0, sticky="ewns", padx=2, pady=2)
        self.bt1.grid(row=3, column=0, sticky="ewns", padx=2, pady=2)
        self.bt2.grid(row=3, column=1, sticky="ewns", padx=2, pady=2)
        self.bt3.grid(row=3, column=2, sticky="ewns", padx=2, pady=2)
        self.bt4.grid(row=2, column=0, sticky="ewns", padx=2, pady=2)
        self.bt5.grid(row=2, column=1, sticky="ewns", padx=2, pady=2)
        self.bt6.grid(row=2, column=2, sticky="ewns", padx=2, pady=2)
        self.bt7.grid(row=1, column=0, sticky="ewns", padx=2, pady=2)
        self.bt8.grid(row=1, column=1, sticky="ewns", padx=2, pady=2)
        self.bt9.grid(row=1, column=2, sticky="ewns", padx=2, pady=2)
        self.bt_plus.grid(row=3, column=3, sticky="ewns", padx=2, pady=2)
        self.bt_sub.grid(row=2, column=3, sticky="ewns", padx=2, pady=2)
        self.bt_divide.grid(row=4, column=3, sticky="ewns", padx=2, pady=2)
        self.bt_multi.grid(row=1, column=3, sticky="ewns", padx=2, pady=2)
        self.bt_point.grid(row=4, column=1, sticky="ewns", padx=2, pady=2)
        self.bt_equal.grid(row=4, column=2, sticky="ewns", padx=2, pady=2)
        self.bt_clear.grid(row=5,column=0,columnspan=2, sticky="ewns", padx=2, pady=2)
        self.bt_quit.grid(row=5,column=2,columnspan=2,sticky="ewns",padx=2,pady=2)
#=====================================================================================================================================

#clear the display
    def clear(self):
        self.display_stringvar.set("")
        self.decimal_point_open = False
#======================================================================================================================================

#rest on
    def about(self):
        about_window = tk.Toplevel(self.parent)
        about_window.title("Python - About")
        tk.Label(about_window, text="Python",font=("Verdana",15,"bold")).grid(row=0,column=0,padx=5,pady=5,sticky="s")
        tk.Label(about_window, text="Simple Calculator").grid(row=1,column=0, padx=5, pady=5,sticky="s")
        tk.Label(about_window, text="Developed in Python 3 and Tkinter").grid(row=2, column=0, sticky="s", padx=5)
        tk.Label(about_window, text="ifo@gmail.com").grid(row=3,column=0,sticky="s",padx=5)
#=======================================================================================================================================

#validator of entrys only valid mathematical expressions
    def only_number_entry(self, key_press, cod):
        valid_chars = "0123456789.+-*/"
        expression_now = self.display_stringvar.get() 
        num_chars_now = len(expression_now)
#in the beginning of the expression, accept only numbers
        if( num_chars_now == 0 ):
            valid_chars_for_init = "0123456789"
            return key_press in valid_chars_for_init        
        else:
            last_char = expression_now[num_chars_now-1]
# if the last inserted element is an operator only accepts numbers or backspace
            if(last_char in "+-*/" and key_press in "+-*/." and cod=='1'):
                return False
#control the use of decimal point
#avoid two consecutive operators    
            elif(last_char in "+-*/" and key_press in "+-*/." and cod=='0'):
                return True
            elif(last_char == '.' and key_press in "+-*/." and cod=='1'):
                return False
            elif(last_char == '.' and key_press in "+-*/." and cod=='0'):
                return True
            elif(self.decimal_point_open and key_press=='.'):
                return False
            elif(not self.decimal_point_open and key_press=='.'):
                self.decimal_point_open = True
                return True
            elif(last_char in "0123456789" and key_press in "+-*/"):
                self.decimal_point_open = False
                return True
#======================================================================================================================================        
# interface button pressed
    def button_press(self, bt):
        expresion_now = self.display_stringvar.get()
        char_num = len(expresion_now)
#define valid characters for the beginning of the expression
        if(char_num==0):
            valid_chars_for_init = "0123456789"
            if(bt in valid_chars_for_init):
                expresion_now+=bt
                self.display_stringvar.set(expresion_now)
        else:
# decimal point usage control
            last_char = expresion_now[char_num - 1]
            if(bt=='.' and not last_char in "+-*/"):
                if(self.decimal_point_open):
                    print("decimal point unavailable")
                else:
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
                    self.decimal_point_open = True
            else:
                if(last_char in ".0123456789" and bt in "0123456789"):
                    expresion_now+=bt
                    self.display_stringvar.set(expresion_now)
                elif(last_char in "0123456789" and not self.decimal_point_open and bt in "+-*/"):
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
                elif(self.decimal_point_open and not last_char=='.' and bt in "+-*/"):
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
                    self.decimal_point_open = False
# operator control
                elif(last_char in "+-*/" and bt in "0123456789"):
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
# button = pressed, get result
                elif(bt=='=' and last_char in "0123456789"):
#=====================================================================================================================================
#calculates the expression
                    self.calc_expression()

    def prepare_expression(self):
        elementos = []
        index = 0
        for char in self.display_stringvar.get():
# start the list with the first number
            if(len(elementos)==0 and char in "0123456789"):
                elementos.append(char)
#new operator as new list member
            elif(len(elementos)>0 and char in "+-*/"):
                elementos.append(char)
                index+=1
            elif(elementos[index] in "+-*/"):
                    elementos.append(char)
                    index+=1
            else:
                elementos[index]+=char
#serves the prepared expression as object attribute
        self.math_expression = elementos
   
#define the expression calculation
    def calc_expression(self, event=None):
        self.prepare_expression()
# multiplication and division, precedence: whichever comes first from left to right
        while ("*" in self.math_expression or "/" in self.math_expression):
            index = 0
            for element in self.math_expression:
                if (element == '*'):
                    v1 = float(self.math_expression[index - 1])
                    v2 = float(self.math_expression[index + 1])
                    result = str(v1 * v2)
                    self.math_expression[index] = result
                    self.math_expression.pop(index + 1)
                    self.math_expression.pop(index - 1)
                    index += 1
                    break
                elif (element == '/'):
                    v1 = float(self.math_expression[index - 1])
                    v2 = float(self.math_expression[index + 1])
                    result = str(v1 / v2)
                    self.math_expression[index] = result
                    self.math_expression.pop(index + 1)
                    self.math_expression.pop(index - 1)
                    index += 1
                    break
                else:
                    index += 1
# addition and subtraction
# Repeat until just about the result
        while (len(self.math_expression) > 1):
            index = 0
            for element in self.math_expression:
                if (element == '+'):
                    v1 = float(self.math_expression[index - 1])
                    v2 = float(self.math_expression[index + 1])
                    result = str(v1 + v2)
                    self.math_expression[index] = result
                    self.math_expression.pop(index + 1)
                    self.math_expression.pop(index - 1)
                    index += 1
                    break
                if (element == '-'):
                    v1 = float(self.math_expression[index - 1])
                    v2 = float(self.math_expression[index + 1])
                    result = str(v1 - v2)
                    self.math_expression[index] = result
                    self.math_expression.pop(index + 1)
                    self.math_expression.pop(index - 1)
                    index += 1
                    break
                else:
                    index += 1
        final_result = str( round( float(self.math_expression[0]), 1 ) )
#include the result in the display
        self.display_stringvar.set(final_result)

if (__name__ == "__main__"):
    calc = Calc()
