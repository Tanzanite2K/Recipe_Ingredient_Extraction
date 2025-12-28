from flask import Flask, request, jsonify
import spacy
import re

app = Flask(__name__)

# Load your trained spaCy NER model
nlp = spacy.load("model/recipe_ner_model")

# This was initial simple logic (worked for single ingredients, but failed for tricky sentences)
"""
@app.route("/extract_old", methods=["POST"])
def extract_entities_old():
    data = request.get_json()
    recipe_text = data.get("recipe")

    
    if recipe_text is None: 
        return jsonify({"error": "No recipe text provided"}), 400

    doc = nlp(recipe_text)
    results = []

    temp = {}

    for ent in doc.ents:
    
        if ent.label_ == "QUANTITY":
        
            temp["quantity"] = ent.text
        elif ent.label_ == "UNIT":
            temp["unit"] = ent.text
        elif ent.label_ == "INGREDIENT":
        
            temp["name"] = ent.text
            results.append(temp)
            temp = {}  # reset for next ingredient

            
    return jsonify({"ingredients": results})
"""

# Updated that logic to handle multi-ingredient sentences, descriptors, and for better JSON
def split_recipe(recipe_text):

    # split by ',' and 'and' to catch multiple ingredients

    parts = re.split(r',| and ', recipe_text)
    return [p.strip() for p in parts if p.strip()]

def extract_ingredients(recipe_text):
    ingredients = []

    for part in split_recipe(recipe_text):
        doc = nlp(part)
        item = {}


        for ent in doc.ents:
            if ent.label_ == "INGREDIENT":
                item["name"] = ent.text
            elif ent.label_ == "QUANTITY":
                item["quantity"] = ent.text
            elif ent.label_ == "UNIT":
                item["unit"] = ent.text

        if item.get("name"):
            # separate descriptors from ingredient name
            words = item["name"].split()
            if len(words) > 1:
                item["descriptor"] = " ".join(words[:-1])

                item["name"] = words[-1]
            ingredients.append(item)
    return ingredients


@app.route("/extract", methods=["POST"])
def extract():
    data = request.get_json()
    recipe_text = data.get("recipe", "")

    if not recipe_text:
        return jsonify({"error": "No recipe text provided"}), 400
    
    result = extract_ingredients(recipe_text)
    
    return jsonify({"ingredients": result})


if __name__ == "__main__":
    # Only the new /extract endpoint works now
    app.run(host="0.0.0.0", port=5000, debug=True)
