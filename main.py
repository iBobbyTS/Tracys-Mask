from sys import argv
import os
from threading import Thread

from psutil import cpu_count
from PIL import Image
import numpy


def process():
    while files:
        f = files.pop(0)
        img = Image.open(os.path.join(path, f))
        img = numpy.asarray(img) * mask
        img = Image.fromarray(img)
        img.save(os.path.join(new_path, f.lower()))
        print(f)


path = argv[1]

mask = Image.open(os.path.join(path, 'mask.png'))
mask = numpy.asarray(mask)
mask = mask[:, :, 3]
mask = mask.astype(numpy.float128)
mask /= 255.0
mask = mask.round()
mask -= 1
mask *= -1
mask = mask.astype(numpy.uint8)
mask = numpy.stack([mask] * 4, 2)
print('mask')

files = os.listdir(path)
files.sort()
files.remove('mask.png')
files = [f for f in files if f.endswith('.png')]
new_path = path + '_masked'
os.mkdir(new_path)
threads = []
for t in range(cpu_count()):
    threads.append(Thread(target=process))
    threads[-1].start()
for t in threads:
    t.join()
print('Done!')
