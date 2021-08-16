class Floater:

    def __init__(self):
        self.__map = [[9,19,29,39,49,59,69,79,89,99],\
                      [8,18,28,38,48,58,68,78,88,98],\
                      [7,17,27,37,47,57,67,77,87,97],\
                      [6,16,26,36,46,56,66,76,86,96],\
                      [5,15,25,35,45,55,65,75,85,95],\
                      [4,14,24,34,44,54,64,74,84,94],\
                      [3,13,23,33,43,53,63,73,83,93],\
                      [2,12,22,32,42,52,62,72,82,92],\
                      [1,11,21,31,41,51,61,71,81,91],\
                      [0,10,20,30,40,50,60,70,80,90]]
        self.__player = 0
        self.__level = 0
        self.__win = False
        self.__block = []
        self.__hover = False
        self.__door = []
        self.__wall = []
        self.__floor = []
        self.__bounce_pad = []
        self.__blue = False
        self.__blue_star = []
        self.__switch = []
        self.__switch_wall = []
        self.__switch_floor = []
        self.__switch_value = 'green'
        self.__dragon = []
        self.__sword = []
        self.__weapons = []
        self.__dead = False

#Greg
### "Star power" such that one can move around freely in the air, using the
### arrow keys. Potentially have it be represented by a number, that being
### the number of moves it lasts for.

#Lisa
### Enemy mirrors you/moves in response to you.
#Bart: "Damaging ground"/spikes present. Must walk enemy into them.

