VAT_RATE = 7.0

def calculateVAT(productPrice):
    if productPrice >= 0:
        vatValue = (productPrice * VAT_RATE)/100
        return vatValue
    else: return 'Can not calculate VAT because the product price is minus.'
     