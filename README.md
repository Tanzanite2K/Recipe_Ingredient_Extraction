# 🍳 Recipe Ingredient Extraction using Named Entity Recognition

## 📖 About the Project

This project is about extracting **ingredients, quantities, and units** from cooking recipes written in plain English.
Instead of using rules or hard-coded logic, I trained a **custom Named Entity Recognition (NER) model** using **spaCy** and exposed it through a **Flask API**.

The idea was to understand how NLP models can be trained for **real-world text**, especially something messy like recipe instructions, where the format is never consistent.

---

## 🎯 What This Project Does

* Accepts a recipe sentence as input (for example:
  *“Add 2 cups of flour and 1 teaspoon salt”*)
* Uses a **custom-trained spaCy NER model** to detect:

  * Quantity (e.g., `2`, `1 teaspoon`, `2–3`)
  * Unit (e.g., `cups`, `tablespoons`, `grams`)
  * Ingredient (e.g., `flour`, `olive oil`)
* Handles **both simple and tricky sentences**
* Returns structured **JSON output**
* Provides a **Flask REST API** that can be tested using Postman

---

## 🛠 Technologies Used

* **Python**
* **spaCy** – for training and running the NER model
* **Flask** – to build the REST API
* **Regex** – for splitting complex recipe sentences
* **Docker** – for containerization (optional)
* **Postman** – for API testing

---

## 📁 Project Structure

```
Recipe_Ingredient_Extraction/
│
├── app.py                     # Flask API (updated version)
├── training/
│   └── train_ner.py            # Script to train the NER model
│
├── data/
│   ├── train_data_simple.py    # Simple recipe examples
│   └── train_data_tricky.py    # Tricky / real-world examples
│
├── model/
│   └── recipe_ner_model/       # Saved trained model
│
├── Dockerfile
└── README.md
```

---

## 🧪 Dataset Explanation

I used **two datasets** instead of one:

### 1️⃣ Simple Dataset

Contains clean and short sentences like:

* “Add 2 cups of flour”
* “Use 1 teaspoon salt”

This helps the model learn the **basic structure** of recipes.

### 2️⃣ Tricky Dataset

Contains more realistic and confusing sentences like:

* “Add 2–3 tablespoons extra-virgin olive oil”
* “Finely chopped onions, about 1 cup”

This dataset improves the model’s ability to handle **real cooking language**.

Both datasets are combined during training without replacing each other.

---

## 🏋️ Model Training

* Base model used: `en_core_web_sm`
* Custom labels added:

  * `INGREDIENT`
  * `QUANTITY`
  * `UNIT`
* Training runs for multiple epochs
* Loss values reduce gradually, showing the model is learning
* Trained model is saved locally and reused by the API

---

## 🌐 Flask API Usage

### Endpoint

```
POST /extract
```

### Request (JSON)

```json
{
  "recipe": "Add 2 cups of flour and 1 teaspoon salt"
}
```

### Response (JSON)

```json
{
  "ingredients": [
    {
      "name": "flour",
      "quantity": "2",
      "unit": "cups"
    },
    {
      "name": "salt",
      "quantity": "1",
      "unit": "teaspoon"
    }
  ]
}
```

---

## 🔄 Code Evolution

Initially, the API used a **very simple logic** that worked only for one ingredient at a time.
Later, the code was improved to:

* Split complex recipes using commas and “and”
* Handle multiple ingredients in one sentence
* Separate descriptors like *“extra-virgin”* from ingredient names

The older logic is still kept in comments to show **project progression**.

---

## 🧪 Testing

* API was tested using **Postman**
* Both simple and tricky recipes were tested
* Output was verified manually

## Outputs 
![ouput_RI](https://github.com/user-attachments/assets/162fdb6e-ad5b-4851-9254-5b388529fbb0)
<img width="1600" height="808" alt="image" src="https://github.com/user-attachments/assets/4aed5821-aaf2-4504-9029-15fe96fee666" />
<img width="1600" height="813" alt="image" src="https://github.com/user-attachments/assets/1a626df4-18e0-42ed-b994-48994758c0a8" />
<img width="1600" height="667" alt="image" src="https://github.com/user-attachments/assets/43791fe4-004b-4ea3-a269-fbd9473374eb" />
