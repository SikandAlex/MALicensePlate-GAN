from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
import string

SAMPLES = 250

def getRandom3():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))

def getPlates():
    for i in range(SAMPLES):
        s1 = getRandom3()
        s2 = getRandom3()
        s_comb = s1 + " " + s2
        img = Image.open("../images/mass_plate_template.bmp")
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("../font/ma2.ttf", 124)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((30, 30),s_comb,(160,44,36),font=font)
        img = img.resize((192,96))
        img.save('../GeneratedPlateSamples/sample-out' + "-" + str(i) + '.png')

getPlates()
