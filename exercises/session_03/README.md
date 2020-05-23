# Session 3. Data Cleaning for NLP

We will perform with [spacy](https://spacy.io/): Tokenization, Stemming and Lemmatization, Stop Word removal, Punctuation Removal. 

## Steps

1. Clone (or pull) this repo.

2. Install project's requirements (for this exercise, you can create a dedicated virtual environment).

3. Load the small (sm) spacy model: `python -m spacy download en_core_web_sm`

4. Download the raw data we will work with: [amazon_co-ecommerce_sample_short.csv](https://drive.google.com/open?id=1Sv8ntNtQdHcWEa8nItGirAHd9ASoAaeC), with reviews of 50 Amazon products. Place it under `frauenloop_interml_course\exercises\session_03\data\`.

5. Execute the `preprocess_texts.py` script:

```bash
cd frauenloop_interml_course\exercises\session_03
python preprocess_texts.py
```

Note that a sample review text is extracted from the dataframe, and separated into sentences and then into tokens.

6. Take a look at the output. 

* What is the difference between splitting sentences using spacy or using our custom method?
* What does `split()` do ? And `strip()` ?
* Include code to remove the `\n` + spaces in `'By\n    \n    spiro clinton\n  \n on 26 Feb. 2015'`:

```python
def text2sentences_custom(text: str) -> List[str]:

    # ...
    sentences2 = [sentence.replace('\n', '') for sentence in sentences_]
    sentences3 = [' '.join(sentence.split())
                  for sentence in sentences2]
    # ...
```

7. Adapt the tokenization function to extract relevant [token attributes](https://spacy.io/api/token#attributes), such as `lower_`, `lemma_`, `is_alpha`, `is_digit`, `is_punct`, `pos_`, ...

```python
def text2tokens_(text: str) -> List[dict]:
    """
    Tokenize a text and return tokens and relevant attributes

    Args:
        text (str): text to tokenize
    """
    doc = nlp(text)

    tokens = [{'text': t.text,
               'lower_': t.lower_,
               'lemma_': t.lemma_,
               'is_alpha': t.is_alpha,
               'is_digit': t.is_digit,
               'is_punct': t.is_punct,
               'pos_': t.pos_}
              for t in doc]

    return tokens

# ...
from utils.spacy_helpers import text2tokens_
tokens_ = text2tokens_(sentences[0])
[print(t) for t in tokens_]
```

Try with different sentences. 

8. How to use these attributes? For example, for lemmatization:

```python
lemmas = [t.lemma_ for t in nlp(text)]
print(f"Spacy lemmatized text: {' '.join(lemmas)}")
```

Or to remove punctuation.

9. Add code to remove stop words.

```python
def remove_stopwords(text: str):
    # ...
    if token.is_stop is True:
        # ...
```

See list of stop words in spacy:

```python
from spacy.lang.en.stop_words import STOP_WORDS
print(STOP_WORDS)
```

To use a custom list of stop words [see this solution](https://stackoverflow.com/questions/41170726/add-remove-custom-stop-words-with-spacy/46380305#46380305).

10. Apply the `preprocess_texts.py` script to your own texts. You might have to adapt splitting, character removal, etc.


## Read more


* [Spacy's Linguistic annotations](https://spacy.io/usage/spacy-101#annotations)
* [Text preprocessing with NLTK and Spacy](https://towardsdatascience.com/text-preprocessing-steps-and-universal-pipeline-94233cb6725a)
* [preprocessing pipeline](https://towardsdatascience.com/setting-up-text-preprocessing-pipeline-using-scikit-learn-and-spacy-e09b9b76758f)