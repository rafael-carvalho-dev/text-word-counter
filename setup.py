from cx_Freeze import setup, Executable

# Define the build options
build_options = {
    "packages": ["os", "time", "logging", "pyfiglet", "colorama", "string", "collections"],
    "include_files": [
        "display_manager.py",
        "io_manager.py",
        "language_manager.py",
        "process_manager.py",
        "block.ico"
    ]
}

# Set base to None for terminal applications
base = None

# Application setup
setup(
    name="Text Word Counter",
    version="1.0",
    description="A simple text word frequency counter application.",
    author="Acme Soft Inc.",
    options={"build_exe": build_options},
    executables=[Executable("main.py", base=base, target_name="TextWordCounter.exe", icon="block.ico")]
)
