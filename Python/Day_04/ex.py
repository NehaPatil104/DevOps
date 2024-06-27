#rate = 5

def loan_factory(rate):
    
    def calulator(p, n):
        return p * n * rate / 100
    
    def updated_r(updated_rate):
        nonlocal rate
        rate = updated_rate
        
    return [calulator, updated_r]

car_emi_cal, updated_rate = loan_factory(8)

#print(car_emi_cal(100, 2)) 

updated_rate(3)
print(car_emi_cal(2000, 2))