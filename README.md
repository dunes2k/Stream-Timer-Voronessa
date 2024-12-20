# Stream Timer Voronessa
![icon](https://github.com/user-attachments/assets/33c3888d-a2fc-4852-8d9e-478c6847ef3f)
#### Easy to use, written in Python using Tkinter.
#### Download the installation file for Windows: https://github.com/dunes2k/Stream-Timer-Voronessa/releases/tag/v1.3
![introduction](https://github.com/user-attachments/assets/90aec769-8fd4-40e0-b70f-d9dde4d3b90e)
## How to start using Voronessa?
- Download this repository, then run main.py
- You can also download a binary build and use it (only Windows)
## Using
- Exit the countdown mode by double-clicking the mouse button
- The clock_pack folder should be located in the working directory
## Your own style
#### You can use your own style packs by uploading them to the clock_pack directory.
#### clock_pack directory map:
```
clock_pack directory |
                     |
                styles directory (ASCII, ceramic, default etc...)
                                             |
                                             |
                                colors directory (white, red, blue etc...)
                                                    |
                                                    |
                                                digit files directory (_0.png, 0.png, 1.png etc...)
```
- Each folder in the clock_pack directory is style-defining
- Each folder defining the style contains folders defining the colors of the style
- Each color folder contains its own set of png elements defining the dial
- The _0.png file defines the separator between the digits of the dial
- The following files from 0.png to 9.png correspond to the number of digits in the decimal system
#### example: directory - clock_pack\default\white
![style_color](https://github.com/user-attachments/assets/8d42adc4-cc3c-42f0-9712-d76a2804d8c2)
- The style folder also contains a file "!empty" which tells the scanner not to ignore this style and add it to the program at startup
- The folder defining the color includes the file "include", which tells the scanner to add this color to the program at startup.
- Do not put files with names "include" and "!empty" to empty folders, as this may cause an error at startup.
- The image file should have an opaque black background in order to avoid any display issues.
- The image size should be 192 x 360 pixels.
- The image must be in PNG format.
