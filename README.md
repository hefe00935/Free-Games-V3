[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)

# Free Games V3
New and improved games grabber for Epic Games that utilizes the Desktop Application rather than the webapp. Designed to run on Windows, but this should also work on Mac and Linux.

This is a improved version of the Free-Games-V2 and not offical I'm not the original creator

<br><br>

## Logs in for you
![](https://github.com/MasonStooksbury/Free-Games-V2/blob/main/GIFs/login.gif)

<br>

## And grabs the free game! (sorry for the terrible quality. I had to compress it to make GitHub happy)
![](https://github.com/MasonStooksbury/Free-Games-V2/blob/main/GIFs/grabbing_game.gif)

<br><br>


# Installation and Setup
- Install Python [from their website](https://www.python.org/downloads/)
  - Be sure to install PIP if it asks
  - Check any boxes related to PATH (this will make execution by any scheduling tool much easier)
- Clone this repository or download a ZIP using the green `Code` button on GitHub
- In a terminal or command prompt run this command to install the required dependencies:
  - pip install opencv-python python-dotenv pyautogui Pillow numpy os
  - (If that doesn't work, try `pip3` instead of `pip`)
 - Open setup-env.py
 - Input your epic games path, e-mail, password     (e-mail,password not neccesery but recommended)
  - For Windows: Open a command prompt, navigate to the folder housing the `Free_Games_V3.py` file and run it with `.\Free_Games_V3.py`. You can also just open the folder in the File Explorer and double-click on it
  - For Mac: Open a terminal, navigate to the folder housing the `Free_Games_V3.py` file, and run it with `python3 ./Free_Games_V3.py`.


<br>

# Schedule to run automatically
Basically, just use `Windows Task Scheduler` or a `CRON` job to run that script whenever you need to (I forget when Epic drops games now, but Friday should do it)


<br><br>

## Edge cases
### Can pass the EULA screen
![](https://github.com/MasonStooksbury/Free-Games-V2/blob/main/GIFs/passing_eula.gif)

<br><br>

