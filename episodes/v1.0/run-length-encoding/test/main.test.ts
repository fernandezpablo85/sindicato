import fc from "fast-check";
import { rle } from "../src/main";

// sanity check that tests work
test("adds 1 + 2 to equal 3", () => {
  expect(1 + 2).toBe(3);
});

test("rle for empty strings should be the empty array", () => {
  expect(rle("")).toStrictEqual([]);
});

test("rle single letter should be the letter with count of 1", () => {
  expect(rle("a")).toEqual([["a", 1]]);
});

test("rle two letters should be the two letters with count of 1", () => {
  let x = rle("ab");
  expect(x).toEqual([
    ["a", 1],
    ["b", 1],
  ]);
});

test("rle of 10 letters should be the letter with count of 10", () => {
  expect(rle("aaaaaaaaaa")).toEqual([["a", 10]]);
});

test("rle letters should be the letters with their count", () => {
  expect(rle("abbcccdddd")).toEqual([
    ["a", 1],
    ["b", 2],
    ["c", 3],
    ["d", 4],
  ]);
});

// this is just an example of a property-based-test
it("sum is commutative", () => {
  const commutativity = fc.property(
    fc.integer(),
    fc.float(),
    (a: number, b: number) => {
      return a + b === b + a;
    }
  );

  fc.assert(commutativity, { verbose: true });
});
