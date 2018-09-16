import unittest

from calculateVAT import calculateVAT

class TestCalculateVAT(unittest.TestCase):
    def testCalculateVAT_When_productPrice_100_vatRate_7_VAT_ShouldBe_7(self):
        productPrice = 100.00
        vatRate = 7.00
        expectedResult = 7.00

        actualResult = calculateVAT(productPrice,vatRate)

        self.assertEqual(actualResult,expectedResult)
        

if __name__ == '__main__':
    unittest.main()
