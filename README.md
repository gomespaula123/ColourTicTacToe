# ColourTicTacToe
Final project programming

REFERENCES:
# for creating the screen:
# Reference note: http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/creating-pygame-window/

here are the calmlywriter notes:
- default class with the position

*‌ with the rect

start screen draw square
if that works, start to try to make the more complex logic
the input, if input's working
if input's working , draw on the screen what's happening
9 squares, change colour when it's x or o
trying to actually draw x and o


Steps:

1: start a window ->‌ make sure you can display information, main
2: draw a simple square -> in class board, from main call class BoardVisual
3: get the input working ->‌
4: draw the actual situation of the game (9 squares)
5: change color according to sitaution (red: cross, blue: circle)
6: acturaly draw crosses and circles
after step 4, do AI, then 5


Functions for the main class:
Set_Position(player, position)
Update_Board()
AI_Position()
DidItEnd
StartWindow()
CloseWindow()


main window would have the position
separate function, send this information and would draw



class visual interface:
startwindow, closewindow, draw board

pygame.init

text.rect


In the board :‌ have 8 images, each image has a correct word with it
In the human player/opencv bit:‌ have 8 ranges of colours, each range (if within this range)‌ would have a colour with it

Compare the input colour (word)‌
input colour (word) -> send to the board

set position ->‌ class

Human Player Class
*‌ send colour to board


BoardVisual
* all images are matched with a colourname
*‌ receives input from Human Player Class (detected_colourname)
*‌ draws mark on position of the image where colourname = detected_colourname
*‌ replace image for markX_image if colourname = detected_colourname


BoardAnalysis

ImageRed = 0
ImageBlue = 0
etc.

ImageMarkX = 1
ImageMarkO = 2

- check win: (hardcoded bit)
- check full: (check whether there is any image 0, if none, return True)








draws the mark on the place of the image of the colour
