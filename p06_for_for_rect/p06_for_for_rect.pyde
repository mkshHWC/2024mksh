# p06_for_for_rect
# 在600*600中,放10*10共100格
size(600,600)
background(127,183,79) #背景色
for x in range(10):
    for y in range(10):
        fill(250,149,225) #給方格塗色
        rect(x*60+2,y*60+2,55,55)
# 打:後電腦給的的空格最標準
