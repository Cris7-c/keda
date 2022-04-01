import PySimpleGUI as sg

layout = [
    [sg.FileBrowse(button_text="选择文件"), sg.In()],
    [sg.FileSaveAs(button_text="文件另存为"), sg.In()],
    [sg.Output(key='-YY-', size=(55, 25))],
    [sg.B('开始转换')]
]

sg.theme('LightGreen')

window = sg.Window('峰哥专属语音转文本助手', layout)
while True:
    event, values = window.read()
    if event == None:
        break

window.close()
