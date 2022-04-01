import PySimpleGUI as sg


list = ['资料1', '资料2', '资料3', '资料4']

layoutb = [
    [sg.LB(list, size=(30, 5))]
]

layouta = [
    [sg.T('账号'), sg.In('')],
    [sg.T('密码'), sg.In('')],
    [sg.B('确定'), sg.B('取消')]
]
layout = [
    [sg.Frame(title='登录框', layout=layouta, key='-a-'),
     sg.Frame(title='资料列表', layout=layoutb, visible=False, key='-b-')]
]

window = sg.Window('demo9', layout)
while True:
    event, values = window.read()
    if event == None:
        break
    if event == '确定':
        window['-a-'].Update(visible=False)
        window['-b-'].Update(visible=True)


window.close()
