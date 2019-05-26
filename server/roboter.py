import random


class Obsticle():
    def __init__(self, canvas):
        self.canvas = canvas
        self.circle = None

        self.xStart = 0
        self.yStart = 0
        self.farbe = "red"
        self.durchmesser = 10

    def setStartPosition(self, x, y):
        self.xStart = x
        self.yStart = y

    def display(self):
        coord = [self.xStart, self.yStart, self.xStart + self.durchmesser, self.yStart + self.durchmesser]
        self.circle = self.canvas.create_oval(coord, fill=self.farbe)

class Roboter(Obsticle):
    def __init__(self, canvas):
        super().__init__(canvas)
        # für die Animation:
        self.moveX = 0
        self.moveX = 0
        self.newCounter = 100
        self.counter = 100
        self.wait = 50
        self.isMoving = False

    def setStartPosition(self, x, y, row, column):
        self.xStart = x
        self.yStart = y
        self.row = row
        self.column = column

    def display(self):
        coord = [self.xStart, self.yStart, self.xStart + self.durchmesser, self.yStart + self.durchmesser]
        self.circle = self.canvas.create_oval(coord, fill=self.farbe)
        

    def moveToPosition(self, newX, newY, loops):

        self.fmoveX = newX
        self.fmoveY = newY

        if not self.isMoving:
            self.isMoving = True

            # ermittle die aktuelle x- und y-Koordinate des Balls
            coordinates = self.canvas.coords(self.circle)
            x = coordinates[0]
            y = coordinates[1]

            # abhängig von der gewählten Geschwindigkeit wird die Anzahl der Durchläufe und die X- und Y-Änderung nach jedem Durchgang berechnet
            self.counter = loops
            self.moveX = int((newX - x) / loops)
            self.moveY = int((newY - y) / loops)

            self.__move()           # starte die Animation

    # diese Methode wird solange selbst aufgerufen, bis die Animation beendet ist
    def __move(self):

        self.canvas.move(self.circle, self.moveX, self.moveY)
        self.canvas.update()

        # falls noch nicht alle Durchläufe absolviert wurden, soll die Methode erneut ausgeführt werden.
        if self.counter >= 0:
            self.counter = self.counter -1
            self.canvas.after(self.wait, self.__move)   # wichtig, damit andere Elemente der GUI während der Animation auch noch angesprochen werden können!!!
        else:
            self.isMoving = False
            # final move after int isnt precise
            coordinates = self.canvas.coords(self.circle)
            x = coordinates[0]
            y = coordinates[1]
            self.canvas.move(self.circle, self.fmoveX-x, self.fmoveY-y) 
            self.canvas.update()
            self.canvas.after(self.wait, self.moveNext) # die Methode moveNext() kann überschrieben werden und wird aufgerufen, wenn die bisherige Animation beendet wurde

    def moveNext(self):
        pass