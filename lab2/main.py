import gensim

word2vec = gensim.models.KeyedVectors.load_word2vec_format("cbow.txt", binary=False)
pos = ["мир_NOUN", "помещик_NOUN"]
dist = word2vec.most_similar(positive=pos)
for i in dist:
    print(i)