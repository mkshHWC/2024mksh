# p15_wavy_square02_if_odd_fill_255_flii_0
size(550,550)
for y in range(11):
    for x in range(11):
        if (x+y)%2==1: fill(255) #白色 1,3,5...黑
        else: fill(0) #黑色 2,4,6...白
        
        rect(x*50,y*50,50,50)
        
        if (x+y)%2==1: fill(0)
        else: fill(255)
        
        rect(x*50+5,y*50+5,10,10)
        rect(x*50+35,y*50+35,10,10)
