import PySimpleGUI as sg


menu = [
    ['文件(&F)',['新建','打开','保存','---','退出']],
    ['编辑(&E)',['撤销','重做','剪切','保存']],
    ['帮助(&H)',['检查更新','使用指南','关乎']]

]


layout = [
    [sg.Menu(menu)],
    [sg.FileBrowse(button_text="选择文件"), sg.In()],
    [sg.FileSaveAs(button_text="文件另存为"), sg.In()],
    [sg.Output(key='-YY-', size=(55, 25))],
    [sg.B('开始转换')]
]

sg.theme('LightGreen')

window = sg.Window('菜单栏设定', layout)
while True:
    event, values = window.read()
    if event == None:
        break

window.close()