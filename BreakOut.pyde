class Brick(object):
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.W = 40
        self.H = 10
        self.toDelete = 0 
        self.brickColors=["#7D11D6","#3B36FC","#FCF336","#FCAD36","#FC3639"]
        self.brickColor=self.brickColors[int(random(len(self.brickColors)))]
        
    def show(self):
        fill(self.brickColor)
        rect(self.x,self.y,self.W,self.H)

class Paddle(object):
    def __init__(self):
        self.x = mouseX
        self.y = 450
    def show(self):
        fill('#FFFFFF')
        rect(self.x,self.y,100,20) 
        
class Ball(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.Xspeed = -10
        self.Yspeed = -10
        
    def show(self):
        fill("#F22226")
        ellipse(self.x,self.y, 30,30)
        
    def move(self):
        self.x += self.Xspeed
        self.y += self.Yspeed
        
    def hit_paddle(self,paddleX):
        if (paddleX-50-20 <= self.x and paddleX+50+20>=self.x and self.y >= 430 and self.y <= 470):
            self.Yspeed *= -1 
            
    def hit_boundary(self):
        if self.x <= 15 or self.x>width-15:
            self.Xspeed *= -1
        if self.y <= 15 or self.y>height-15:
            self.Yspeed *= -1
            
def setup():
    size(920,500)
    global bricks, ball
    bricks = []
    global s,m
    s=second()
    m=minute()
    for i in range(3):
        for j in range(11):
            bricks.append(Brick(j*80+40,60*i+60))
    ball = Ball(width/2,450)
    background(51)
        
        
def draw():
    background(51)
    for brick in bricks:
        brick.show()
        
    paddle = Paddle()
    paddle.show()
    
    ball.show()
    ball.move()
    ball.hit_boundary()
    ball.hit_paddle(mouseX)
    
    for brick in bricks:
        if dist(brick.x,brick.y,ball.x,ball.y) < 35:
            brick.toDelete = 1
            ball.Yspeed *= -1
        if brick.toDelete == 1:
            bricks.remove(brick)
        
    if len(bricks) == 0:
        Stop()
        
        
        score = 33 - len(bricks)
        textSize(20)
        text("Score: " + str(score), width/2-50, 50)
        
        time_limit = 30
        text("Time Left: " + str(time_limit-((minute()*60+second())-(m*60+s))), width/2-50,30)
        
def Lose():
    noLoop()
    background(51)
    textAlign(CENTER)
    text("You ran out of time", width/2,height/2)
    
def Stop():
    noLoop()
    background(51)
    textAlign(CENTER)
    text("All Bricks Cleared", width/2,height/2)
    
