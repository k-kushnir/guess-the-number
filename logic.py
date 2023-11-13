import random
import PySimpleGUI as sg
import database as settings


class NumberGuessingGame:
    def __init__(self):
        self.number = 0
        self.attempts = 0
        self.window = None

    def initialize_game(self):
        self.number = random.randint(
            settings.start_number, settings.end_number)
        self.attempts = settings.attempts

        sg.theme(settings.theme)

        layout = [
            [sg.Text(
                f"Я загадав число від {settings.start_number} до {settings.end_number}. У вас буде {settings.attempts} спроб, щоб вгадати його.")],
            [sg.Text("Введіть число: "), sg.InputText(key='attempt')],
            [sg.Button("Вгадати", key='guess'), sg.Button("Вийти"),
             sg.Button("Грати знову", disabled=True, key='again')],
            [sg.Text("", size=(50, 1), key='result')]
        ]

        self.window = sg.Window("Гра вгадай число", layout)

    def handle_guess_attempt(self, attempt):
        if attempt == self.number:
            self.window['result'].update("Ви вгадали! Ви перемогли!")
            self.disable_guess_button()
        elif attempt < self.number:
            self.window['result'].update(
                f"Загадане число більше. Спроб залишилось: {self.attempts}")
        else:
            self.window['result'].update(
                f"Загадане число менше. Спроб залишилось: {self.attempts}")

    def disable_guess_button(self):
        self.window['guess'].update(disabled=True)
        self.window['again'].update(disabled=False)

    def run_game(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == "Вийти":
                self.window.close()
                break

            try:
                attempt = int(values['attempt'])
            except ValueError:
                self.window['result'].update("Будь ласка, введіть ціле число.")
                continue

            if settings.start_number <= attempt <= settings.end_number:
                self.attempts -= 1
                self.handle_guess_attempt(attempt)

                if self.attempts == 0:
                    self.window['result'].update(
                        f"Гра закінчена. Загадане число було {self.number}.")
                    self.disable_guess_button()
            else:
                self.window['result'].update(
                    f"Будь ласка, введіть число від {settings.start_number} до {settings.end_number}.")

            if event == "again":
                self.window.close()
                self.initialize_game()
                self.run_game()
                return
