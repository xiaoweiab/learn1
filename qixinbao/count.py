import PIL.Image as image
import win32
image1 = image.open('foo1.png')
image2 = image.open('foo2.png')
a =[]
for i in range(65,325):
    for j in range(0,145):
        pix1 = image1.getpixel((i,j))
        pix2 = image2.getpixel((i, j))
        for c in range(0,3):
            if abs(pix1[c]-pix2[c])>=50:
               if i not in a:
                   a.append(i)
# a.sort()
# print(a)
