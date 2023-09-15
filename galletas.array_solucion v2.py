import numpy as np
class Galleta:
    #Atributos
    @property
    def precio_venta(self):
        return self._precio_venta
    
    @precio_venta.setter
    def precio_venta(self, nuevo_valor):
        if(nuevo_valor >= 0):
            self._precio_venta = nuevo_valor
        else:
            raise ValueError('El precio de venta no puede ser negativo')
        
    @property
    def impuesto(self):
        return self._impuesto
    
    @impuesto.setter
    def impuesto(self, nuevo_valor):
        if(nuevo_valor < 0):
            raise ValueError('El impuesto no puede ser un valor negativo')
        if(nuevo_valor > 100):
            raise ValueError('El impuesto no puede ser mayor a 100')
        else:
            self._impuesto = nuevo_valor


    #_init_ es el metodo constructor. El metodo constructor sirve para construir OBJETOS
    #co y pf son parametros/argumentos
    #self: el primer parametro/argumento es el objeto en SI, o sea g1, g2. g3... etc
    _slots_ = ['color_ojos', 'precio_fabricacion', '_precio_venta', '_impuesto']
    def __init__(self, co='', pf=0, pv=0, i=0):
        self.color_ojos = co
        self.precio_fabricacion = pf
        self.precio_venta = pv
        self.impuesto = 0
        self.devuelta = False
        self.motivo_devuelta = ''

    #user input
    def pedir_datos(self, numero_galleta):
        numero_galleta += 1
        self.color_ojos = input(f'Ingrese el color de ojos de la galleta {numero_galleta}: ')
        self.precio_fabricacion = float(input(f'Ingrese el valor de fabricacion de la galleta {numero_galleta}: '))
        self.impuesto = float(input(f'Ingrese el impuesto de la galleta {numero_galleta}: '))

    def vender(self, numero_galleta):
        numero_galleta += 1
        self.precio_venta = float(input(f'Ingrese el valor de venta de la galleta {numero_galleta}: '))
        self.precio_venta = self.precio_venta + ((self.precio_venta)*(self.impuesto/100))
        print(f'valor total a pagar: {self.precio_venta}')


galletas_array = np.array([], dtype=object)

cantidad_galletas = int(input('Ingrese la cantidad de galletas: '))
for i in range(0, cantidad_galletas):
    g = Galleta()
    g.pedir_datos(i)
    galletas_array = np.append(galletas_array, g)

print('Galletas antes de vender')
for g in galletas_array:
    print(g.precio_venta)

cantidad_galletas_devuelta = 0
motivos = [0, 0, 0, 0]
dinero_perdido = 0
cantidad_galletas_vendidas = int(input('Ingrese la cantidad de galletas vendidas: '))
for p in range(0, cantidad_galletas_vendidas):
    galletas_array[p].vender(p)
    devuelta = input('¿Fue devuelta? Escriba un valor alfanumérico y enter para especificar un motivo: ')
    if (devuelta != ''):
        motivo = ''
        while motivo == '':
            motivo = int(input('¿Motivo de la devolución? 1: sabe maluco   2: muy fea   3: muy cara   4: vencida :'))
            print(motivo)
            if (motivo not in [1, 2, 3, 4]):
                print(f'{motivo} no es una opción válida')
                motivo = ''
            else: 
                cantidad_galletas_devuelta = cantidad_galletas_devuelta + 1
                motivos[motivo - 1] = motivos[motivo - 1] + 1
                dinero_perdido = dinero_perdido + galletas_array[i].precio_venta
 

print('Galletas despues de vender')
ganancias = 0
for g in galletas_array:
    print(g.precio_venta)
    ganancias = ganancias + g.precio_venta

print(f'Se devolvieron {cantidad_galletas_devuelta}')
print(f'{motivos[1]} estaban muy feas')
print(f'{motivos[0]} sabían maluco')
print(f'{motivos[3]} vencidas')
print(f'{motivos[2]} estaban muy caras')

motivo_mas_vendido = 'maluca'
motivo = 0
if (motivos[motivo] < motivos[1]):
    motivo_mas_vendido = 'fea'
else:
    motivo = 1

if (motivos[motivo] < motivos[2]):
    motivo_mas_vendido = 'cara'
else: 
    motivo = 2

if (motivos[motivo] < motivos[3]):
    motivo_mas_vendido = 'vencida'
else:
    motivo = 3

ganancias = ganancias - dinero_perdido

print(f'{motivo_mas_vendido} fue el motivo por el que más se devolvieron')
print(f'Se perdió {dinero_perdido} en devoluciones')
print(f'El total de ganancias fue: {ganancias}')
