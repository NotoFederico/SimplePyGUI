# SimplePyGUI
A python GUI desktop application which redirects the user to go to NASA's Perseverance Site

---

![SimplePyGUI.Cover](Cover.PNG)

---

### Builds
| Latest release | Latest development build |
|----------------|--------------------------|
| [![Noto](https://img.shields.io/badge/master-v1.0-green.svg)](https://github.com/NotoFederico/SimplePyGUI/tree/main) | [![Noto](https://img.shields.io/badge/develop-v1.1+-blue.svg)](https://github.com/NotoFederico/SimplePyGUI/tree/dev) |

---

# Contents
- 1 - [Introduction](#1-introduction)
- 2 - [Building the application](#2-building-the-application)
  - 2.1 - [Building prerequisites](#21-building-prerequisites)
  - 2.2 - [Compiling and running](#22-compiling-and-running)
- 3 - [Contributing](#3-contributing)
- 4 - [Licence](#4-licence)

---

# 1. Introduction

**SimplePyGUI** is a open source application made in Python and Glade (GUI). The simple graphic interface allows 
the user to go to NASA's Perseverance site with a single click.

---

# 2. Building the application

## 2.1 Building prerequisites

**You need python for either operative system. Get it from https://www.python.org/downloads/**

### Windows
1. Clone the repository
2. Go to http://www.msys2.org/ and download the x86_64 installer
3. Follow the instructions on the page for setting up the basic environment
4. Run C:\msys64\mingw64.exe - a terminal window should pop up
5. Execute pacman -Suy 
6. The console will close after finishing step 5. Repeat step 4 and 5, then continue with step 7
7. Execute pacman -S mingw-w64-x86_64-gtk3 mingw-w64-x86_64-python3 mingw-w64-x86_64-python3-gobject
8. Execute pacman -S mingw-w64-x86_64-python-requests
9. Use cd command to go to the local path folder where you cloned the repository, i.e, "cd C:/Users/MyUser/Documents/SimplePyGUI"
10. Execute python main.py

### GNU/Linux
1. Clone the repository

---

## 2.2 Compiling and running

### Windows
1. Run C:\msys64\mingw64.exe - a terminal window should pop up
2. Use cd command to go to the local path folder where you cloned the repository
3. Execute python main.py

### GNU/Linux
1. Open a terminal in the local path folder where you cloned the repository
2. Execute python main.py

---

# 3. Contributing
SimplePyGUI uses the [gitflow workflow](https://www.atlassian.com/git/tutorials/comparing-workflows#gitflow-workflow). If you are implementing a new feature or logic from the original game, please branch off and perform pull requests to ```develop```. If you are fixing a bug for the next release, please branch off and perform pull requests to the correct release branch. ```master``` only contains tagged releases, you should never branch off this.

---
# 4. Licence

SimplePyGUI is licensed under the GNU General Public License version 3.


