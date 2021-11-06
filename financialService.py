def futueValue(presentValue,rate,year):
    futureValue=presentValue*(1+rate)**year
    return futureValue

def monthlyPayment(loan,rate,term):
    pmt=(loan*rate/12)/(1-(1+rate/12)**(-12*term))
    return pmt

def goalSeek(presentValue, rate, target):
	futureValue = presentValue
	years = 0

	while futureValue < target:
		years = years + 1
		futureValue = presentValue * (1 + rate)** years 

	return years 
        
