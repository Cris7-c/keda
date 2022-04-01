import PySimpleGUI as sg

layout = [
    [sg.Button('中文'), sg.Button('English')],
    [sg.Text('请输入基本信息！', key='-INFO-')],
    [sg.Text('姓名', key='-name-', size=(8, 1)), sg.InputText('')],
    [sg.Text('性别', key='-sex-', size=(8, 1)), sg.InputText('')],
    [sg.Text('国籍', key='-nation-', size=(8, 1)), sg.InputText('')],
    [sg.Button('确定', key='-confirm-', size=(8, 1)),
     sg.Button('取消', key='-cancle-', size=(8, 1))]
]

window = sg.Window('Python GUI', layout)

while True:
    event, values = window.read()
    if event == None:
        break
    if event == 'English':
        window['-INFO-'].update('Please enter basic information!')
        window['-name-'].update('Name')
        window['-sex-'].update('Sex')
        window['-nation-'].update('Nationality')
        window['-confirm-'].update('Confirm')
        window['-cancle-'].update('Cancle')
    if event == '中文':
        window['-INFO-'].update('请输入基本信息！')
        window['-name-'].update('姓名')
        window['-sex-'].update('性别')
        window['-nation-'].update('国籍')
        window['-confirm-'].update('确定')
        window['-cancle-'].update('取消')

window.close()

