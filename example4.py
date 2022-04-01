import PySimpleGUI as sg

dict = {'程序员1': 'python', '程序员2': 'java', '程序员3': 'c++', '程序员4': 'php'}
list = []
for i in dict:
    list.append(i)
    print(list)


layout = [
    [sg.LB(list, key='-LB-', size=(30, 6), enable_events=True)],
    [sg.T('语言'), sg.In(key='-YY-',size=(26))]
]

window = sg.Window('demo4', layout)
while True:
    event, values = window.read()
    if event == None:
        break
    if event == '-LB-':
        window['-YY-'].update(dict[values['-LB-'][0]])

window.close()
