import PySimpleGUI as sg


layoutL = [
    [sg.T('标题')],
    [sg.In('请输入文章标题')],
    [sg.T('作者')],
    [sg.In('请输入姓名或笔名')]
]

layoutR = [
    [sg.ML('请输入正文内容', size=(30, 20))],
    [sg.B('确认提交')]

]

layout = [
    [sg.Col(layoutL, pad=((10,35),(10,10))), sg.Col(layoutR)]
]

window = sg.Window('demo8', layout)
while True:
    event, values = window.read()
    if event == None:
        break


window.close()
