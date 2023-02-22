Install the dependencies:
pip install -r requirements.txt

Build the project
pyinstaller AppNotas.py
pyinstaller --noconsole --windowed --icon=icons/app_icon.jpg AppNotas.py

(Running the app creates the .appnotas folder automatically)

On linux, create an .appnotas dir in your home directory
mkdir ~/.appnotas

On windows create it in C:\User\<user>\AppData\Local\appnotas

Copy the icons there
cp icons ~/.appnotas/ -r


The executable is dist/AppNotas/AppNotas
On linux, modify the .desktop and copy it to ~/.local/share/applications
On windows, right click the .exe and pin it to the start menu
