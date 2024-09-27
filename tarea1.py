producto1="sabritas"
costo1=18.50
iva=.14
total1=costo1+(costo1*iva)
producto2="coca cola"
costo2=23.99
total2=costo2+(costo2*iva)
producto3="galletas"
costo3=16.98
total3=costo3+(costo3*iva)
producto4="jugo"
costo4=8.00
total4=costo4+(costo4*iva)
producto5="chocolates"
costo5=27.50
total5=costo5+(costo5*iva)
producto6="gomitas"
costo6=13.50
total6=costo6+(costo6+iva)
producto7="azúcar"
costo7=37.99
total7=costo7+(costo7*iva)
producto8="tortillas"
costo8=25.00
total8=costo8+(costo8*iva)
producto9="aceite"
costo9=28.50
total9=costo9+(costo9*iva)
producto10="arroz"
costo10=32.00
total10=costo10+(costo10*iva)
print("{:^20} {:^20} {:^20}".format("Producto","Valor sin IVA","Total de compra"))
print("{:^20} {:^20} {:^20,.2f}".format(producto1,costo1,total1))
print("{:^20} {:^20} {:^20,.2f}".format(producto2,costo2,total2))
print("{:^20} {:^20} {:^20,.2f}".format(producto3,costo3,total3))
print("{:^20} {:^20} {:^20,.2f}".format(producto4,costo4,total4))
print("{:^20} {:^20} {:^20,.2f}".format(producto5,costo5,total5))
print("{:^20} {:^20} {:^20,.2f}".format(producto6,costo6,total6))
print("{:^20} {:^20} {:^20,.2f}".format(producto7,costo7,total7))
print("{:^20} {:^20} {:^20,.2f}".format(producto8,costo8,total8))
print("{:^20} {:^20} {:^20,.2f}".format(producto9,costo9,total9))
print("{:^20} {:^20} {:^20,.2f}".format(producto10,costo10,total10))