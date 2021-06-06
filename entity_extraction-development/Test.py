import spacy
from spacy.tokens import Doc
from pathlib import Path

output_dir=Path('new_hindi_model/')

nlp=spacy.load(output_dir)

nlp=nlp.get_pipe("ner")

test_text = 'सांचोर जाना है मुजे'.split()
test_text
spaces = []
for i in range(len(test_text)):
    spaces.append(True)

doc = Doc(nlp.vocab, words=test_text, spaces=spaces)

out = nlp(doc)
for ent in out.ents:
    print(ent.text,ent.label_)

