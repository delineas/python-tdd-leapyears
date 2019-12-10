class LeapYears:
    def divisible (self, num, divider):
        return not num % divider

    def isLeapYear(self, year):
        if self.divisible(year, 100) and not self.divisible(year, 400):
            return False
        if not self.divisible(year, 4):
            return False
        return True
