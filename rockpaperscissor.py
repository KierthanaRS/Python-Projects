import random
import PySimpleGUI as sg

sg.theme('DarkBlue3')
rock_image = 'rock.png'  
paper_image = 'paper.png'  
scissors_image = 'scissors.png'  
result_image = 'result.png'
layout = [[sg.Text('Choose your weapon:')],
          [sg.Button(image_filename=rock_image, image_size=(100, 100), key='Rock'),
           sg.Button(image_filename=paper_image, image_size=(100, 100), key='Paper'),
           sg.Button(image_filename=scissors_image, image_size=(100, 100), key='Scissors')],
          [sg.Text('Computer choise:'),sg.Image(key='-IMAGE-')],
          [sg.Text(size=(40,3), key='-OUTPUT-')],
          [sg.Button('Quit')]]

window = sg.Window('Rock Paper Scissors', layout)
score_u = 0
score_c = 0
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        sg.popup('Thanks for playing!')
        break
    # if event == 'Rock':
    #     user_choice_image = rock_image
    # elif event == 'Paper':
    #     user_choice_image = paper_image
    # else:
    #     user_choice_image = scissors_image
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    computer_choice_image = {
    'Rock': rock_image,
    'Paper': paper_image,
    'Scissors': scissors_image
}.get(computer_choice, result_image)
    if event == 'Rock':
        if computer_choice == 'Rock':
            result = 'Tie!'
        elif computer_choice == 'Paper':
            result = 'You lose!'
            score_c += 1
        else:
            result = 'You win!'
            score_u += 1
    elif event == 'Paper':
        if computer_choice == 'Rock':
            result = 'You win!'
            score_u += 1
        elif computer_choice == 'Paper':
            result = 'Tie!'
        else:
            result = 'You lose!'
            score_c += 1
    else:
        if computer_choice == 'Rock':
            result = 'You lose!'
            score_c+=1
        elif computer_choice == 'Paper':
            result = 'You win!'
            score_u += 1
        else:
            result = 'Tie!'
    window['-IMAGE-'].update(filename=computer_choice_image)
    window['-OUTPUT-'].update(f'{result}\nYour score: {score_u}\n Computer score: {score_c}')

window.close()
