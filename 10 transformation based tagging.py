
def apply_transformation_rule(word):
    if word.lower().endswith('ing'):
        return 'VERB'
    else:
        return 'NOUN'
def transform_based_pos_tagging(sentence):
    tagged_sentence = []
    for word in sentence:
        pos_tag = apply_transformation_rule(word)
        tagged_sentence.append((word, pos_tag))
    return tagged_sentence
sentence_to_tag = ['The', 'running', 'dog', 'is', 'jumping']
tagged_sentence = transform_based_pos_tagging(sentence_to_tag)
print("Original Sentence:", sentence_to_tag)
print("Transformation-based POS Tagging Result:", tagged_sentence)
