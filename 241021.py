import tkinter as tk

window = tk.Tk()
window.title("Login Form")

username_label = tk.Label(window, text="Username:", font ='Arial 12')
username_label.grid(row=0, column=0, padx=0, pady=10)

username_entry = tk.Entry(window, width=30)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(window, text="Password:", font ='Arial 12')
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(window, show="*", width=30)
password_entry.grid(row=1, column=0, padx=10, pady=10)

login_button = tk.Button(window, text="Login", width=10, font='Arial 12')
login_button.grid(row=2, column=1, padx=10, pady=10, sticky='e')

window.mainloop()
