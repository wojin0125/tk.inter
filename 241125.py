import tkinter as t
window = None
display_label = None
expression = ''

def press(num):
    global expression
    if display_label['text'] == '0':  # 화면에 '0'이 있으면 새로운 계산 시작
        expression = str(num)
    else:
        expression += str(num)
    display_label['text'] = expression

def press_clear():
    global expression
    expression = ''
    display_label['text'] = '0'

def press_result():
    global expression
    try:
        result = str(eval(expression))
        display_label['text'] = result
        expression = result  # 결과를 expression에 저장하여 이어서 계산할 수 있게 함
    except Exception as e:
        display_label['text'] = 'Error'  # 오류가 발생한 경우 'Error' 표시
        expression = ''  # 오류가 발생하면 입력값을 초기화

def setup_GUI():
    global window
    global display_label

    window = t.Tk()
    window.title('My Calc')
    display_label = t.Label(window, text='0', anchor='e', relief=t.SUNKEN, width=15, font='Arial 20')
    display_label.grid(row=0, columnspan=4)

    btn1 = t.Button(window, text='1', width=5, height=2, font='Arial 15', command=lambda: press(1))
    btn2 = t.Button(window, text='2', width=5, height=2, font='Arial 15', command=lambda: press(2))
    btn3 = t.Button(window, text='3', width=5, height=2, font='Arial 15', command=lambda: press(3))
    btn4 = t.Button(window, text='4', width=5, height=2, font='Arial 15', command=lambda: press(4))
    btn5 = t.Button(window, text='5', width=5, height=2, font='Arial 15', command=lambda: press(5))
    btn6 = t.Button(window, text='6', width=5, height=2, font='Arial 15', command=lambda: press(6))
    btn7 = t.Button(window, text='7', width=5, height=2, font='Arial 15', command=lambda: press(7))
    btn8 = t.Button(window, text='8', width=5, height=2, font='Arial 15', command=lambda: press(8))
    btn9 = t.Button(window, text='9', width=5, height=2, font='Arial 15', command=lambda: press(9))
    btn0 = t.Button(window, text='0', width=5, height=2, font='Arial 15', command=lambda: press(0))
    clear_btn = t.Button(window, text='C', width=5, height=2, font='Arial 15', command=press_clear)
    result_btn = t.Button(window,bg='green', text='=', width=5, height=2, font='Arial 15', command=press_result)
    add_btn = t.Button(window, text='+', width=5, height=2, font='Arial 15', command=lambda: press('+'))
    subtraction_btn = t.Button(window, text='-', width=5, height=2, font='Arial 15', command=lambda: press('-'))
    multiply_btn = t.Button(window, text='*', width=5, height=2, font='Arial 15', command=lambda: press('*'))
    divide_btn = t.Button(window, text='/', width=5, height=2, font='Arial 15', command=lambda: press('/'))

    btn1.grid(row=1, column=0)
    btn2.grid(row=1, column=1)
    btn3.grid(row=1, column=2)
    btn4.grid(row=2, column=0)
    btn5.grid(row=2, column=1)
    btn6.grid(row=2, column=2)
    btn7.grid(row=3, column=0)
    btn8.grid(row=3, column=1)
    btn9.grid(row=3, column=2)
    btn0.grid(row=4, column=1)
    clear_btn.grid(row=4, column=0)
    result_btn.grid(row=4, column=2)
    add_btn.grid(row=1, column=3)
    subtraction_btn.grid(row=2, column=3)
    multiply_btn.grid(row=3, column=3)
    divide_btn.grid(row=4, column=3)

setup_GUI()
window.mainloop()
