import os
import photos
from PIL import Image
import numpy

mask_asset = photos.pick_asset(title='Select the mask')
layers_asset = photos.pick_asset(title='Select the rest', multi=True)

print('Processing mask', end='')
mask = mask_asset.get_image()
mask = numpy.asarray(mask)
mask = mask[:, :, 3]
mask = mask.astype(numpy.float32)
mask /= 255.0
mask = mask.round()
mask -= 1
mask *= -1
mask = mask.astype(numpy.uint8)
mask = numpy.stack([mask] * 4, 2)

count = 1
for layer in layers_asset:
    print(f'\rProcessing layer{count}', end='', flush=True)
    layer = layer.get_image()
    layer = numpy.asarray(layer) * mask
    layer = Image.fromarray(layer)
    layer.save('tmp.png')
    photos.create_image_asset('tmp.png')
    count += 1

os.remove('tmp.png')
photos.batch_delete(layers_asset+[mask_asset])
print('\rDone!', flush=True)
