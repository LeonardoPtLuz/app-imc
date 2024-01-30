import PySimpleGUI as sg


def layout_main():
        sg.theme('Black')
        layout = [
                [sg.Frame('Sexo', layout=[
                        [sg.Checkbox('Masculino', key='-MASCULINO-'), sg.Checkbox('Feminino', key='-FEMININO-')],
                ])],
                # [sg.Frame('Idade', layout=[
                #         [sg.Input(key='-INPUT_IDADE-', size=(6, 1))],
                # ])],
                [sg.Frame('Altura', layout=[
                        [sg.Input(key='-INPUT_ALTURA-', size=(6, 1)), sg.Text('cm')],
                ])],
                [sg.Frame('Peso', layout=[
                        [sg.Input(key='-INPUT_PESO-', size=(6, 1)), sg.Text('kg')],
                ])],
                [sg.Frame('IMC', layout=[
                        [sg.Text(size=(30, 1), key='-IMC_OUTPUT-')],
                ])],

                [sg.Button('Calcular'), sg.Button('Resetar'), sg.Button('Sair')]
                ]
        return sg.Window('Calculadora IMC', layout=layout, finalize=True) 
