Python code that randomly selects an image from a specified directory and sets it as the wallpaper for dark mode in GNOME

Here’s how to make your Python script run every time you start Ubuntu:

1. Create a .desktop file for autostart
Open a terminal and run:

  nano ~/.config/autostart/random_wallpaper.desktop

If the folder ~/.config/autostart doesn’t exist, create it:

  mkdir -p ~/.config/autostart

Paste the following content into the editor:

  [Desktop Entry]
  Type=Application
  Exec=python3 /path/to/your/script/random_wallpaper.py
  Hidden=false
  X-GNOME-Autostart-enabled=true
  Name=Random Wallpaper Setter
  Comment=Sets a random wallpaper on system startup

Replace /path/to/your/script/random_wallpaper.py with the full path to your Python script.

Save the file by pressing Ctrl + O, then Enter. Exit the editor with Ctrl + X.
