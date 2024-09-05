# Dictionary that holds translations for English and Portuguese
translations = {
    'en': {
        'input_text': 'Please enter some text: ',
        'word_frequency': 'Words Frequency:',
        'continue_prompt': 'Would you like to keep going? (Y/N): ',
        'error': 'Error: ',
        'unexpected_error': 'An unexpected error occurred: ',
        'empty_input': 'Input cannot be empty. Please enter some text.',
        'invalid_continue': "Invalid input. Please enter 'Y' or 'N'."
    },
    'pt': {
        'input_text': 'Por favor, insira algum texto: ',
        'word_frequency': 'Frequência de Palavras:',
        'continue_prompt': 'Gostaria de continuar? (S/N): ',
        'error': 'Erro: ',
        'unexpected_error': 'Ocorreu um erro inesperado: ',
        'empty_input': 'A entrada não pode estar vazia. Por favor, insira algum texto.',
        'invalid_continue': "Entrada inválida. Por favor, insira 'S' ou 'N'."
    }
}


def choose_language():
    """Allows the user to choose between English and Portuguese."""
    languages = {
        '1': 'en',
        '2': 'pt'
    }
    
    while True:
        print("Choose your language / Escolha seu idioma:")
        print("1. English")
        print("2. Português-Br")

        choice = input("Enter 1 or 2: ").strip()
        
        if choice in languages:
            return languages[choice]
        else:
            # Display an error message and prompt again
            print("Invalid choice. Please enter 1 for English or 2 for Portuguese.")
