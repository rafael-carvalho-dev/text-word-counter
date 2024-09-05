import logging
from display_manager import print_title, clear_console
from io_manager import get_user_input, ask_continue
from language_manager import choose_language, translations 
from process_manager import show_word_frequency
from time import sleep

logging.basicConfig(filename='app.log', level=logging.ERROR)

def app_launcher():
    """Launches the main application loop."""
    
    print_title()
    sleep(5)
    print('\n')
    lang = choose_language()
    clear_console()
    sleep(0.5)
    

    while True:
        try:
            text = get_user_input(lang)
            sleep(2)
            print(f'\n{translations[lang]["word_frequency"]}\n')
            sleep(1)
            show_word_frequency(text, lang)
            sleep(0.5)

            if not ask_continue(lang):
                clear_console()
                break

        except ValueError as ve:
            print(f"{translations[lang]['error']}{ve}")
            sleep(2)
            clear_console()

        except Exception as e:
            logging.error("An unexpected error occurred", exc_info=True)
            print(f"{translations[lang]['unexpected_error']}{e}")
            sleep(2)
            clear_console()
            break


if __name__ == '__main__':
    app_launcher()
