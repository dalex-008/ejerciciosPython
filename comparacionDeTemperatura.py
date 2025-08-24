temperatura_hoy = int(input("que temperatura esta hoy"))
temperatura_ayer = int(input("que temperatura estaba ayer"))

if temperatura_ayer >  temperatura_hoy:
    print("hay mas calor de que hoy")
if temperatura_ayer == temperatura_hoy:
    print("esta igual que ayer ")
else:
    print("nooo aler avia mas")