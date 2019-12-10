import unittest
from leapyears import LeapYears

class TestLeapYears(unittest.TestCase):

    def testLeapYearsIsInvoked(self):
        leap_years = LeapYears()

    def testIsLeapFrom400(self):
        leap_years = LeapYears()
        self.assertTrue(leap_years.isLeapYear(2000))

    def testIsLeapFrom100AndNot400(self):
        leap_years = LeapYears()
        self.assertFalse(leap_years.isLeapYear(1900))