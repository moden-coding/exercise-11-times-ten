#!/usr/bin/env python3

import unittest

from src.times_ten import times_ten


def expected(a, b):
    return {x: x * 10 for x in range(a, b + 1)}


class TestTimesTen(unittest.TestCase):

    def test_function_is_callable(self):
        try:
            times_ten(1, 2)
        except Exception as e:
            self.fail(
                "times_ten(1, 2) should be callable without error. "
                "Got exception: %r" % (e,))

    def test_return_type_is_dict(self):
        result = times_ten(1, 2)
        self.assertIsInstance(
            result, dict,
            msg=f"times_ten should return a dict. Got {type(result)}.")

    def test_various_ranges(self):
        test_cases = ((1, 3), (0, 6), (2, 8), (20, 23), (100, 110))
        for a, b in test_cases:
            result = times_ten(a, b)
            correct = expected(a, b)
            self.assertEqual(
                len(result), len(correct),
                msg="times_ten(%d, %d) should return a dict with %d "
                "items, but it returned %d items: %s"
                % (a, b, len(correct), len(result), result))
            self.assertEqual(
                result, correct,
                msg="times_ten(%d, %d) returned\n%s\nbut the correct "
                "result is\n%s" % (a, b, result, correct))

    def test_single_value_range(self):
        result = times_ten(5, 5)
        self.assertEqual(
            result, {5: 50},
            msg="times_ten(5, 5) should return {5: 50}: the range is "
            "inclusive of both endpoints, so a single value still counts.")


if __name__ == '__main__':
    unittest.main()
