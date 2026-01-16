products={
    "tv":15000,
    "mobaile":5000,
    "laptop":65000,
    "Ac":75000,
    "fridge":40000
}

d2=dict(filter(lambda item:item[1]>50000,products.items()))
print(d2)