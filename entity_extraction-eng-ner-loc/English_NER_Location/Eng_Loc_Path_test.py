# %%
from pathlib import Path

# %%
import spacy

# %%
output_dir=Path('Eng_loc_Model/')

# %%
nlp=spacy.load(output_dir) 

# %%
nlp.to_disk(output_dir)

# %%
# Load the saved model and predict
print("Loading from", output_dir)
nlp_updated = spacy.load(output_dir)
doc = nlp_updated(input("Enter the test"))
print("Entities", [(ent.text, ent.label_) for ent in doc.ents])

# %%


# %%


# %%
