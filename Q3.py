a = 80000
b = 200000
anos = 0
while b > a:
    a = (a * 0.3) + a
    b = (b * 0.15) + b
    anos += 1
print ("o total de anos necessarios eh: %d" %contador) 
