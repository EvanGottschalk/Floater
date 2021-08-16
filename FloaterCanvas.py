from tkinter import *
import Floater

class FloaterCanvas:

    #creates the game object
    def __init__(self):
        self.root = Tk()
        self.game = Floater.Floater()
        self.switch = 'green'
        self.root.title('Floater - Level '+str(self.game.getLevel()))
        self.Map = self.createFloaterMap(self.game.getLevel())
        self.Map.bind_all('<Key>', self.moveFloater)
        self.createObjects()
        mainloop()

    #creates the canvas the game is played on
    def createFloaterMap(self, level):
        Map = Canvas(self.root, height = 550, width = 500, bg = 'black')
        Map.pack()
        Map.create_line(0,525,500,525, width = 50, fill = 'brown')
        Map.create_text(25, 475, text = 'i', fill = 'yellow', font = 'Times 50 bold')
        #Map.create_text(10,-170, text = '.', fill = 'yellow', font = 'Times 500 bold')
        self.game.loadLevel()
        return(Map)
        
    #creates the character
    def createFloater(self, color):
        floater = self.game.locatePlayer()
        x = (((floater // 10) * 50) + 25)
        if color == 'yellow':
            y = 475 - ((floater % 10) * 50)
            if self.game.getHover():
                if self.game.getBlue():
                    self.Map.create_text(x, y-1, text = '0', fill = 'blue', font = 'Times 53 bold')
                    self.Map.create_text(x, y-1, text = 'l', fill = 'blue', font = 'Times 55 bold')
                else:
                    self.Map.create_text(x+1, y, text = '0', fill = 'gray', font = 'Times 50 bold')
                    self.Map.create_text(x, y, text = 'l', fill = 'gray', font = 'Times 50 bold')
            self.Map.create_text(x, y, text = 'i', fill = color, font = 'Times 50 bold')
        elif color == 'black':
            y = 382 - ((floater % 10) * 50)
            self.Map.create_line((floater//10)*50,525-(((floater%10)*50)+50),((floater//10)*50)+50,525-(((floater%10)*50)+50), width = 50, fill = color)
            self.createObjects()
            
    #moves the character
    def moveFloater(self, event):
        move = event.keysym
        self.Map.delete(ALL)
        self.Map.create_line(0,525,500,525, width = 50, fill = 'brown')
        self.ham = False
        #manages going to the next level
        if self.game.getWin():
            self.createNextLevel()
        elif self.game.getDead():
            self.game.changeLevel(-1)
            self.createNextLevel()
        #manages the input and what happens and shit
        if move == 'Left':
            self.createFloater('black')
            if self.game.getWin() == False and self.game.getDead() == False:
                self.game.moveLeft()
            self.createFloater('yellow')
        elif move == 'Right':
            self.createFloater('black')
            if self.game.getWin() == False and self.game.getDead() == False:
                self.game.moveRight()
            self.createFloater('yellow')
        elif move == 'Up' and self.game.enterDoor():
            self.createFloater('black')
            self.Map.create_text(250, 250, text = '*Success!*', fill = 'white', font = 'Times 50 bold')
            self.Map.create_text(250, 295, text = 'Press any key to continue!', fill = 'white', font = 'Times 25 bold')
            self.ham = True
        elif move == 'space':
            self.createFloater('black')
            if self.game.getWin() == False and self.game.getDead() == False:
                self.game.jump()
            self.createFloater('yellow')
        elif move == 'F12':
            self.game.winGame()
        else:
            self.createFloater('black')
            self.createFloater('yellow')
        if self.ham == False:
            #draws the floors/walls
            for floor in self.game.getFloors():
                self.Map.create_line((floor//10)*50,550-(((floor%10)*50)+50),((floor//10)*50)+50,550-(((floor%10)*50)+50), width = 5, fill = 'brown')
            for wall in self.game.getWalls():
                self.Map.create_line((wall//10)*50,550-(((wall%10)*50)+50),(wall//10)*50,500-(((wall%10)*50)+50), width = 5, fill = 'brown')
            #draws blue floors
            for bounce_pad in self.game.getBouncePads():
                self.Map.create_line((bounce_pad//10)*50,550-(((bounce_pad%10)*50)+50),((bounce_pad//10)*50)+50,550-(((bounce_pad%10)*50)+50), width = 5, fill = 'blue')
            #changes switch walls
            for wall in self.game.getSwitchWalls():
                if 700 <= wall < 800:
                    pos = wall - 700
                    if self.game.getSwitchValue() == 'green':
                        self.Map.create_line((pos//10)*50,550-(((pos%10)*50)+50),(pos//10)*50,500-(((pos%10)*50)+50), width = 5, fill = 'green')
                    else:
                        self.Map.create_line((pos//10)*50,550-(((pos%10)*50)+50)-42,(pos//10)*50,500-(((pos%10)*50)+50), width = 3, fill = 'green')
                elif 800 <= wall < 900:
                    pos = wall - 800
                    if self.game.getSwitchValue() == 'red':
                        self.Map.create_line((pos//10)*50,550-(((pos%10)*50)+50),(pos//10)*50,500-(((pos%10)*50)+50), width = 5, fill = 'red')
                    else:
                        self.Map.create_line((pos//10)*50,550-(((pos%10)*50)+50)-42,(pos//10)*50,500-(((pos%10)*50)+50), width = 3, fill = 'red')
            #changes switch floors
            for floor in self.game.getSwitchFloors():
                if 900 <= floor < 1000:
                    pos = floor - 900
                    if self.game.getSwitchValue() == 'green':
                        self.Map.create_line((pos//10)*50,550-(((pos%10)*50)+50),((pos//10)*50)+50,550-(((pos%10)*50)+50), width = 5, fill = 'green')
                    else:
                        self.Map.create_line((pos//10)*50 + 42,550-(((pos%10)*50)+50),((pos//10)*50)+50,550-(((pos%10)*50)+50), width = 3, fill = 'green')
                elif 1000 <= floor < 1100:
                    pos = floor - 1000
                    if self.game.getSwitchValue() == 'red':
                        self.Map.create_line((pos//10)*50,550-(((pos%10)*50)+50),((pos//10)*50)+50,550-(((pos%10)*50)+50), width = 5, fill = 'red')
                    else:
                        self.Map.create_line((pos//10)*50 + 42,550-(((pos%10)*50)+50),((pos//10)*50)+50,550-(((pos%10)*50)+50), width = 3, fill = 'red')
            #sets up the directions in the first level
            if self.game.getLevel() == 0:
                if self.game.getWin() == False:
                    self.Map.create_text(250, 50, text = '*Directions*', fill = 'white', font = 'Times 50 bold')
                    self.Map.create_text(250, 100, text = 'Use the left and right directional arrows to move around.', fill = 'white', font = 'Times 15 bold')
                    self.Map.create_text(218, 140, text = 'Use spacebar to jump and float, and again to fall.', fill = 'white', font = 'Times 15 bold')
                    self.Map.create_text(229, 180, text = 'Your goal in each level is to reach the green portal.', fill = 'white', font = 'Times 15 bold')
                    self.Map.create_text(233, 220, text = 'Reach the portal and press the up-arrow to enter it!', fill = 'white', font = 'Times 15 bold')
                #if int(self.game.getLevel()) / 10 == int(self.game.getLevel()) // 10:
            if self.game.getLevel() == 10:
                if self.game.locatePlayer() == 51:
                    self.Map.create_line(23, 145, 397, 145, width = 103, fill = 'white')
                    self.Map.create_line(23, 93, 397, 93, width = 2, fill = 'red')
                    self.Map.create_line(23, 197, 397, 197, width = 2, fill = 'red')
                    self.Map.create_line(23, 93, 23, 197, width = 2, fill = 'red')
                    self.Map.create_line(397, 93, 397, 197, width = 2, fill = 'red')
                    self.Map.create_text(30, 108, anchor = W, text = 'You are faced with a dragon.', fill = 'black', font = 'Times 15 bold')
                    self.Map.create_text(30, 143, anchor = W, text = 'If you fight it unarmed, you', fill = 'black', font = 'Times 15 bold')
                    self.Map.create_text(30, 178, anchor = W, text = 'will surely die.', fill = 'black', font = 'Times 15 bold')
                if self.game.locatePlayer() == 9:
                    self.Map.create_line(23, 145, 397, 145, width = 103, fill = 'white')
                    self.Map.create_line(23, 93, 397, 93, width = 2, fill = 'red')
                    self.Map.create_line(23, 197, 397, 197, width = 2, fill = 'red')
                    self.Map.create_line(23, 93, 23, 197, width = 2, fill = 'red')
                    self.Map.create_line(397, 93, 397, 197, width = 2, fill = 'red')
                    self.Map.create_text(30, 108, anchor = W, text = 'Congratulations!', fill = 'black', font = 'Times 15 bold')
                    self.Map.create_text(30, 143, anchor = W, text = 'You have obtained a sword!', fill = 'black', font = 'Times 15 bold')
            if self.game.getLevel() == 11:
                self.Map.create_text(250, 50, text = 'YOU are a', fill = 'white', font = 'Times 25 bold')
                self.Map.create_text(250, 100, text = '*FLOATING MASTER!*', fill = 'white', font = 'Times 33 bold')
                self.Map.create_text(250, 155, text = 'Congratulations!', fill = 'white', font = 'Times 39 bold')
                self.Map.create_text(500, 550, anchor = SE, text = 'An Evan Gottschalk production~', fill = 'white', font = 'Comic 15 bold')
            #draws the sword
            for sword in self.game.getSwords():
                self.Map.create_line((sword//10)*50 + 15,550-(((sword%10)*50)+50)-15,((sword//10)*50)+50 - 15,550-(((sword%10)*50)+50)-15, width = 5, fill = 'white')
                self.Map.create_line((sword//10)*50 + 25,550-(((sword%10)*50)+50),(sword//10)*50 + 25,500-(((sword%10)*50)+50), width = 5, fill = 'white')
            if self.game.getDead():
                self.createFloater('black')
                self.Map.create_text(250, 250, text = '*You died!*', fill = 'white', font = 'Times 50 bold')
                self.Map.create_text(250, 295, text = 'Press any key to continue!', fill = 'white', font = 'Times 25 bold')
            if 'sword' in self.game.getWeapons():
                self.Map.create_line(15,550-15,50 - 15,550-15, width = 5, fill = 'white')
                self.Map.create_line(25,505,25,550, width = 5, fill = 'white')
            if self.game.locatePlayer() == 71:
                if self.game.getDead() == False:
                    if self.game.getLevel() == 10:
                        self.Map.create_text(250, 250, text = '*Success!*', fill = 'white', font = 'Times 50 bold')
                        self.Map.create_text(250, 295, text = 'You slew the dragon!', fill = 'white', font = 'Times 25 bold')
            #draws the dragon
            self.photo = PhotoImage(file = 'DragonBlock.gif')
            for dragon in self.game.getDragons():
                self.Map.create_image(dragon//10 * 50 + 25, 500 - dragon%10 * 50 - 25, image = self.photo)

                    
    #creates levels after level 1
    def createNextLevel(self):
        self.Map.delete(ALL)
        self.root.title('Floater - Level '+str(self.game.getLevel()+1))
        self.Map.create_line(0, 250, 500, 250, width = 500, fill = 'black')
        self.Map.create_line(0,525,500,525, width = 50, fill = 'brown')
        #self.Map.create_text(25, 475, text = 'i', fill = 'yellow', font = 'Times 50 bold')
        level = self.game.initializeLevel()
        self.game.loadLevel()
        self.createObjects()
        floater = self.game.locatePlayer()
        self.Map.create_text(((floater // 10) * 50) + 25, 475 - ((floater % 10) * 50), text = 'i', fill = 'yellow', font = 'Times 50 bold')
        
    #prints the coordinates of each square on the map
    def printCoordinates(self, Map):
        grid = self.game.getMap()
        for row in grid:
            for num in row:
                Map.create_text(((num//10)*50)+25, 475-((num%10)*50), text = str(num), fill = 'white', font = 'Times 30 bold')

    def createObjects(self):
        for block in self.game.getBlocks():
            self.Map.create_line((block//10)*50,525-(((block%10)*50)+50),((block//10)*50)+50,525-(((block%10)*50)+50), width = 50, fill = 'brown')
        for door in self.game.getDoors():
            self.Map.create_text((door//10)*50 + 25, 440 -(((door%10)*50)+50), text = '.', fill = 'green', font = 'Times 235 bold')            
        for bounce_pad in self.game.getBouncePads():
            self.Map.create_line((bounce_pad//10)*50,550-(((bounce_pad%10)*50)+50),((bounce_pad//10)*50)+50,550-(((bounce_pad%10)*50)+50), width = 5, fill = 'blue')
        for blue_star in self.game.getBlueStars():
            self.Map.create_text((blue_star//10)*50 + 25, 535 -(((blue_star%10)*50)+50), text = '*', fill = 'blue', font = 'Times 70 bold')
        for switch in self.game.getSwitch():
            self.Map.create_text((switch//10)*50 + 11, 535 -(((switch%10)*50)+50) - 40, text = '.', fill = 'green', font = 'Times 70 bold')
            self.Map.create_text((switch//10)*50 + 36, 535 -(((switch%10)*50)+50) - 40, text = '.', fill = 'red', font = 'Times 70 bold')
        #draws the dragon
        for dragon in self.game.getDragons():
            photo = PhotoImage(file = 'DragonBlock.gif')
            self.Map.create_image(dragon//10 * 50 + 25, 500 - dragon%10 * 50 - 25, image = photo)
        #draws the sword
        for sword in self.game.getSwords():
            self.Map.create_line((sword//10)*50 + 15,550-(((sword%10)*50)+50)-15,((sword//10)*50)+50 - 15,550-(((sword%10)*50)+50)-15, width = 5, fill = 'white')
            self.Map.create_line((sword//10)*50 + 25,550-(((sword%10)*50)+50),(sword//10)*50 + 25,500-(((sword%10)*50)+50), width = 5, fill = 'white')
        #sets up the directions in the first level
        if self.game.getLevel() == 0:
            if self.game.getWin() == False:
                self.Map.create_text(250, 50, text = '*Directions*', fill = 'white', font = 'Times 50 bold')
                self.Map.create_text(250, 100, text = 'Use the left and right directional arrows to move around.', fill = 'white', font = 'Times 15 bold')
                self.Map.create_text(218, 140, text = 'Use spacebar to jump and float, and again to fall.', fill = 'white', font = 'Times 15 bold')
                self.Map.create_text(229, 180, text = 'Your goal in each level is to reach the green portal.', fill = 'white', font = 'Times 15 bold')
                self.Map.create_text(233, 220, text = 'Reach the portal and press the up-arrow to enter it!', fill = 'white', font = 'Times 15 bold')

FloaterCanvas()
