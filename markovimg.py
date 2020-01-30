#!/usr/bin/env python3
# Invoke like this: ./markovimg.py [YOURFILENAME]

from PIL import Image
import random
import sys


# Used only by run().
# Feel free to replace any function by your own; possibly by `generate.sample_colpoint = lambda ...`
CONTEXT = dict(
    w=400,
    h=300,
    prob_start=0.0,
    prob_end=1.0,
    img_type='L',
    img_col1=0,
    img_col2=255,
)


def generate_image(ctx):
    data = []
    cols = [ctx['img_col1'], ctx['img_col2']]
    for y in range(ctx['h']):
        state = bool(random.getrandbits(1))
        change_chance = ctx['prob_start'] + (ctx['prob_end'] - ctx['prob_start']) * y / (ctx['h'] - 1)
        for x in range(ctx['w']):
            data.append(cols[state])
            if random.random() < change_chance:
                state = not state
    img = Image.new(ctx['img_type'], (ctx['w'], ctx['h']))
    img.putdata(data)
    return img


def run_output(dst_filename):
    img = generate_image(CONTEXT)
    img.save(dst_filename)


def run():
    if len(sys.argv) == 1:
        import time
        filename = time.strftime('output_%s.png')
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print('USAGE: {} [OUTPUTFILENAME]'.format(sys.argv[0]), file=sys.stderr)
        exit(1)
    run_output(filename)


if __name__ == '__main__':
    run()
