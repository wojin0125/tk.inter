import tkinter as t
window = None
display_label = None
expression = ''

def press(num):
    global expression
    expression += str(num)
    display_label['text'] = expression

def press_clear():
    global expression
    expression = ''
    display_label['text'] = '0'

def press_result():
    global expression
    display_label['text'] = str(eval(expression))
    expression = ''

def setup_GUI():
    global window
    global display_label

    window = t.Tk()
    window.title('My Calc')
    display_label = t.Label(window, text='0', anchor='e', relief=t.SUNKEN, width=15, font='Arial 20')
    display_label.grid(row=0, columnspan=4)

    btn1 = t.Button(window, text='1', width=5, height=2, font='Arial 15', command=lambda: press(1))
    clear_btn = t.Button(window, text='C', width=5, height=2, font='Arial 15', command=press_clear)
    result_btn = t.Button(window,bg='green', text='=', width=5, height=2, font='Arial 15', command=press_result)
    add_btn = t.Button(window, text='+', width=5, height=2, font='Arial 15', command=lambda: press('+'))

    btn1.grid(row=1, column=0)
    clear_btn.grid(row=4, column=0)
    result_btn.grid(row=4, column=2)
    add_btn.grid(row=1, column=3)
    
setup_GUI()
