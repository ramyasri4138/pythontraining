# convert the prices in USD & Euro using appropriate function
#     PricesList_inr =[3000,56000,45000,2300]
PricesList_inr =[3000,56000,45000,2300]

for value in PricesList_inr:
    value=value*0.011
    print(f"{value:.2f} usd",end=' ')
print("")
for value2 in PricesList_inr:
    value2=value2*0.012
    print(f"{value:.2f} euro")
    
# Exchange rates
inr_to_eur = 0.011
inr_to_usd = 0.012

# Input list of values in INR
inr_values = [100, 200, 500, 1000]

# Convert INR to EUR and USD
eur_values = []
for value in inr_values:
    eur_value = value * inr_to_eur
    eur_values.append(eur_value)
usd_values = [value * inr_to_usd for value in inr_values]

print("Values in INR: ", inr_values)
print("Values in EUR: ", eur_values)
print("Values in USD: ", usd_values)


PricesList_inr=[3000,56000,45000,2300]
def conv_usd(PricesList_inr):
    print([(num*0.011) for num in PricesList_inr])
def conv_euro(PricesList_inr):
    print([(num*0.012) for num in PricesList_inr])
def main():
    conv_usd(PricesList_inr)
    conv_euro(PricesList_inr)
main()