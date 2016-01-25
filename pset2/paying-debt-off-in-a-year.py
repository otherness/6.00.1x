balance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0
fixedPayment = round(balance / 12, -1) - 10

rem_balance = 1
while ( rem_balance > 0):
    fixedPayment += 10
    rem_balance = balance
    monthlyUnpaidBalance = 0
    
    for month in range(1,13):
        monthlyUnpaidBalance = rem_balance - fixedPayment
        rem_balance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate

print "Lowest payment: " +str(int(fixedPayment))