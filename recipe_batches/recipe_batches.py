#!/usr/bin/python

import math

ingredients = {
  'eggs': 15,
  'butter': 30,
  'sugar': 24,
  'flour': 45
}

recipe = {
  'eggs': 7,
  'butter': 10,
  'sugar': 10,
  'flour': 5
}

def recipe_batches(recipe, ingredients):
  recipeValues = []
  ingredientValues = []
  dividedValues = []
  for x in recipe.values():
    recipeValues.append(x)

  for x in ingredients.values():
    ingredientValues.append(x)
  
  for x in range(0, len(recipeValues)):
    dividedValues.append(int(ingredientValues[x]/recipeValues[x]))

  print(dividedValues)



print(recipe_batches(recipe, ingredients))

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))