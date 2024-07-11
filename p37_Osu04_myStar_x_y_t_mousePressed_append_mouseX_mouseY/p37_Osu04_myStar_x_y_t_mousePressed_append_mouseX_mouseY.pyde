# p37_Osu04_myStar_x_y_t_mousePressed_append_mouseX_mouseY
def myStar(x, y, t):
    cSize = t #circleSize圈圈大小
    noFill()
    ellipse(x, y, cSize, cSize)
    fill(193, 33, 33)
    ellipse(x, y, 40, 40)
x, y, t = [], [], []
def setup():
    size(500, 400)
def draw():
    background(0)
    stroke(92, 0, 0)
    strokeWeight(6)
    for i in range(len(x)):
        myStar(x[i], y[i], t[i])
        t[i] -= 2 #縮小速度 
        if t[i]<=40: t[i]=150 #縮到40就反彈
def mousePressed():
    x.append(mouseX)
    y.append(mouseY)
    t.append(150)
# 滑鼠點哪就出現在哪,每顆按鍵都有自己的縮圈時間
    
