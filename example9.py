import PySimpleGUI as sg


layouta = [
    [sg.T('账号'),sg.In('')],
    [sg.T('密码'),sg.In('')]
]
layout = [
    [sg.Frame(title='登录框',layout=layouta)]
]

window = sg.Window('demo9', layout)
while True:
    event, values = window.read()
    if event == None:
        break


window.close()
