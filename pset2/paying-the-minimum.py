balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate/12.0
minPayment = 0
monthlyUnpaidBalance = 0
totalPaid = 0


for month in range(1,13):
    print "Month: " + str(month)
    minPayment = balance * monthlyPaymentRate
    totalPaid += minPayment
    print "Minimum monthly payment: " +  str(round(minPayment,2))
    monthlyUnpaidBalance = balance - minPayment
    balance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
    print "Remaining balance: " + str(round(balance,2))

print "Total paid: " + str(round(totalPaid,2))
print "Remaining balance: " + str(round(balance,2))