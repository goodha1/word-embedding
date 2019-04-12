#!/usr/bin/env python
import distsim
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
###Provide your answer below

###Answer examples; replace with your choices

for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['florida'],set(['florida']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i+1, word, score))
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['teachers'],set(['teachers']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i+1, word, score))
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['single'],set(['single']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i+1, word, score))
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['buy'],set(['buy']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i+1, word, score))
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['week'],set(['week']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i+1, word, score))
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['china'],set(['china']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i+1, word, score))
