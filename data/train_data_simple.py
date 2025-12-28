    # simple sentences with quantity, unit and ingredient

TRAIN_DATA = [

    ("Add 2 cups of flour",
     {"entities": [
         (4, 5, "QUANTITY"),     # 2
         (6, 10, "UNIT"),           # cups
         (14, 19, "INGREDIENT")  # flour
     ]}),


    ("Use 1 teaspoon salt",
     {"entities": [
         (4, 5, "QUANTITY"),         # 1
         (6, 14, "UNIT"),        # teaspoon
         (15, 19, "INGREDIENT")  # salt
     ]}),
    ("Mix 200 grams butter",
     {"entities": [
         (4, 7, "QUANTITY"),     # 200
         (8, 13, "UNIT"),            # grams
         (14, 20, "INGREDIENT")  # butter
     ]}),



    ("Add 3 eggs",
     {"entities": [
         (4, 5, "QUANTITY"),        # 3
         (6, 10, "INGREDIENT")   # eggs
     ]}),


    ("Pour 1 cup milk",
     {"entities": [
         (5, 6, "QUANTITY"),     # 1
         (7, 10, "UNIT"),           # cup
         (11, 15, "INGREDIENT")     # milk
     ]}),
    ("Use 2 tablespoons olive oil",
     {"entities": [
         (4, 5, "QUANTITY"),     # 2
         (6, 17, "UNIT"),           # tablespoons
         (18, 27, "INGREDIENT")  # olive oil
     ]}),



    ("Add 100 grams sugar",
     {"entities": [
         (4, 7, "QUANTITY"),         # 100
         (8, 13, "UNIT"),        # grams
         (14, 19, "INGREDIENT")  # sugar
     ]}),

     

    ("Mix 1 cup venigar",
     {"entities": [
         (4, 5, "QUANTITY"),     # 1
         (6, 9, "UNIT"),            # cup
         (10, 15, "INGREDIENT") # venigar
     ]}),
]
