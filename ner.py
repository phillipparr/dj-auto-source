import spacy
nlp = spacy.load('en')


def get_names_from_article(article):
    doc = nlp(article)
    non_humans = ['dog', 'cat', 'dogs', 'cats']

    good_tokens= []
    token_texts = []

    for token in doc:
        if token.ent_type_ == 'PERSON' and token.text not in token_texts:
            token_texts.append(token.text)
            good_tokens.append(token)

    heads = [token.head.text for token in good_tokens]
    children = [[child for child in token.children] for token in good_tokens]
    conjuncts = [[conjunct for conjunct in token.conjuncts] for token in good_tokens]
    lefts = [[left for left in token.lefts] for token in good_tokens]
    rights = [[right for right in token.rights] for token in good_tokens]

    for token in good_tokens:
        if token.head.text in non_humans:
            good_tokens.remove(token)

    return [token.text for token in good_tokens]