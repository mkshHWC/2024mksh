# p36_Osu03_myStar_for_loop
t = 100
def myStar(x, y, t):
    cSize = t #circleSize圈圈大小
    noFill()
    ellipse(x, y, cSize, cSize)
    fill(193, 33, 33)
    ellipse(x, y, 40, 40)
x, y = [], []
def setup():
    size(500, 400)
    for i in range(30):
        x.append(random(500))
        y.append(random(400))
def draw():
    background(0)
    stroke(92, 0, 0)
    strokeWeight(6)
    global t
    t -= 2 #縮小速度 
    if t<=40: t=200 #縮到40就反彈
    for i in range(len(x)):
        myStar(x[i], y[i], t)
    
