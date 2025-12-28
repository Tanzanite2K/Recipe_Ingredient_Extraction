import spacy
from spacy.training.example import Example
import sys
import os

# fix import path for data folder

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))

sys.path.insert(0, project_root)


# now imports from data work
from data.train_data_simple import TRAIN_DATA as TRAIN_SIMPLE
from data.train_data_tricky import TRAIN_DATA as TRAIN_TRICKY

# combined dataset for training
TRAIN_DATA = TRAIN_SIMPLE + TRAIN_TRICKY



# fixing import path issue if any
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)


# load base model for fine-tuning
nlp = spacy.load("en_core_web_sm")


ner = nlp.get_pipe("ner")

# add custom labels


ner.add_label("INGREDIENT")
ner.add_label("QUANTITY")
ner.add_label("UNIT")


# start the training
optimizer = nlp.resume_training()

print("Training started...")




for i in range(30):
    losses = {}

    for text, annot in TRAIN_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annot)
        nlp.update([example], drop=0.35, losses=losses)

    print("Epoch", i + 1, "Loss:", losses)

print("Training completed.")

model_path = os.path.join(project_root, "model", "recipe_ner_model")



# make sure directories exist
os.makedirs(model_path, exist_ok=True)

# save the model
nlp.to_disk(model_path)


print("Model saved at:", model_path)
