from syllable import syl_count
import nltk, string
from nltk.tokenize.punkt import PunktWordTokenizer as tok

def flesch(sent):
	ty = type(sent)
	if ty==str:
		sent = tok().tokenize(sent.translate(None, string.punctuation))
		ty = list
	if ty == list:
		sent = [w.translate(None, string.punctuation) for w in sent]
		word_count = len(sent)
		if word_count == 0: return -1
		asl = word_count
		total_syl = 1.0*sum([syl_count(w) for w in sent])
		asw = total_syl/word_count
		print asw, total_syl, word_count
		return 206.835 - (1.015 * asl) - (84.6 * asw) 	
	else: return -1

