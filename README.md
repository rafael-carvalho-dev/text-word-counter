<<<<<<< HEAD
# text-word-counter
A simple word frequency counter application.
=======
# Text Word Counter

**Text Word Counter** is a simple word frequency counter application. The program reads a text input provided by the user, normalizes the text (removing punctuation and converting it to lowercase), and displays the frequency of each word in ascending order.

## Features
- Displays a stylized title using **ASCII art**.
- Accepts text input from the user and counts word frequency.
- Displays words and their frequencies in ascending order.
- Allows the user to keep processing new texts or exit the program.

## Installation

### Prerequisites
- Python 3.8 or higher
- **cx_Freeze** (for generating executables)
- Terminal compatible with **Colorama** for color display.

### Dependencies
The following Python libraries are required to run the project:
- `pyfiglet`
- `colorama`
- `collections`
- `logging`
- `cx_Freeze`

### Installing Dependencies
You can install all the dependencies at once using the `requirements.txt` file:

`pip install -r requirements.txt`

### How to Run the Project

1. Clone the repository to your local machine:

   `git clone https://github.com/yourusername/text-word-counter.git`

2. Navigate to the project directory:

   `cd text-word-counter`

3. Run the `main.py` file:

   `python main.py`

### Generate the Executable (Windows)
If you want to generate the application’s executable, follow the steps below:

1. Install **cx_Freeze**:
   
   `pip install cx-Freeze`

2. Run the build script:

   `python setup.py build`

3. The generated executable will be available in the `build` directory.

## Project Structure
The code is divided into different modules to maintain an organized structure:

- **main.py**: Contains the main logic to run the application.
- **display_manager.py**: Manages the display of the title and console clearing.
- **io_manager.py**: Manages user input.
- **process_manager.py**: Contains functions for text processing and word frequency calculation.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---
>>>>>>> d62de93 (Initial commit)
