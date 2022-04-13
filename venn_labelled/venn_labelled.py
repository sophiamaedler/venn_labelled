import math, itertools
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3
import numpy as np

## based on code from https://stackoverflow.com/questions/42855256/python-venn-diagram-how-to-show-the-diagram-contents

# Generate list index for itertools combinations
def gen_index(n):
    x = -1
    while True:       
        while True:
            x = x + 1
            if bin(x).count('1') == n:
                break
        yield x

# Generate all combinations of intersections
def make_intersections(sets):
    l = [None] * 2**len(sets)
    for i in range(1, len(sets) + 1):
        ind = gen_index(i)
        for subset in itertools.combinations(sets, i):
            inter = set.intersection(*subset)
            l[next(ind)] = inter
    return l

# Get weird reversed binary string id for venn
def number2venn_id(x, n_fill):
    id = bin(x)[2:].zfill(n_fill)
    id = id[::-1]
    return id

# Iterate over all combinations and remove duplicates from intersections with
# more sets
def sets2dict(sets):
    l = make_intersections(sets)
    d = {}
    for i in range(1, len(l)):
        d[number2venn_id(i, len(sets))] = l[i]
        for j in range(1, len(l)):
            if bin(j).count('1') < bin(i).count('1'):
                l[j] = l[j] - l[i]
                d[number2venn_id(j, len(sets))] = l[j] - l[i]
    return d

def venn2_labels(list_sets, labels):
    # Plot it
    f = plt.figure(figsize = (10, 10))
    d = sets2dict(list_sets)

    h = venn2(list_sets, labels)
    for k, v in d.items():
        l = h.get_label_by_id(k)
        if l:
            l.set_fontsize(12)
            l.set_text('\n'.join(sorted(v)))
    return(f)

def venn3_labels(list_sets, labels):
    # Plot it
    f = plt.figure(figsize = (10, 10))
    d = sets2dict(list_sets)

    h = venn3(list_sets, labels)
    for k, v in d.items():
        l = h.get_label_by_id(k)
        if l:
            l.set_fontsize(12)
            l.set_text('\n'.join(sorted(v)))
    return(f)