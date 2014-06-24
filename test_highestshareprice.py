import sys
import unittest
from highest_share_price import HighestSharePrice

class TestingHighestSharePrice(unittest.TestCase):
	""" Unittest for the HighestSharePrice Class
	"""

	def setUp(self):
		self.expected_result = ['Company_0: 2006, Jan, 50', 'Company_1: 2012, Mar, 100', 
		'Company_2: 2011, May, 150', 'Company_3: 2008, Dec, 200', 'Company_4: 2011, Aug, 250']

	def test_success(self):
		""" Test the Working of Module.
		"""
		class_object = HighestSharePrice()
		actual_result = class_object.get_highest_share_price()

		self.assertEqual(self.expected_result, actual_result)
		self.assertTrue(actual_result)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingHighestSharePrice)
    unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit()