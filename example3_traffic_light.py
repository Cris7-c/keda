from turtle import update
import PySimpleGUI as sg

layout = [
    [sg.B('绿灯', key='-green-', button_color=('black', 'green'), size=(30, 10))],
    [sg.B('黄灯', key='-yellow-', button_color=('black', 'yellow'), size=(30, 10))],
    [sg.B('红灯', key='-red-', button_color=('black', 'red'), size=(30, 10))]
]
window = sg.Window('红绿灯', layout)

while True:
    event, values = window.read()
    if event == None:
        break
    if event == '-green-':
        window['-green-'].update(button_color=('black', 'green'))
        window['-yellow-'].update(button_color=('black', 'grey'))
        window['-red-'].update(button_color=('black', 'grey'))
    if event == '-yellow-':
        window['-green-'].update(button_color=('black', 'grey'))
        window['-yellow-'].update(button_color=('black', 'yellow'))
        window['-red-'].update(button_color=('black', 'grey'))
    if event == '-red-':
        window['-green-'].update(button_color=('black', 'grey'))
        window['-yellow-'].update(button_color=('black', 'grey'))
        window['-red-'].update(button_color=('black', 'red'))
