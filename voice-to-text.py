import PySimpleGUI as sg


layout = [
    [sg.T('输入你的key： '), sg.In(key='-YY-', size=(25))],
    [sg.T('选择文件路径：'), sg.In(key='-YY-', size=(25)), sg.FileBrowse()],
    [sg.R('保存文件   ', group_id=1), sg.In(key='-YY-', size=(25)), sg.FileBrowse()],
    [sg.Output(key='-YY-', size=(50, 20))]

]

window = sg.Window('峰哥专属语音转文本助手', layout)
while True:
    event, values = window.read()
    if event == None:
        break
    if event == '-LB-':
        window['-YY-'].update(dict[values['-LB-'][0]])

window.close()
