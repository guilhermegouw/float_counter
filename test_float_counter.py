import unittest

from float_counter import split_string, extract_values


class TestFloatCounter(unittest.TestCase):
    def test_split_string(self):
        string = "0,01 X 1(0,55) X 5 METROS (0,905) x 5,67 MTRS (9,0)MTRS"
        output = split_string(string)
        expected = ['0,01', '1(0,55)', '5 METROS (0,905)', '5,67 MTRS (9,0)MTRS']
        self.assertEqual(expected, output)

    def test_extract_values(self):
        values_list = ['0,01', '1(0,55)', '5 METROS (0,905)', '5,67 MTRS (9,0)MTRS']
        output = extract_values(values_list)
        expected = [0.01, 0.55, 0.905, 9.0]
        self.assertEqual(expected, output)
