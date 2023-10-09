# logic_module.py
import random
import PySimpleGUI as sg
import database as settings


def game_logic():
    while True:
        number = random.randint(settings.start_number, settings.end_number)
        attempts = settings.attempts

        layout = [
            [sg.Text(
                f"Я загадав число від {settings.start_number} до {settings.end_number}. У вас буде {settings.attempts} спроб, щоб вгадати його.")],
            [sg.Text("Введіть число: "), sg.InputText(key='attempt')],
            [sg.Button("Вгадати"), sg.Button("Вийти")],
            [sg.Text("", size=(50, 1), key='result')]
        ]

        window = sg.Window("Гра вгадай число", layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "Вийти":
                window.close()
                break

            try:
                attempt = int(values['attempt'])
            except ValueError:
                window['result'].update("Будь ласка, введіть ціле число.")
                continue

            attempts -= 1
            if attempt == number:
                window['result'].update("Ви вгадали! Ви перемогли!")
                break
            elif attempt < number:
                window['result'].update(
                    f"Загадане число більше. Спроб залишилось: {attempts}")
            else:
                window['result'].update(
                    f"Загадане число менше. Спроб залишилось: {attempts}")

            if attempts == 0:
                window['result'].update(
                    f"Гра закінчена. Загадане число було {number}.")
                break

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "Вийти":
                window.close()
                return
