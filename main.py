import PySimpleGUI as sg

def janela_login():
    sg.theme('Black')
    layout_1 = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]

    return sg.Window('Login', layout=layout_1, finalize=True)

def janela_pedido():
    sg.theme('Black')
    layout_2 = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Calabresa c/ Catupiry', key='pizza1'),
         sg.Checkbox('Pizza Camarão c/ Catupiry', key='pizza2')],
        [sg.Ok('Pedir'), sg.Cancel('Voltar')]
    ]

    return sg.Window('Pedido', layout=layout_2, finalize=True)
#
janela1, janela2 = janela_login(), None

while True:
    window,event,values = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    #
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Pedir':
        print(f'O pedido foi emitido com sucesso!')
        break

