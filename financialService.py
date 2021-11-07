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

def showDepreciationTable(prop_value, prop_life):
    print("table")
    pv = "{:.2f}".format(prop_value)
    pl = "{:.1f}".format(prop_life)

    print("\n")
    print("\tDouble Declining Depreciation Table\n")
    print("\tProperty value: $",pv)
    print("\tProperty life: ", pl,"\n")

    print("\tYear\t\tValue At\t\tDepreciation\t\tTotal Depreciation",)
    print("\tYear\t\tBegin Year\t\tDuring Year\t\t",)
    print("\t__________________________________________________________________________________________________________\n")

    count = 0
    depreciation = 0
    total_depreciation = 0

    while prop_life > count:
        count = count + 1
        depreciation = prop_value * 2 / prop_life
        total_depreciation = total_depreciation + depreciation

        p = "${:,.2f}".format(prop_value)
        d = "${:,.2f}".format(depreciation)
        t = "${:,.2f}".format(total_depreciation)

        output_20 = "\t{0}{1:^29.2f}{2:^32.2f}{3:^1.2f}".format(count, round(prop_value, 2), round(depreciation, 2), round(total_depreciation, 2))

        if(count < 10):
            print("\t",count,"\t\t",p,"\t\t",d,"\t\t",t)
        else: 
            print("\t",count,"\t\t",p,"\t\t",d,"\t\t",t)

        prop_value = prop_value - depreciation
