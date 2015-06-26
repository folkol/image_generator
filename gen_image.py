from PIL import Image
from sys import argv
from random import randrange
import random
from subprocess import call
import os


def gibberish(n):
   return ' '.join(random.sample(words, n))

def csv(n):
    return gibberish(n).replace(' ', ',')

def lucky():
    return random.choice([True, False])

f=random.choice(os.listdir('gallery'))
src=os.path.join('gallery', f)
img=Image.open(src)

if lucky():
    size=(randrange(30, 1024), randrange(30, 768))
    img=img.resize(size, Image.ANTIALIAS)

out_name=argv[1]
img.save(out_name)

words = []
with file('words.txt') as f:
    words = f.read().split()

tags=[
    '-Headline=%s' % gibberish(3),
    '-Caption-Abstract=%s' % gibberish(15),
    '-Credit=%s' % gibberish(2),
    '-SubjectReference=thismustbe13charsormore %s' % gibberish(2),
    '-ExifImageHeight=666',
    '-ExifImageWidth=321',
    '-Keywords=%s' % csv(3),
    '-Country-PrimaryLocationName=%s' % csv(3),
    '-Sub-Location=%s' % csv(3),
    '-Organization=%s' % csv(2)
]
tags = [t for t in tags if lucky()]

call(['exiftool', '-overwrite_original', out_name] + tags)
