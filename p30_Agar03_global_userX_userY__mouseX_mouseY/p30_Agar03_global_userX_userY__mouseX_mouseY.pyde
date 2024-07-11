# p30_Agar03_global_userX_userY__mouseX_mouseY
def setup():
    size(1000,1000)
userX, userY = 200.0, 200.0 #要用小數點才精確
def draw():
    global userX, userY
    background(230,235,238)
    stroke(205,216,221)
    for x in range(0,1000,50):
        line(x, 0, x, 1000)
    for y in range(0,1000,50):
        line(0, y, 1000, y)
    fill(255,165,7)
    ellipse(userX, userY,100,100)
    fill(142,232,47)
    ellipse(100,100,60,60)
    userX = (mouseX+userX*19)/20
    userY = (mouseY+userY*19)/20
