import tkinter as t
import math  # 수학 함수를 위한 라이브러리

window = None
display_label = None
expression = ''

# 계산 기록을 파일에 저장
def save_history(result):
    with open("calc_history.txt", "a") as file:
        file.write(result + "\n")

# 계산 기록을 불러와서 표시
def load_history():
    try:
        with open("calc_history.txt", "r") as file:
            history = file.readlines()
            history = [line.strip() for line in history]
            history_text = "\n".join(history[-5:])  # 최근 5개의 계산 기록만 표시
            display_label['text'] = history_text
    except FileNotFoundError:
        display_label['text'] = "No history found."

# 숫자 또는 연산자 버튼을 눌렀을 때 화면에 표시되는 함수
def press(num):
    global expression
    expression += str(num)
    display_label['text'] = expression

# 입력을 지우는 함수
def press_clear():
    global expression
    expression = ''
    display_label['text'] = '0'

# 결과를 계산하는 함수
def press_result():
    global expression
    try:
        # 수식의 계산
        result = str(eval(expression))
        display_label['text'] = result
        expression = result  # 결과가 나오면 결과를 새 수식으로 사용
        save_history(result)  # 계산 결과를 기록
    except:
        display_label['text'] = 'Error'

# 제곱 함수 (x^2)
def press_square():
    global expression
    try:
        value = float(expression)
        result = value ** 2
        display_label['text'] = str(result)
        expression = str(result)  # 결과로 업데이트
        save_history(str(result))  # 계산 결과를 기록
    except:
        display_label['text'] = 'Error'

# 제곱근 함수 (sqrt(x))
def press_sqrt():
    global expression
    try:
        value = float(expression)
        result = math.sqrt(value)  # 수학 모듈의 sqrt 함수 사용
        display_label['text'] = str(result)
        expression = str(result)  # 결과로 업데이트
        save_history(str(result))  # 계산 결과를 기록
    except:
        display_label['text'] = 'Error'

# 삼각 함수 (sin, cos, tan)
def press_sin():
    global expression
    try:
        value = float(expression)
        result = math.sin(math.radians(value))  # 각도를 라디안으로 변환 후 sin 계산
        display_label['text'] = str(result)
        expression = str(result)  # 결과로 업데이트
        save_history(str(result))  # 계산 결과를 기록
    except:
        display_label['text'] = 'Error'

def press_cos():
    global expression
    try:
        value = float(expression)
        result = math.cos(math.radians(value))  # 각도를 라디안으로 변환 후 cos 계산
        display_label['text'] = str(result)
        expression = str(result)  # 결과로 업데이트
        save_history(str(result))  # 계산 결과를 기록
    except:
        display_label['text'] = 'Error'

def press_tan():
    global expression
    try:
        value = float(expression)
        result = math.tan(math.radians(value))  # 각도를 라디안으로 변환 후 tan 계산
        display_label['text'] = str(result)
        expression = str(result)  # 결과로 업데이트
        save_history(str(result))  # 계산 결과를 기록
    except:
        display_label['text'] = 'Error'

def setup_GUI():
    global window
    global display_label

    window = t.Tk()
    window.title('My Advanced Calculator')

    display_label = t.Label(window, text='0', anchor='e', relief=t.SUNKEN, width=20, font='Arial 20')
    display_label.grid(row=0, columnspan=4)

    # 숫자 버튼들
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

    # 연산자 버튼들
    clear_btn = t.Button(window, text='C', width=5, height=2, font='Arial 15', command=press_clear)
    result_btn = t.Button(window, bg='green', text='=', width=5, height=2, font='Arial 15', command=press_result)
    add_btn = t.Button(window, text='+', width=5, height=2, font='Arial 15', command=lambda: press('+'))
    subtraction_btn = t.Button(window, text='-', width=5, height=2, font='Arial 15', command=lambda: press('-'))
    multiply_btn = t.Button(window, text='*', width=5, height=2, font='Arial 15', command=lambda: press('*'))
    divide_btn = t.Button(window, text='/', width=5, height=2, font='Arial 15', command=lambda: press('/'))

    # 함수 버튼들
    square_btn = t.Button(window, text='x²', width=5, height=2, font='Arial 15', command=press_square)
    sqrt_btn = t.Button(window, text='√', width=5, height=2, font='Arial 15', command=press_sqrt)
    sin_btn = t.Button(window, text='sin', width=5, height=2, font='Arial 15', command=press_sin)
    cos_btn = t.Button(window, text='cos', width=5, height=2, font='Arial 15', command=press_cos)
    tan_btn = t.Button(window, text='tan', width=5, height=2, font='Arial 15', command=press_tan)

    # 계산 기록 버튼
    load_history_btn = t.Button(window, text="History", width=5, height=2, font='Arial 15', command=load_history)

    # 배치
    btn1.grid(row=1, column=0, sticky='nsew')
    btn2.grid(row=1, column=1, sticky='nsew')
    btn3.grid(row=1, column=2, sticky='nsew')
    btn4.grid(row=2, column=0, sticky='nsew')
    btn5.grid(row=2, column=1, sticky='nsew')
    btn6.grid(row=2, column=2, sticky='nsew')
    btn7.grid(row=3, column=0, sticky='nsew')
    btn8.grid(row=3, column=1, sticky='nsew')
    btn9.grid(row=3, column=2, sticky='nsew')
    btn0.grid(row=4, column=1, sticky='nsew')

    clear_btn.grid(row=4, column=0, sticky='nsew')
    result_btn.grid(row=4, column=2, sticky='nsew')
    add_btn.grid(row=1, column=3, sticky='nsew')
    subtraction_btn.grid(row=2, column=3, sticky='nsew')
    multiply_btn.grid(row=3, column=3, sticky='nsew')
