# Ana está organizando su fiesta de cumpleaños y necesita calcular cuánto dinero necesita para comprar todo lo necesario 

#dinero disponible 
dinero = 500 
dinero_extra = 50 
dinero_total = dinero_extra + dinero

#costo de cosas para la fiesta 
pastel = 180
globos = 25 * 6  #150
refresco = 30 * 4 #120
dulces = 40 * 3 #120
#costo total de todo 
costo_total = pastel + globos + refresco + dulces 
#calcular lo que falta o sobra 
restante = dinero_total - costo_total

print("dinero disponible:",dinero_total)
print("costo total de fiesta:",costo_total)
print("tipo del resultado:",type(dinero))