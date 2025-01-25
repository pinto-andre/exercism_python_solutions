/// <reference path="./global.d.ts" />
//
// @ts-check

/**
 * Determine the price of the pizza given the pizza and optional extras
 *
 * @param {Pizza} pizza name of the pizza to be made
 * @param {Extra[]} extras list of extras
 *
 * @returns {number} the price of the pizza
 */
export function pizzaPrice(pizza, ...extras) {
  let pizzaList = {
    Margherita: 7,
    Caprese: 9,
    Formaggio: 10,
  };
  let chosenPizzaPrice = 0;
  let extraPrice = 0;
  if (pizza in pizzaList) {
    chosenPizzaPrice = pizzaList[pizza];
  }
  for (let i = 0; i < extras.length; i++) {
    if (extras[i] === "ExtraSauce") {
      extraPrice = extraPrice + 1;
    } else {
      extraPrice = extraPrice + 2;
    }
  }
  return chosenPizzaPrice + extraPrice;
}

/**
 * Calculate the price of the total order, given individual orders
 *
 * (HINT: For this exercise, you can take a look at the supplied "global.d.ts" file
 * for a more info about the type definitions used)
 *
 * @param {PizzaOrder[]} pizzaOrders a list of pizza orders
 * @returns {number} the price of the total order
 */
export function orderPrice(pizzaOrders) {
  let totalPrice = 0;
  for (let i = 0; i < pizzaOrders.length; i++) {
    let pizza = pizzaOrders[i].pizza;
    let extra = pizzaOrders[i].extras;
    totalPrice = totalPrice + pizzaPrice(pizza, ...extra);
  }
  return totalPrice;
}
