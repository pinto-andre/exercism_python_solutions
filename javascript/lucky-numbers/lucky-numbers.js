// @ts-check

import { isNull } from "util";

/**
 * Calculates the sum of the two input arrays.
 *
 * @param {number[]} array1
 * @param {number[]} array2
 * @returns {number} sum of the two arrays
 */
export function twoSum(array1, array2) {
  let stringOne = array1.toString();
  let stringTwo = array2.toString();
  let numberOne = Number(stringOne.replaceAll(",", ""));
  let numberTwo = Number(stringTwo.replaceAll(",", ""));

  return numberOne + numberTwo;
}

/**
 * Checks whether a number is a palindrome.
 *
 * @param {number} value
 * @returns {boolean} whether the number is a palindrome or not
 */
export function luckyNumber(value) {
  let valueArr = Array.from(String(value), Number);
  let reversedArr = [...valueArr].reverse(); // Spread operator to avoid modifying the original array
  for (let i = 0; i < valueArr.length; i++) {
    if (valueArr[i] !== reversedArr[i]) {
      return false;
    }
  }
  return true;
}

/**
 * Determines the error message that should be shown to the user
 * for the given input value.
 *
 * @param {string|null|undefined} input
 * @returns {string} error message
 */
export function errorMessage(input) {
  if (input == null || input === "") {
    return "Required field";
  }

  const num = Number(input);
  if (isNaN(num) || num === 0) {
    return "Must be a number besides 0";
  }

  return "";
}
