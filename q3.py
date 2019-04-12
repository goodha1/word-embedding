#!/usr/bin/env python
import distsim

word_to_ccdict = distsim.load_contexts("nytcounts.4k")


### provide your answer below


###Answer examples; replace with your choices
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['florida'],set(['florida']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['teachers'],set(['teachers']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['single'],set(['single']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['buy'],set(['buy']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['week'],set(['week']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['china'],set(['china']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))