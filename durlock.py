def calculadorDeMateriales ():
    lado1 = float(input("Ingrese la medida de uno de los lados: "))
    lado2 = float(input("Ingrese la medida de otro de los lados: "))
    if lado1 > lado2:
        ladoLargo = lado1
        ladoCorto = lado2
    elif lado2 > lado1:
        ladoLargo = lado2
        ladoCorto = lado1
    else:
        ladoLargo = lado1
        ladoCorto = lado2
    perimetro = 2*(lado1 + lado2)
    placaDurlock = 2.88 #metros cuadrados
    medidaMontantes = 2.60
    medidaSolera = 2.60
    cielorraso = ladoLargo * ladoCorto #resultado en metros cuadrados 
    soleras = perimetro / medidaSolera
    if ladoCorto >= medidaSolera:
        soleras += perimetro / medidaSolera*2
    cantidadPlacas = cielorraso / placaDurlock
    montantesX = ladoLargo / 0.40# Distancia entre cada montante
    montantesY = ladoCorto / 2.60 
    totalMontantes = montantesX * montantesY
    t2PorPlaca = 50 #aprox
    t1 = perimetro / 0.15
    t2 = t2PorPlaca * cantidadPlacas
    print("Cantidad de placas de Durlock necesarias:", round(cantidadPlacas + cantidadPlacas /10 ,1))
    print("Cantidad de soleras necesarias:", round(soleras + soleras/10,1))
    print("Cantidad de montantes necesarios:", round(totalMontantes + totalMontantes /10 ,1))
    print(f"Cantidad de T1 es: {t1} y T2 total: {t2}")
calculadorDeMateriales()