#Bart
### Switch that rotates level 90/180 degrees.

    #accessor methods
    def getWin(self):
        return self.__win

    def getLevel(self):
        return self.__level

    def locatePlayer(self):
        return self.__player

    def getBlocks(self):
        return self.__block

    def getDoors(self):
        return self.__door

    def getHover(self):
        return self.__hover

    def getMap(self):
        return self.__map

    def getWalls(self):
        return self.__wall

    def getFloors(self):
        return self.__floor

    def getBouncePads(self):
        return self.__bounce_pad

    def getBlue(self):
        return self.__blue

    def getBlueStars(self):
        return self.__blue_star

    def getSwitch(self):
        return self.__switch

    def getSwitchWalls(self):
        return self.__switch_wall

    def getSwitchFloors(self):
        return self.__switch_floor
    
    def getSwitchValue(self):
        return self.__switch_value

    def getDragons(self):
        return self.__dragon

    def getSwords(self):
        return self.__sword

    def getWeapons(self):
        return self.__weapons

    def getDead(self):
        return self.__dead
    
    #mutator methods
    def moveRight(self):
        #does the moving
        if not(self.__player+10 in self.__block or self.__player+10>99 or self.__player+10 in self.__wall):
            self.__player+=10
            #checks for being in a switch
            if self.__player in self.__switch:
                if self.__switch_value == 'green':
                    self.__switch_value = 'red'
                    for wall in self.__switch_wall:
                        if 700 <= wall < 800:
                            self.__wall.remove(wall - 700)
                        elif wall >= 800:
                            self.__wall.append(wall - 800)
                    for floor in self.__switch_floor:
                        if 900 <= floor < 1000:
                            self.__floor.remove(floor - 900)
                        elif 1000 <= floor < 1100:
                            self.__floor.append(floor - 1000)
                else:
                    self.__switch_value = 'green'
                    for wall in self.__switch_wall:
                        if 700 <= wall < 800:
                            self.__wall.append(wall - 700)
                        elif wall >= 800:
                            self.__wall.remove(wall - 800)
                    for floor in self.__switch_floor:
                        if 900 <= floor < 1000:
                            self.__floor.append(floor - 900)
                        elif 1000 <= floor < 1100:
                            self.__floor.remove(floor - 1000)
        #checks hover status
        if self.__player-1 in self.__block or self.__player in self.__floor or self.__player in self.__bounce_pad:
            self.__hover = False
        if self.__hover == False:
            while not(self.__player - 1 in self.__block) and not(self.__player%10 == 0) and not(self.__player in self.__floor) and not(self.__player in self.__bounce_pad):
                self.__player-=1
                #checks for being in a switch
                if self.__player in self.__switch:
                    if self.__switch_value == 'green':
                        self.__switch_value = 'red'
                        for wall in self.__switch_wall:
                            if 700 <= wall < 800:
                                self.__wall.remove(wall - 700)
                            elif wall >= 800:
                                self.__wall.append(wall - 800)
                        for floor in self.__switch_floor:
                            if 900 <= floor < 1000:
                                self.__floor.remove(floor - 900)
                            elif 1000 <= floor < 1100:
                                self.__floor.append(floor - 1000)
                    else:
                        self.__switch_value = 'green'
                        for wall in self.__switch_wall:
                            if 700 <= wall < 800:
                                self.__wall.append(wall - 700)
                            elif wall >= 800:
                                self.__wall.remove(wall - 800)
                        for floor in self.__switch_floor:
                            if 900 <= floor < 1000:
                                self.__floor.append(floor - 900)
                            elif 1000 <= floor < 1100:
                                self.__floor.remove(floor - 1000)
        #checks blue
        if self.__blue == True:
            if self.__player%10 == 0 or self.__player-1 in self.__block or self.__player in self.__floor or self.__player in self.__bounce_pad:
                self.__bounce_pad.append(self.__player)
                self.__blue = False
        if self.__player in self.__blue_star:
            self.__blue = True
        #checks for being eaten
        if self.__player in self.__dragon:
            if 'sword' in self.__weapons:
                self.__dragon.remove(self.__player)
                self.__weapons.remove('sword')
            else:
                self.__dead = True
        #checks for the sword
        if self.__player in self.__sword:
            self.__weapons.append('sword')
            self.__sword.remove(self.__player)
        if self.__hover == False:
            while not(self.__player - 1 in self.__block) and not(self.__player%10 == 0) and not(self.__player in self.__floor) and not(self.__player in self.__bounce_pad):
                self.__player-=1
        
    def moveLeft(self):
        #moves you
        if not(self.__player-10 in self.__block) and not(self.__player-10<0) and not(self.__player in self.__wall):
            self.__player-=10
            #checks for being in a switch
            if self.__player in self.__switch:
                if self.__switch_value == 'green':
                    self.__switch_value = 'red'
                    for wall in self.__switch_wall:
                        if 700 <= wall < 800:
                            self.__wall.remove(wall - 700)
                        elif wall >= 800:
                            self.__wall.append(wall - 800)
                    for floor in self.__switch_floor:
                        if 900 <= floor < 1000:
                            self.__floor.remove(floor - 900)
                        elif 1000 <= floor < 1100:
                            self.__floor.append(floor - 1000)
                else:
                    self.__switch_value = 'green'
                    for wall in self.__switch_wall:
                        if 700 <= wall < 800:
                            self.__wall.append(wall - 700)
                        elif wall >= 800:
                            self.__wall.remove(wall - 800)
                    for floor in self.__switch_floor:
                        if 900 <= floor < 1000:
                            self.__floor.append(floor - 900)
                        elif 1000 <= floor < 1100:
                            self.__floor.remove(floor - 1000)
        #checks the hover status
        if self.__player-1 in self.__block or self.__player in self.__floor or self.__player in self.__bounce_pad:
            self.__hover = False
        if self.__hover == False:
            while not(self.__player-1 in self.__block) and not(self.__player%10 == 0) and not(self.__player in self.__floor) and not(self.__player in self.__bounce_pad):
                self.__player-=1
                #checks for being in a switch
                if self.__player in self.__switch:
                    if self.__switch_value == 'green':
                        self.__switch_value = 'red'
                        for wall in self.__switch_wall:
                            if 700 <= wall < 800:
                                self.__wall.remove(wall - 700)
                            elif wall >= 800:
                                self.__wall.append(wall - 800)
                        for floor in self.__switch_floor:
                            if 900 <= floor < 1000:
                                self.__floor.remove(floor - 900)
                            elif 1000 <= floor < 1100:
                                self.__floor.append(floor - 1000)
                    else:
                        self.__switch_value = 'green'
                        for wall in self.__switch_wall:
                            if 700 <= wall < 800:
                                self.__wall.append(wall - 700)
                            elif wall >= 800:
                                self.__wall.remove(wall - 800)
                        for floor in self.__switch_floor:
                            if 900 <= floor < 1000:
                                self.__floor.append(floor - 900)
                            elif 1000 <= floor < 1100:
                                self.__floor.remove(floor - 1000)
        #checks blue
        if self.__blue == True:
            if self.__player%10 == 0 or self.__player-1 in self.__block or self.__player in self.__floor or self.__player in self.__bounce_pad:
                self.__bounce_pad.append(self.__player)
                self.__blue = False
        if self.__player in self.__blue_star:
            self.__blue = True
        #checks for being eaten
        if self.__player in self.__dragon:
            if 'sword' in self.__weapons:
                self.__dragon.remove(self.__player)
                self.__weapons.remove('sword')
            else:
                self.__dead = True
        #checks for the sword
        if self.__player in self.__sword:
            self.__weapons.append('sword')
            self.__sword.remove(self.__player)
        if self.__hover == False:
            while not(self.__player - 1 in self.__block) and not(self.__player%10 == 0) and not(self.__player in self.__floor) and not(self.__player in self.__bounce_pad):
                self.__player-=1

    def jump(self):
        move = False
        if self.__hover == False and not(self.__player + 1 in self.__block) and self.__player%10 != 9 and not(self.__player+1 in self.__floor):
            if self.__player in self.__bounce_pad:
                self.__player+=2
                move = True
            else:
                self.__player+=1
                move = True
            self.__hover = True
        else:
            self.__hover = False
            while not(self.__player - 1 in self.__block) and not(self.__player%10 == 0) and not(self.__player in self.__floor) and not(self.__player in self.__bounce_pad):
                self.__player-=1
                move = True
        #checks blue
        if self.__blue == True:
            if self.__player%10 == 0 or self.__player-1 in self.__block or self.__player in self.__floor or self.__player in self.__bounce_pad:
                self.__bounce_pad.append(self.__player)
                self.__blue = False
        if self.__player in self.__blue_star:
            self.__blue = True
        if move:
            #checks for being in a switch
            if self.__player in self.__switch:
                if self.__switch_value == 'green':
                    self.__switch_value = 'red'
                    for wall in self.__switch_wall:
                        if 700 <= wall < 800:
                            self.__wall.remove(wall - 700)
                        elif wall >= 800:
                            self.__wall.append(wall - 800)
                    for floor in self.__switch_floor:
                        if 900 <= floor < 1000:
                            self.__floor.remove(floor - 900)
                        elif 1000 <= floor < 1100:
                            self.__floor.append(floor - 1000)
                else:
                    self.__switch_value = 'green'
                    for wall in self.__switch_wall:
                        if 700 <= wall < 800:
                            self.__wall.append(wall - 700)
                        elif wall >= 800:
                            self.__wall.remove(wall - 800)
                    for floor in self.__switch_floor:
                        if 900 <= floor < 1000:
                            self.__floor.append(floor - 900)
                        elif 1000 <= floor < 1100:
                            self.__floor.remove(floor - 1000)
        #checks if a floor appeared beneath you
        if self.__player - 1 in self.__block or self.__player%10 == 0 or self.__player in self.__floor or self.__player in self.__bounce_pad:
            self.__hover = False
        #checks for being eaten
        if self.__player in self.__dragon:
            if 'sword' in self.__weapons:
                self.__dragon.remove(self.__player)
                self.__weapons.remove('sword')
            else:
                self.__dead = True
        #checks for the sword
        if self.__player in self.__sword:
            self.__weapons.append('sword')
            self.__sword.remove(self.__player)
        if self.__hover == False:
            while not(self.__player - 1 in self.__block) and not(self.__player%10 == 0) and not(self.__player in self.__floor) and not(self.__player in self.__bounce_pad):
                self.__player-=1

    def winGame(self):
        self.__win = True
            
    def enterDoor(self):
        if self.__player in self.__door:
            self.__win = True
        return(self.__win)

    def createBlock(self, position):
        self.__block.append(position)

    def createDoor(self, position):
        self.__door.append(position)

    def createWall(self, position):
        self.__wall.append(position)

    def createFloor(self, position):
        self.__floor.append(position)

    def createBouncePad(self, position):
        self.__bounce_pad.append(position)

    def createBlueStar(self, position):
        self.__blue_star.append(position)

    def createSwitch(self, position):
        self.__switch.append(position)

    def createSwitchWall(self, position):
        self.__switch_wall.append(position)
    
    def createSwitchFloor(self, position):
        self.__switch_floor.append(position)

    def createDragon(self, position):
        self.__dragon.append(position)

    def createSword(self, position):
        self.__sword.append(position)

    def changeLevel(self, value):
        self.__level += value
        
    def loadLevel(self):
        filename = 'Level '+str(self.__level)+'.txt'
        fileNotOpened = True
        while fileNotOpened:
            try:
                infile = open('levels/' + filename, 'r')
                fileNotOpened = False
            except:
                infile = open(filename, 'r')
                fileNotOpened = False                    
        line = infile.readline()
        self.__player = 0
        while line != '':
            if int(line) < 0:
                self.__player = abs(int(line))
            elif 0 <= int(line) < 100:
                self.createBlock(int(line))
            elif 100 <= int(line) < 200:
                self.createDoor(int(line)-100)
            elif 200 <= int(line) < 300:
                self.createWall(int(line)-200)
            elif 300 <= int(line) < 400:
                self.createFloor(int(line)-300)
            elif 400 <= int(line) < 500:
                self.createBouncePad(int(line)-400)
            elif 500 <= int(line) < 600:
                self.createBlueStar(int(line)-500)
            elif 600 <= int(line) < 700:
                self.createSwitch(int(line)-600)
            elif 700 <= int(line) < 900:
                self.createSwitchWall(int(line))
                if int(line) < 800:
                    self.createWall(int(line)-700)
            elif 900 <= int(line) < 1100:
                self.createSwitchFloor(int(line))
                if int(line) < 1000:
                    self.createFloor(int(line)-900)
            elif 1100 <= int(line) < 1200:
                self.createDragon(int(line) - 1100)
            elif 1200 <= int(line) < 1300:
                self.createSword(int(line) - 1200)
            line = infile.readline()

    def initializeLevel(self):
        self.__level+=1
        self.__win = False
        self.__door = []
        self.__block = []
        self.__wall = []
        self.__floor = []
        self.__bounce_pad = []
        self.__hover = False
        self.__blue_star = []
        self.__blue = False
        self.__switch = []
        self.__switch_wall = []
        self.__switch_floor = []
        self.__switch_value = 'green'
        self.__dragon = []
        self.__sword = []
        self.__weapons = []
        self.__dead = False

    def checkBlue(self):
        if self.__blue == True:
            if self.__player in self.__block or self.__player in self.__floor or self.__player in self.__bounce_pad:
                createBouncePad(self.__player)
                self.__blue = False
        if self.__player in self.__blue_star:
            self.__blue = True

    def __str__(self):
        mapString = ''
        for num in range(10):
            rowString = ('|  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |\n'\
                         % (self.__map[num][0], self.__map[num][1],\
                            self.__map[num][2], self.__map[num][3],\
                            self.__map[num][4], self.__map[num][5],\
                            self.__map[num][6], self.__map[num][7],\
                            self.__map[num][8], self.__map[num][9],))
            mapString+=rowString
        return(mapString)
