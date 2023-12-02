try:
    #Python2
    import Tkinter as tk
except ImportError:
    #Python3
    import tkinter as tk

class solarSystem:
    CANVAS_WIDTH = 800
    CANVAS_HEIGHT = 800
    
    #Moon starting values
    mPosX = 400.0
    mPosY = 100.0
    mRadius = 20
    mVelX = 30.0
    mVelY = 0.0

    #Planet starting values
    pPosX = 400.0
    pPosY = 400.0
    pRadius = 70
    pVelX = -6.0
    pVelY = 0.0

    #Fix animation rate, time in milliseconds
    STEP_TIME = 20

    
    def move_bodies(self):
        #Moon acceleration
        self.mVelX += (self.pPosX - self.mPosX) * .01
        self.mPosX += self.mVelX
        
        self.mVelY += (self.pPosY - self.mPosY) * .01
        self.mPosY += self.mVelY
    
        #Planet Acceleration
        self.pVelX += (self.mPosX - self.pPosX) * .002
        self.pPosX += self.pVelX
        
        self.pVelY += (self.mPosY - self.pPosY) * .002
        self.pPosY += self.pVelY

        #Move the image itself    
        self.canvas.move("moon", self.mVelX, self.mVelY)
        self.canvas.move("planet", self.pVelX, self.pVelY)

        """If you leave this code uncommented the planet and moon will teleport to the
        other side of the canvas causing some fun gravitational interactions"""
        #Loop the moon to the other side of the screen    
        if self.mPosX < 0:
            self.mPosX += self.CANVAS_WIDTH
            self.canvas.move("moon", self.CANVAS_WIDTH, 0)
        elif self.mPosX > self.CANVAS_WIDTH:
            self.mPosX -= self.CANVAS_WIDTH
            self.canvas.move("moon", 0 - self.CANVAS_WIDTH, 0)
        if self.mPosY < 0:
            self.mPosY += self.CANVAS_HEIGHT
            self.canvas.move("moon", 0, self.CANVAS_HEIGHT)
        elif self.mPosY > self.CANVAS_HEIGHT:
            self.mPosY -= self.CANVAS_HEIGHT
            self.canvas.move("moon", 0, 0 - self.CANVAS_WIDTH)
        #Loop the planet to the other side of the screen
        if self.pPosX < 0:
            self.pPosX += self.CANVAS_WIDTH
            self.canvas.move("planet", self.CANVAS_WIDTH, 0)
        elif self.pPosX > self.CANVAS_WIDTH:
            self.pPosX -= self.CANVAS_WIDTH
            self.canvas.move("planet", 0 - self.CANVAS_WIDTH, 0)
        if self.pPosY < 0:
            self.pPosY += self.CANVAS_HEIGHT
            self.canvas.move("planet", 0, self.CANVAS_HEIGHT)
        elif self.pPosY > self.CANVAS_HEIGHT:
             self.pPosY -= self.CANVAS_HEIGHT
             self.canvas.move("planet", 0, 0 - self.CANVAS_WIDTH)


        self.canvas.after(self.STEP_TIME, self.move_bodies)
   
    def circle(self, x, y, r, name, color = 'orange'):
        #Form a bounding square using center (x,y) and radius r
        #Upper left corner (ulc) and lower right corner (lrc) coordinates of square
        ulc = x-r, y-r
        lrc = x+r, y+r
        # give the circle a tag name for reference
        self.canvas.create_oval(ulc, lrc, tag=name, fill=color)

    def __init__(self):
        root = tk.Tk()
        root.title("Animated Circle")
        #Ulc position of rootwindow
        root.geometry("+{}+{}".format(150, 80))
    
        #Create a canvas to draw on 
        self.canvas = tk.Canvas(root, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, bg='lightblue')
        self.canvas.pack()
 
        self.circle(self.mPosX, self.mPosY, self.mRadius, 'moon', 'darkred')
        self.circle(self.pPosX, self.pPosY, self.pRadius, 'planet', 'darkblue')
 
        self.move_bodies()
 
        root.mainloop()

solarSystem()
