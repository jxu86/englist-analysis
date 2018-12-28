import nltk
nltk.download('averaged_perceptron_tagger')

word_tag = nltk.tag.pos_tag(words)