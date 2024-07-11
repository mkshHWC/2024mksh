# p35_Osu02_global_t_cSize_ellipse
# 目標:做出漸進環並逐漸收縮
t = 200
def setup():
    size(500, 400)
def draw():
    background(0)
    stroke(92, 0, 0)
    strokeWeight(6)
    noFill()
    global t
    cSize = t #circleSize圈圈大小
    t -= 2 #縮小速度
    if t<=40: t=200 #縮到40就反彈
    #cSize = dist(mouseX, mouseY, 250, 200)*2 #隨滑鼠距離移動
    ellipse(250, 200, cSize, cSize)
    fill(193, 33, 33)
    ellipse(250, 200, 40, 40)
