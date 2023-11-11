import PySimpleGUI as sg

layout = [
    [sg.Text('To-Do List')],
    [sg.InputText(key='input',enable_events=True), sg.Button('Add',key='Add')],
    [sg.Listbox(values=[], size=(40, 10), key='items')],
    [sg.Button('Delete',key='Delete'), sg.Button('Clear',key='Clear')]
]
sg.theme('TealMono')

window = sg.Window('To-Do List', layout, use_default_focus=False, finalize=True)
window.bind("<Return>", "button")
window.bind("<BackSpace>", "delete")
window.bind("<Delete>", "clear")
window.bind("<Escape>", "Exit")

items = []


while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Add' or event == 'button':
        item = values['input']
        if item:
            items.append(item)
            window['items'].update(items)
            window['Add'].update(disabled=False)
            window['input'].update('')
    elif event == 'Delete' or event == 'delete':
        last_item = items[-1]
        if last_item:
            items.pop()
        window['items'].update(items)
    elif event == 'Clear' or event == 'clear':
        items.clear()
        window['items'].update(items)
    elif event == 'Exit':
        break
    elif event == 'items':
        window['Add'].update(disabled=False)

# Close the window
window.close()