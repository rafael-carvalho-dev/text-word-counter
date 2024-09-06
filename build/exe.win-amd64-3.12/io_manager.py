from language_manager import translations

def get_user_input(lang):
    """Gets user input as a string and ensures it is not empty.

    Args:
        lang (str): The current language selected by the user.

    Returns:
        str: The text entered by the user.

    Raises:
        ValueError: If the user does not enter any text.
    """
    user_input = input(translations[lang]['input_text']).strip()
    if not user_input:
        raise ValueError(translations[lang]['empty_input'])
    return user_input


def ask_continue(lang):
    """Asks the user if they want to continue.

    Args:
        lang (str): The current language selected by the user.

    Returns:
        bool: True if the user wants to continue, False otherwise.

    Raises:
        ValueError: If the user enters an invalid response.
    """
    response = input(translations[lang]['continue_prompt']).strip().lower()
    valid_responses = ['y', 'n'] if lang == 'en' else ['s', 'n']
    if response not in valid_responses:
        raise ValueError(translations[lang]['invalid_continue'])
    return response in ['y', 's']
