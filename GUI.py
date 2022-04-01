import weblfasr_python3_demo
import _thread
import PySimpleGUI as sg

# sg.theme('LightGreen')
menu = [
    ['文件(&F)',['新建','打开','保存','---','退出']],
    ['编辑(&E)',['撤销','重做','剪切','保存']],
    ['帮助(&H)',['检查更新','使用指南','关乎']]

]


layout = [
    [sg.Menu(menu)],
    [sg.T("选择待转换的语音文件：", font=('宋体',11)), sg.In(key = '-sourcefile-', tooltip = "仅支持'.mp3'文件"), sg.FileBrowse(button_text="选择", file_types=(("mp3文件", "*.mp3")), font=('宋体',11))],
    [sg.T("选择文本文件保存路径：", font=('宋体',11)), sg.In(key = '-outfile-'),sg.FileSaveAs(button_text="选择", file_types=(("txt文本文件", "*.txt")), font=('宋体',11))],
    [sg.Output(key='-YY-', size=(75, 30))],
    [sg.B('开始转换',  key='-start-', font = ('宋体',11))]
]

window = sg.Window('峰哥专属语音转文本助手/by豪哥&大强', layout)

while True:
    event, values = window.read()
    if event == None:
        break
    if event == '-start-':
        source_file = values['-sourcefile-']
        out_file = values['-outfile-']
        print("小峰峰等等，正在转换！！！")
        try:
            _thread.start_new_thread( weblfasr_python3_demo.begain, (source_file, out_file))
        except:
            print ("Error: 无法启动线程")

window.close()
