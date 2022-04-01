import PySimpleGUI as sg

listb = ['非常满意','满意','一般','不满意']
lista = ['对邹凌的指导做出评价：', '对毕卉的指导做出评价：']

# 从左到右的单选框
""" layout = [
    [sg.T('1.'+lista[0])],
    [sg.R(i, group_id=1) for i in listb],
    [sg.T('2.'+lista[1])],
    [sg.R(i, group_id=2) for i in listb]
] """

""" # 从上到下的单选框
layout = [
    [[sg.R(i, group_id=1)] for i in listb]
]
 """
# 巧用 key=(x,y), for循环快速定义单选框
# 从左到右、从上到下同时遍历
layout = [[sg.T(str(y+1))]+[sg.R(x,group_id=y,key=(x,y))for x in listb]for y in range(9)]

window = sg.Window('demo7', layout)
while True:
    event, values = window.read()
    if event == None:
        break
    if event == '-SP-':
        window['-YY-'].update(values['-SP-'])

window.close()
