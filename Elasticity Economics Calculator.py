#Python Program to calculate Price Elastisticity of Demand/Supply in Economics
print("Price Elasticity of Demand/Supply Calculator")
print()
#User input quantity 1 and quantity 2
quant1=float(input("Enter Initial Quantity (Q1): "))
quant2=float(input("Enter Final Quantity (Q2): "))
print()
#User input price 1 and price 2
price1=float(input("Enter Initial Price (P1): "))
price2=float(input("Enter Final Quantity (P2): "))
print()
#Calculate ED
quantelasticity=(quant2-quant1)/(quant2+quant1)
priceelasticity=(price2-price1)/(price2+price1)
ed=round(quantelasticity/priceelasticity,2)
print("Elasticity of Demand = ", ed)
