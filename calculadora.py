import PySimpleGUI as sg

def tela_calculadora():
    sg.theme('Dark')
    layout_tela = [[sg.Output(size=(10, 8))],
                   [sg.Button('9', k='-9-'), sg.Button('8', k='-8-'), sg.Button('7', k='-7-')],
                   [sg.Button('6', k='-6-'), sg.Button('4', k='-5-'), sg.Button('4', k='-4-')],
                   [sg.Button('3', k='-3-'), sg.Button('2', k='-2-'), sg.Button('1', k='-1-')],]

    return sg.Window('Calculadora', layout=layout_tela, finalize=True)

window = tela_calculadora()

while True:
    window,event,values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break
    if event == '-9-':
        valor = 9
        print(valor)
    if event == '-8-':
        valor = 8
        print(valor)
    if event == '-7-':
        valor = 7
        print(valor)
    if event == '-6-':
        valor = 6
        print(valor)
    if event == '-5-':
        valor = 5
        print(valor)
    if event == '-4-':
        valor = 4
        print(valor)
    if event == '-3-':
        valor = 3
        print(valor)
    if event == '-2-':
        valor = 2
        print(valor)
    if event == '-1-':
        valor = 1
        print(valor)

