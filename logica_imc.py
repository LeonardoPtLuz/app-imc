import PySimpleGUI as sg
from layout_main import *
from imc_homem_mulher import *


def logica():
    window = layout_main()

    while True:
        event, values = window.read()


        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break
        
        if event == 'Calcular':
            try:
                if values['-MASCULINO-'] and values['-FEMININO-']:
                    window['-IMC_OUTPUT-'].update('Apenas um sexo por vez!', text_color='red')   
                    
                elif values['-MASCULINO-'] and (not values['-INPUT_PESO-'] or not values['-INPUT_ALTURA-']):
                    window['-IMC_OUTPUT-'].update('Faltam informações do sexo masculino!', text_color='red')

                elif values['-FEMININO-'] and (not values['-INPUT_PESO-'] or not values['-INPUT_ALTURA-']):
                    window['-IMC_OUTPUT-'].update('Faltam informaçoes do sexo feminino!', text_color='red')

                elif values['-MASCULINO-']:
                    imc_result = imc_masculino(float(values['-INPUT_PESO-']), float(values['-INPUT_ALTURA-']))
                    window['-IMC_OUTPUT-'].update(imc_result, text_color='green')

                elif values['-FEMININO-']:
                    imc_result = imc_feminino(float(values['-INPUT_PESO-']), float(values['-INPUT_ALTURA-']))
                    window['-IMC_OUTPUT-'].update(imc_result, text_color='green')
            
            except TypeError as er:
                #window['-IMC_OUTPUT-'].update(er)
                print(er)
            
        elif event == 'Resetar':
            window['-INPUT_IDADE-'].update('')
            window['-INPUT_ALTURA-'].update('')
            window['-INPUT_PESO-'].update('')
            window['-MASCULINO-'].update('')
            window['-FEMININO-'].update('')
            window['-IMC_OUTPUT-'].update('')

    window.close()