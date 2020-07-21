"""
Main script to preprocess a list of texts
"""

from utils.data_wranglers import wrangle_amazon_reviews, sample_amazon_reviews, \
    get_amazon_review
from utils.spacy_helpers import text2sentences, text2sentences_custom, text2tokens, text2tokens_
import spacy


#
# read data_manipulation
#

df = wrangle_amazon_reviews()
# sample_review = sample_amazon_reviews(df, 1)[0]
# review_0 = get_amazon_review(df, 0)
review_0_raw = df.loc[0, 'customer_reviews']

#
# splitting sentences
#

sentences = text2sentences(review_0_raw)
sentences_custom = text2sentences_custom(review_0_raw)

#
# tokenization
#

# tokenize a sentence
tokens = text2tokens(sentences[0])
tokens_ = text2tokens_(sentences[0])

#
# output
#

#print('original review:', review_0_raw)
#print('sentences:', sentences)
#print('sentences custom:', sentences_custom)
#print('tokens:', tokens)
#print('sentences 0', sentences[0])
#[print(t) for t in tokens_]




#-------------------

#lemmas = [t.lemma_ for t in nlp(text)]
#print(f"Spacy lemmatized text: {' '.join(lemmas)}")


text = 'We are, a group, in Frauenloop.'

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

all_tokens = list()
for token in doc:
    all_tokens.append(token)

tokens_dirty = list()
tokens_clean = list()
lemmas = list()
for token in doc:
    lemmas.append(token.lemma_)
    if token.is_punct is False:
        tokens_clean.append(token)
    else:
        tokens_dirty.append(token)

print('lemmas', lemmas)
print('all_tokens', all_tokens)
print('tokens_dirty', tokens_dirty)
print('tokens_clean', tokens_clean)



