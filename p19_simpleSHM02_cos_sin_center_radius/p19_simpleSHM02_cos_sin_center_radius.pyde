# p19_simpleSHM02_cos_sin_center_radius
def setup():
    size(600,600)
def draw():
    background(255)
    noFill() #空心的大園
    ellipse(150,150,200,200)
    fill(0) #實心的小圓
    a = frameCount * PI/360
    ellipse(150+100*cos(a),150+100*sin(a),8,8)