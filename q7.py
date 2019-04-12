import re
import distsim

word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")

string = ''
flag = False
total = 0
correct1 = 0
correct5 = 0
correct10 = 0

with open("word-test.v3.txt") as f:
	for line in f:
		w = line.strip().split(' ')
		length = len(w)
		if flag and line[0] == ':':
			strings = string.strip('\n')
			score1 = str(round(float(correct1)/total,3))
			score5 = str(round(float(correct5)/total,3))
			score10 = str(round(float(correct10)/total,3)) 
			print strings + ':' +'\t' +score1 +'\t' +score5 +'\t' +score10 + '\n'
			correct1 = 0
			correct5 = 0
			correct10 = 0
			total = 0
		if length - 4 == 0:
			total += 1
			flag = True
			word1 = w[0].strip('\t')
			word2 = w[1].strip('\t')
			word3 = w[2].strip('\t')
			word4 = w[3].strip('\t')
			words1 = word_to_vec_dict[word1]
			words2 = word_to_vec_dict[word2]
			words4 = word_to_vec_dict[word4]
			ret = distsim.show_nearest(word_to_vec_dict,
                                   words1 - words2 + words4,
                                   set([word1, word2, word4]),
                                   distsim.cossim_dense)
			sim = []
			for i in ret:
				sim.append(i[0])
			pos = -1
			if word3 in sim:
				pos = sim.index(word3)
			if pos != -1 and pos < 10:
				correct10 += 1
			if pos != -1 and pos < 5:
				correct5 += 1
			if pos != -1 and pos < 1:
				correct1 += 1
		elif line[0] == ':':
			s = line.split(' ')
			string = s[1]
			# print 'test'
	strings = string.strip('\n')
	score1 = str(round(float(correct1)/total,3))
	score5 = str(round(float(correct5)/total,3))
	score10 = str(round(float(correct10)/total,3)) 
	print strings + ':' +'\t' +score1 +'\t' +score5 +'\t' +score10 + '\n'

