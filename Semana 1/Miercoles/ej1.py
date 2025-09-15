volumen_reservorio = 4.445*(10**8)
lluvia = 5*(10**6)
lluvia = lluvia * 0.9
volumen_reservorio += lluvia
volumen_reservorio *= 1.05
volumen_reservorio = volumen_reservorio - (volumen_reservorio * 0.02)
volumen_reservorio -= 2.5*(10**5)
print(volumen_reservorio)