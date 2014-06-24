import sys
import unittest
from highest_share_price import HighestSharePrice

class TestingHighestSharePrice(unittest.TestCase):
    """ Unittest for the HighestSharePrice Class
    """

    def setUp(self):
		self.expected_result = ['Company_0: 2013, Aug, 50', 'Company_1: 2011, Nov, 100', 
		'Company_2: 2010, Dec, 150', 'Company_3: 2010, May, 220', 'Company_4: 2012, Apr, 360']		

    def test_success(self):
		""" Test the Working of Module
		"""
		
		class_object = HighestSharePrice()
		actual_result = class_object.get_highest_share_price()
		
		self.assertEqual(self.expected_result, actual_result)
		self.assertTrue(actual_result)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingHighestSharePrice)
    unittest.TextTestRunner(verbosity=2).run(suite)            
    sys.exit()