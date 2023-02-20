from PIL import Image 
import sys

def concealImg(imgPath, concealmentImgPath):
    
    buf = ""
    with open(concealmentImgPath,'rb') as f:
        buf = f.read()

    temp = ""
    for i in range(len(buf)):
        t = bin(buf[i])[2:].zfill(8)
        temp = temp + t 

    temp = list(temp)

    img = Image.open(imgPath)

    w, h = img.size
    k = 0 
    nImg = Image.new('RGB',img.size,'#fff')
    i = nImg.load()
    for y in range(0, h):
        for x in range(0, w):
            p = img.getpixel((x,y))
            r,g,b = p

            if k<len(temp):
                t = (g&1) ^ int(temp[k])
                p = r&-2
                p = p | t
                r = p
                
            k = k+1
            if k<len(temp):
                t = (g&1) ^ int(temp[k])
                p = b&-2
                p = p | t 
                b = p
            
            k = k+1        
            
            p = (r,g,b)
            nImg.putpixel((x,y),p)


    nImg.save("./result.png")

def usage():
	print("syntax : steganography.py <Image path> <File path>")
	print("sample : steganography.py ./cat.jpg ./flag.ext")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        exit()

    print(sys.argv[1])
    imgPath = sys.argv[1]
    concealmentImgPath = sys.argv[2]
    concealImg(imgPath, concealmentImgPath)

