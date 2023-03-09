## Setup
### Dependencies

Install the dependencies by running:

`pip install -r requirements.txt`

### Build the project
`pyinstaller --noconsole --windowed --icon=icons/app_icon.jpg src/AppNotas.py`


### Running the app
The executable is located at dist/AppNotas/AppNotas.

On Linux, modify the .desktop file and copy it to ~/.local/share/applications to get a shortcut

On Windows, right-click the .exe file and pin it to the start menu.


### Icons

Create the .appnotas folder if it's not already there

`mkdir ~/.appnotas`

Copy the icons there

`cp icons ~/.appnotas/ -r`

On Windows, create it in C:\User\<user>\AppData\Local\appnotas.