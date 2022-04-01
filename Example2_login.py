import PySimpleGUI as sg

User1 = {'用户名': 'abc', '密码': '123'}
User2 = {'用户名': 'admin', '密码': '456'}
User3 = {'用户名': 'user211', '密码': '789'}

UserList = [User1, User2, User3]

layout = [
    [sg.B('中文'), sg.B('English')],
    [sg.T('用户名', key='-username-', size=(8, 1)), 
     sg.In('请输入您的用户名', key='-user-'), sg.FileBrowse()],
    [sg.T('密码', key='-password-', size=(8, 1)),
     sg.In('', tooltip='密码为3位数字', key='-pwd-', password_char='*')],
    [sg.B('确定', key='-confirm-'), sg.B('取消', key='-cancle-')]
]

window = sg.Window('Login GUI', layout)

while True:
    event, values = window.read()
    if event == None:
        break
    if event == 'English':
        window['-username-'].update('Username')
        window['-password-'].update('Password')
        window['-confirm-'].update('Confirm')
        window['-cancle-'].update('Cancle')
    if event == '中文':
        window['-username-'].update('用户名')
        window['-password-'].update('密码')
        window['-confirm-'].update('确定')
        window['-cancle-'].update('取消')
    if event == '确定':
        for user in UserList:
            if values['-user-'] == user['用户名'] and values['-pwd-'] == user['密码']:
                msg = '输入正确'
            else:
                msg = '输入错误'
            sg.Popup(msg)
            break

window.close()
