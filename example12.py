import PySimpleGUI as sg

layout = [
    [sg.FileBrowse(),sg.In()]
    
]

window = sg.Window('文件选择器', layout)
while True:
    event, values = window.read()
    if event == None:
        break

window.close()
