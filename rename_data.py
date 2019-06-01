import os

i = 0
for filename in os.listdir('data/'):
    src = 'data/' + filename
    dest = 'data/' + str(i) + '.png'
    os.rename(src, dest)
    i += 1
