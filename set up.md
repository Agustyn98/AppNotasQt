Install the dependencies:
pip install -r requirements.txt

Build the project
pyinstaller AppNotas.py
pyinstaller --noconsole --windowed --icon=icons/app_icon.jpg

On linux, create an .appnotas dir in your home directory
mkdir ~/.appnotas

Copy the icons there
cp icons ~/.appnotas/ -r

The executable is dist/AppNotas/AppNotas
