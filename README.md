# PyBounce

This is a simple game written in Python using the Tkinter module. The player is represented by a bat and needs to hit a ball and
avoid the ball going below the bat itself, this would be a game-over. The player gets to see the amount of times the ball is hit
at the end of the game.

## Brief setup

1. Initiate a virtual enviroment 
This will initiate a new virtual enviroment locally. Please use the interpeter included in the virtual enviroment (.env/bin/python).

**Gnu/Linux**
python3 -m venv .env

**Windows**
python -m venv .env

2. Activate virtual enviroment

  **Windows**
  CMD: .env/Scripts/activate.bat.
  Powershell: .env/Scripts/Activate.ps1.
  Powershell Core: .env/bin/Activate.ps1.

  **Mac and Linux**
  Bash and ZSH: source .env/bin/activate.
  Fish: source .env/bin/activate.fish.
  csh/tcsh: source .env/bin/activate.csh. To deactivate the virtual enviroment, execute the deactivate command.

3. Install packages
  pip install -r requirements.txt. This will install all packages listed in {project_root}/requirements.txt.
  If a new dependency is installed, run pip freeze > requirements.txt so every package (including new ones) is registered, so others can also easily install. There are no packages installed currently, so this step is not neccesary.

4. Python Tkinter module
If problems are encountered, you may need to install the Python3 Tkinter module (for the game). 
Cannot be installed in local enviroment via pip. But can be installed globally with:

**Windows**
pip install tk

**Debian & Ubuntu** 
Gnu/Linux distributions 
sudo apt-get install python3-tk.
