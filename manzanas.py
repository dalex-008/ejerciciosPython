stock = int(input("cuntas tienes en stock"))
pedido = int(input("cuantas manzanas quieres en el pedido"))

if stock >= pedido:
    print("si te tenemos stock")
else:
    print("no tenemos stock")