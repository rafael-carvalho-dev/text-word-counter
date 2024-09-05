# Text Word Counter

**Text Word Counter** is a simple word frequency counter application. The program reads a text input provided by the user, normalizes the text (removing punctuation and converting it to lowercase), and displays the frequency of each word in ascending order.

**Text Word Counter** é um aplicativo simples de contagem de frequência de palavras em blocos de texto. O programa lê uma entrada de texto fornecida pelo usuário, normaliza o texto (removendo pontuações e convertendo para minúsculas) e exibe a frequência de cada palavra em ordem crescente de frequência.

## Features / Funcionalidades
- Displays a stylized title using **ASCII art**. / Exibe um título estilizado usando ASCII art.
- Accepts text input from the user and counts word frequency. / Conta a frequência de palavras de um texto.
- Displays words and their frequencies in ascending order. / Exibe as palavras e suas frequências em ordem crescente.
- Allows the user to keep processing new texts or exit the program. / Permite continuar processando textos ou sair.

## Installation / Instalação

### Prerequisites / Pré-requisitos
- Python 3.8 or higher
- **cx_Freeze** (for generating executables / para geração de executáveis)
- Terminal compatible with **Colorama** for color display. / Deve ser compatível com Colorama para exibição de cores.

### Dependencies / Dependências
The following Python libraries are required to run the project:
(As seguintes bibliotecas Python são necessárias para rodar o projeto:)
- `pyfiglet`
- `colorama`
- `collections`
- `logging`
- `cx_Freeze`

### Installing Dependencies / Instalação das dependências
You can install all the dependencies at once using the `requirements.txt` file:
(Você pode instalar todas as dependências de uma vez usando o `requirements.txt`:)

`pip install -r requirements.txt`

### How to Run the Project / Como executar o projeto

1. Clone the repository to your local machine / Clone o repositório para sua máquina local:

   `git clone https://github.com/yourusername/text-word-counter.git`

2. Navigate to the project directory / Navegue até o diretório do projeto:

   `cd text-word-counter`

3. Run the `main.py` file / Execute o arquivo `main.py`:

   `python main.py`

### Generate the Executable (Windows) / Geração do executável (Windows)
If you want to generate the application’s executable, follow the steps below:
(Se você quiser gerar o executável da aplicação, siga as etapas abaixo:)

1. Install **cx_Freeze** / Instale **cx_Freeze**:
   
   `pip install cx-Freeze`

2. Run the build script / Execute o script de build:

   `python setup.py build`

3. The generated executable will be available in the `build` directory.
(O executável gerado estará disponível no diretório `build`.)

## Project Structure / Estrutura do projeto
The code is divided into different modules to maintain an organized structure:
(O código está dividido em diferentes módulos para manter uma estrutura organizada:)

- **main.py**: Contains the main logic to run the application.
- **display_manager.py**: Manages the display of the title and console clearing.
- **io_manager.py**: Manages user input.
- **language_manager.py**: Manages the application language.
- **process_manager.py**: Contains functions for text processing and word frequency calculation.

- **main.py**: Contém a lógica principal para executar o aplicativo.
- **display_manager.py**: Gerencia a exibição do título e a limpeza do console.
- **io_manager.py**: Gerencia a entrada do usuário.
- **language_manager.py**: Gerencia o idioma do aplicativo.
- **process_manager.py**: Contém funções para processamento de texto e cálculo de frequência de palavras.

## License / Licença

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---
