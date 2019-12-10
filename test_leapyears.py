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

    def testIsLeapFor4AndNot100(self):
        leap_years = LeapYears()
        self.assertTrue(leap_years.isLeapYear(2008))


    def testIsNotLeapForNot4(self):
        leap_years = LeapYears()
        self.assertFalse(leap_years.isLeapYear(2017))