// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

import { time } from "console";

/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */
export function timeToMixJuice(name) {
  let time;
  switch (name) {
    case "Pure Strawberry Joy":
      time = 0.5;
      break;
    case "Energizer":
      time = 1.5;
      break;
    case "Green Garden":
      time = 1.5;
      break;
    case "Tropical Island":
      time = 3;
      break;
    case "All or Nothing":
      time = 5;
      break;
    default:
      time = 2.5;
  }
  return time;
}

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */
export function limesToCut(wedgesNeeded, limes) {
  // 6 wedges from a `'small'` lime, 8 wedges from a `'medium'` lime and 10 from a `'large'` lime.
  let limeSizing = {
    small: 6,
    medium: 8,
    large: 10,
  };
  let limeCount = 0;
  let wedgesCount = 0;

  if (wedgesNeeded === 0) {
    return limeCount;
  }

  for (let i = 0; i < limes.length; i++) {
    let type = limes[i];
    wedgesCount += limeSizing[type];
    limeCount = limeCount + 1;
    if (wedgesCount >= wedgesNeeded) {
      break;
    }
  }
  return limeCount;
}

/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft - The time left in minutes.
 * @param {string[]} orders - The array of juice orders.
 * @returns {string[]} The orders that remain after the shift ends.
 */
export function remainingOrders(timeLeft, orders) {
  while (timeLeft > 0) {
    timeLeft = timeLeft - timeToMixJuice(orders[0]);

    orders.shift();
  }

  return orders;
}
