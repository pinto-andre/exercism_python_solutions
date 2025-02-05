/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */
export function cookingStatus(timer) {
  /* - If the timer shows `0`, it should return `'Lasagna is done.'`.
- If the timer shows any other number, the result should be `'Not done, please wait.'`.
- If the function is called without a timer value, the result should be `'You forgot to set the timer.'`. */
  if (timer === undefined) {
    return "You forgot to set the timer.";
  } else if (timer === 0) {
    return "Lasagna is done.";
  } else {
    return "Not done, please wait.";
  }
}

export function preparationTime(layers, layeringTime = 2) {
  return layers.length * layeringTime;
}

export function quantities(layers) {
  let ingredientQuantity = {
    noodles: 0,
    sauce: 0,
  };

  for (let i = 0; i < layers.length; i++) {
    if (layers[i] === "sauce") {
      ingredientQuantity.sauce += 0.2;
    } else if (layers[i] === "noodles") {
      ingredientQuantity.noodles += 50;
    }
  }
  return ingredientQuantity;
}

export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList[friendsList.length - 1]);
}

export function scaleRecipe(recipe, portions) {
  let scaled = { ...recipe };
  for (let item in recipe) {
    scaled[item] = recipe[item] * (portions / 2);
  }
  return scaled;
}
