import PySimpleGUI as sg

a = ['python', 'java', 'c++', 'php', 'c++']


layout = [
    [sg.T('OptionMenu'), sg.OptionMenu(list(range(10)), key='-OM-'),
     sg.T('Spin'), sg.Spin(list(range(10)), key='-SP-', enable_events=True)],
    [sg.T('语言'), sg.In(key='-YY-', size=(25))]
]

window = sg.Window('demo6', layout)
while True:
    event, values = window.read()
    if event == None:
        break
    if event == '-SP-':
        window['-YY-'].update(values['-SP-'])

window.close()
