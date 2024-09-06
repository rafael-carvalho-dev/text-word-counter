from language_manager import translations

def get_user_input(lang):
    """Gets multi-line user input as a string and ensures it is not empty.

    Args:
        lang (str): The current language selected by the user.

    Returns:
        str: The text entered by the user.

    Raises:
        ValueError: If the user does not enter any text.
    """
    print(translations[lang]['input_text'])
    print(translations[lang]['multi_line_hint'])  # A tip for the user on how to close the input
    
    lines = []
    while True:
        line = input()  # Captures one row at a time
        if not line.strip():  # When the user types an empty line
            break
        lines.append(line.strip())  # Remove extra spaces in each line and add to the array of lines

    full_text = ' '.join(lines)  # Unite all lines into a single string, separated by a space

    if not full_text:
        raise ValueError(translations[lang]['empty_input'])

    return full_text


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
