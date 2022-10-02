import PySimpleGUI as sg

def janela_cadastro():
    sg.theme('Black')
    layout_register = [[sg.T('SIGN UP', font=40)],
                        [sg.Text("Login:"), sg.Input("", k='-LOGIN1-')],
                       [sg.Text("Password:"), sg.Input("", k='-SENHA1-', password_char="*")],
                       [sg.Text("Email Adress"), sg.Input("", k='-EMAIL1-')],
                       [sg.Ok('Register'), sg.Cancel('Exit'), sg.Cancel('Sign In')]
                       ]

    return sg.Window('Register', layout=layout_register, finalize=True)

def janela_verificacao():
    layout_verifica = [[sg.T('Cadastro realizado com sucesso')],
                       [sg.Ok('Exit')]]
    return sg.Window('Confirmação', layout=layout_verifica, finalize=True)

def janela_login():
    sg.theme('Black')
    layout_login = [[sg.T('SIGN IN', font=40)],
                        [sg.Text("Login:"), sg.Input("", k='-LOGIN-')],
                       [sg.Text("Senha:"), sg.Input("", k='-SENHA-', password_char="*")],
                       [sg.Ok('Login'), sg.Cancel('Exit'), sg.Cancel('Sign Up')]
                       ]

    return sg.Window('Login', layout=layout_login, finalize=True)

def janela_principal():
    sg.theme('Black')
    layout_principal = [[sg.T(f'Seja bem vindo, {login}')],
                        sg.Cancel('Deslogar')]
    return sg.Window('Painel do Usuario', layout=layout_principal, finalize=True)

def buscar_usuario():
    users = []
    try:
        with open('usuarios.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(",")
                users.append(linha.split())

            for user in users:
                userx = user[0]
                passw= user[1]
                if values['-LOGIN1-'] == userx and values['-SENHA1-'] == passw:
                    return True
    except FileNotFoundError:
        return False

janela1, janela2, janela_verificat, janela3 = janela_cadastro(), None, None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED or event == 'Exit':
        break
    if window == janela2 and event == sg.WIN_CLOSED or event == 'Exit':
        break
    if window == janela_verificat and event == sg.WIN_CLOSED or event == 'Exit':
        break
    if window == janela3 and event == sg.WIN_CLOSED or event == 'Exit':
        break
    if window == janela1 and event == 'Sign In':
        janela1.hide()
        janela2 = janela_login()
    if window == janela2 and event == 'Sign Up':
        janela2.hide()
        janela1.un_hide()
    if window == janela1 and event == 'Register':
        login = values['-LOGIN1-']
        senha = values['-SENHA1-']
        email = values['-EMAIL1-']
        with open('usuarios.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
            arquivo.writelines(f'{login} {senha} {email}\n')
    if window == janela2 and event == 'Login':
        buscar_usuario()
        if userx == values['-LOGIN-'] and passw == values['-SENHA-']:
            janela3 = janela_principal()
            janela2.hide()
    if window == janela3 and event == 'Deslogar':
        janela3.hide()
        janela2.un_hide()

