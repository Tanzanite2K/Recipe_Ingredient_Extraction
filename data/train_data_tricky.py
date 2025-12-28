    # fraction quantity, multi-word ingredient with adjective

TRAIN_DATA = [

    ("Add 1½ cups finely chopped onions",
     {"entities": [
         (4, 7, "QUANTITY"),        # 1½
         (8, 12, "UNIT"),               # cups
         (13, 32, "INGREDIENT")      # finely chopped onions
     ]}),


    ("Mix 2–3 tablespoons extra-virgin olive oil",
     {"entities": [
         (4, 7, "QUANTITY"),     # 2–3
         (8, 19, "UNIT"),           # tablespoons
         (20, 42, "INGREDIENT")      # extra-virgin olive oil
     ]}),


    ("Pour about ½ liter milk",
     {"entities": [
         (10, 13, "QUANTITY"),         # ½
         (14, 19, "UNIT"),         # liter
         (20, 24, "INGREDIENT")   # milk
     ]}),



    ("Add 6 eggs",
     {"entities": [
         (4, 5, "QUANTITY"),   # 6
         (6, 10, "INGREDIENT")      # eggs
     ]}),

    ("Use 250 grams unsalted butter",
     {"entities": [
         (4, 7, "QUANTITY"),    # 250
         (8, 13, "UNIT"),          # grams
         (14, 30, "INGREDIENT")         # unsalted butter
     ]}),
    ("Stir in 1 teaspoon vanilla extract",
     {"entities": [
         (7, 8, "QUANTITY"),   # 1
         (9, 17, "UNIT"),         # teaspoon
         (18, 34, "INGREDIENT")    # vanilla extract
     ]}),



    ("Add 5 kg all-purpose flour",
     {"entities": [
         (4, 5, "QUANTITY"),    # 5
         (6, 8, "UNIT"),            # kg
         (9, 26, "INGREDIENT")    # all-purpose flour
     ]}),

    ("Mix 2 tablespoons sugar",
     {"entities": [
         (4, 5, "QUANTITY"),   # 2
         (6, 17, "UNIT"),         # tablespoons
         (18, 23, "INGREDIENT")    # sugar
     ]}),



    ("Add roughly 4½ cups chopped fresh tomatoes",
     {"entities": [
         (11, 14, "QUANTITY"),  # 4½
         (15, 19, "UNIT"),          # cups
         (20, 43, "INGREDIENT")   # chopped fresh tomatoes
     ]}),


    ("Use 1–2 teaspoons dark-roast coffee beans",
     {"entities": [
         (4, 7, "QUANTITY"),    # 1–2
         (8, 17, "UNIT"),        # teaspoons
         (18, 44, "INGREDIENT")      # dark-roast coffee beans
     ]}),
]
