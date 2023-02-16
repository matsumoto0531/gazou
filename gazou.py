from PIL import Image
im = Image.open("aichan.png")
im.show()
rgb_im = im.convert('RGB')
size = rgb_im.size
im2 = Image.new('RGB',size,(0, 128, 255))

data = 0b0101001010100111

r0,g0,b0 = [25, 0, 40]
r1,g1,b1 = [39, 39, 39]

xcheck = 0
ycheck = 0
for x in range(size[0]):
    xcheck += 1
    for y in range(size[1]):
      if ycheck%64 == 0 and xcheck%40 == 0:
        a = data & 0b0000000000000001
        if a == 0b1:     
          im2.putpixel((x,y),(r1,g1,b1))
        else:
          im2.putpixel((x,y),(r0,g0,b0))
        data = data >> 1
      elif ycheck == 0:
        im2.putpixel((x, y),(r0,g0,b0))
      elif ycheck == 1:
        im2.putpixel((x, y),(r1,g1,b1))
      else:
        r, g, b = rgb_im.getpixel((x,y))
        im2.putpixel((x,y),(r,g,b))
      ycheck += 1

im2.show()
im2.save('test.png')

data2 = 0
r0,g0,b0 = im2.getpixel((0,0))
r1,g1,b1 = im2.getpixel((0,1))

x = 0
y = 0
for x in range(size[0]):
    for y in range(size[1]):
        r,g,b = im2.getpixel((x,y))
        if r == r1 and b == b1 and g == g1 and y != 1:
          data2 += 1
          data2 = data2 << 1
        elif g == g0 and b == b0 and r == r0 and y != 0:
          data2 = data2 << 1

print(bin(data2))