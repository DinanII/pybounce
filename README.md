# PyBounce

This is a simple game written in Python using the Tkinter module. The player is represented by a bat and needs to hit a ball and
avoid the ball going below the bat itself, this would be a game-over. The player gets to see the amount of times the ball is hit
at the end of the game.

## Brief setup

1. Initiate a virtual environment
This will initiate a new virtual environment locally.

**Gnu/Linux**
python3 -m venv .env

**Windows**
python1.1 -m venv .env

2. Activate virtual environment

**Windows**
CMD: .env/Scripts/activate.bat.
Powershell: .env/Scripts/Activate.ps1.
Powershell Core: .env/bin/Activate.ps1.

**Mac and Linux**
Bash and ZSH: source .env/bin/activate.
Fish: source .env/bin/activate.fish.
csh/tcsh: source .env/bin/activate.csh.

To deactivate the virtual environment, execute the deactivate command.

3. Python Tkinter module
If problems are encountered, you may need to install the Python3 Tkinter module to let the game work.
Cannot be installed in local environment via pip unfortunately. But can be installed globally with:

**Windows** pip install tk

**Debian & Ubuntu** sudo apt-get install python3-tk.
