from PIL import Image
from sys import argv
from random import randrange, sample
import random
from subprocess import call
import os


out_name=argv[1]

f=random.choice(os.listdir('gallery'))
src=os.path.join('gallery', f)
size=(randrange(30, 1024), randrange(30, 768))
Image.open(src).resize(size, Image.ANTIALIAS).save(out_name)

words = []
with file('words.txt') as f:
    words = f.read().split()

def gibberish(n):
   return ' '.join(sample(words, n))

def tags(n):
    return gibberish(n).replace(' ', ',')

def lucky():
    return random.choice([True, False])

tags=[
    '-Headline=%s' % gibberish(3),
    '-Caption-Abstract=%s' % gibberish(15),
    '-Credit=%s' % gibberish(2),
    '-SubjectReference=thismustbe13charsormore %s' % gibberish(2),
    '-ExifImageHeight=666',
    '-ExifImageWidth=321',
    '-Keywords=%s' % tags(3)
]
tags = [t for t in tags if lucky()]


call(['exiftool', '-overwrite_original', out_name] + tags)
