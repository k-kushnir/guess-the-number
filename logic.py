import random
import PySimpleGUI as sg
import database as settings


def game_logic():
    while True:
        number = random.randint(settings.start_number, settings.end_number)
        attempts = settings.attempts

        # Зміна теми програми
        sg.theme(settings.theme)

        layout = [
            [sg.Text(
                f"Я загадав число від {settings.start_number} до {settings.end_number}. У вас буде {settings.attempts} спроб, щоб вгадати його.")],
            [sg.Text("Введіть число: "), sg.InputText(key='attempt')],
            # Додавання кнопки перезапуску гри
            [sg.Button("Вгадати", key='guess'), sg.Button("Вийти"),
             sg.Button("Грати знову", disabled=True, key='again')],
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

            if attempt < settings.start_number or attempt > settings.end_number:
                window['result'].update(
                    f"Будь ласка, введіть число від {settings.start_number} до {settings.end_number}.")
                continue

            attempts -= 1

            if attempt == number:
                window['result'].update("Ви вгадали! Ви перемогли!")
                window['guess'].update(disabled=True)
                window['again'].update(disabled=False)
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
                window['guess'].update(disabled=True)
                window['again'].update(disabled=False)
                break

        while True:
            event, values = window.read()
            # логіка перезапуску гри
            if event == "again":
                window.close()
                game_logic()
                return
            if event == sg.WIN_CLOSED or event == "Вийти":
                window.close()
                return
