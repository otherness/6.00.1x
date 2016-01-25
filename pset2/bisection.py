balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0
lowerBound = balance/12.0
upperBound = (balance * (1 + monthlyInterestRate)**12)/12.0
rem_balance = 1
while (rem_balance > 0) or (rem_balance < -0.01):
    rem_balance = balance
    fixedPayment = (upperBound + lowerBound)/2.0
   # print "Lower bound: " + str(lowerBound)
   # print "Upper bound: " + str(upperBound)
   # print "Fixed payment: " + str(fixedPayment)
    monthlyUnpaidBalance = 0
    
    for month in range(1,13):
        monthlyUnpaidBalance = rem_balance - fixedPayment
        rem_balance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
    
   # print rem_balance
    if (rem_balance < 0):
        upperBound = fixedPayment
    else:
        lowerBound = fixedPayment
        
    
print "Lowest payment: " +str(round(fixedPayment,2))