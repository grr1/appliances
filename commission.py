def calcStoveCommission(units):
    if units <=3:
        comission  = 0
    else:
        commission = 0.03 * units * 1400 
        
    return comission
    
def refrigeratorCommission(units):
    if units <=12:
        comission  = 0
    else:
        commission = 0.035 * units * 250 
        
    return comission    