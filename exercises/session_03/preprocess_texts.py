"""
Main script to preprocess a list of texts
"""

from utils.data_wranglers import wrangle_amazon_reviews, sample_amazon_reviews, \
    get_amazon_review
from utils.spacy_helpers import text2sentences, text2sentences_custom, text2tokens


#
# read data
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

#
# output
#

print('original review:', review_0_raw)
print('sentences:', sentences)
print('sentences custom:', sentences_custom)
print('tokens:', tokens)


