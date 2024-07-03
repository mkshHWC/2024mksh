# p08_two_image
size(640,427)
imgBG = loadImage('blue.jpg') # 用你的背景圖片的大小
image(imgBG,0,0)
img1 = loadImage('kitty.jpg') #找半透明的png圖
image(img1,10,250,100,150)
img1 = loadImage('kitty.png')
image(img1,500,300,100,100)
