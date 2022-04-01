import PySimpleGUI as sg


lista = ['资料1', '资料2', '资料3', '资料4']
listb = ['程序员1', '程序员2', '程序员3', '程序员4']

tab1_layout = [[sg.LB(lista,size=(30,5))]]
tab2_layout = [[sg.LB(listb,size=(30,5))]]



layout = [
    [sg.TabGroup([[sg.Tab('资料',tab1_layout),sg.Tab('程序员',tab2_layout)]])]
]

window = sg.Window('demo10', layout)
while True:
    event, values = window.read()
    if event == None:
        break
    if event == '确定':
        window['-a-'].Update(visible=False)
        window['-b-'].Update(visible=True)


window.close()
