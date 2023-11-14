# Password generator app
import PySimpleGUI as sg
import random
import string

def generate_password(pass_length):
    password_length = pass_length
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    window['password'].update(password)
    

layout = [
    [sg.Text('Password Length:'), sg.InputText(enable_events=True)],
    [sg.Button('Generate Password' ,key='Generate Password')],
    [sg.Text('Your Password:'), sg.InputText(key='password')]
]

window=sg.Window('Password Generator', layout,use_default_focus=False, finalize=True)
window.bind("<Return>", "Generate")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Generate Password' or event == 'Generate':
        generate_password(int(values[0]))
window.close()
