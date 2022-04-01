import PySimpleGUI as sg

layout = [
    [sg.Slider(key='-S-')],
    [sg.B('update')]
]

window = sg.Window('demo8', layout)
while True:
    event, values = window.read()
    if event == None:
        break
    if event == 'update':
        window['-S-'].update(
            value=None,
            range=(100, 500),
            disabled=None,
            visible=None

        )

window.close()
