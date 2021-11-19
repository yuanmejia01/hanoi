#Ejercicio torres de Hanoi
torre_1 = 1 #torre inicial
torre_2 = 2 #torre medio
torre_3 = 3 #torre final
class Hanoi:
    def __init__(self):
        pass
    def excepcion(self,number):
        try:
            int(number)
            return int(number)
        except:
            return "Valor ingresado no es valido."
    def excepcion1(self,number):
        if number <= 0:
            return "Numero de discos no valido."
        else:
            return number
    @staticmethod
    def stepsHanoi(number_of_disks,torre_1,torre_2,torre_3):
        Torres = ['1','2','3']
        steps = (2 ** number_of_disks) - 1
        if number_of_disks == 1:
            print(f"Mueva el disco desde la torre {Torres[(torre_1)-1]} hasta la torre {Torres[(torre_3)-1]}")
        elif number_of_disks > 1:
            Hanoi.stepsHanoi(number_of_disks - 1, torre_1, torre_3, torre_2)
            print(f"Mueva el disco desde la torre {Torres[(torre_1) - 1]} hasta la torre {Torres[(torre_2) - 1]}")
            Hanoi.stepsHanoi(number_of_disks - 1, torre_2, torre_3, torre_1)
        else:
            steps = "El valor ingresado no es valido"
        return steps
# Función principal
def main():
    valido = True
    while valido:
        number_of_disks = input('Introduzca el numero de discos para resolver el problema de torres de Hanoi: ')
        objeto = Hanoi()
        number_of_disks = objeto.excepcion(number_of_disks)
        if number_of_disks == "Valor ingresado no es valido.":
            print("El valor ingresado no es valido")
        else:
            number_of_disks = objeto.excepcion(number_of_disks)
            if number_of_disks == "Numero de discos no valido.":
                print("El valor ingresado no es valido")
            else:
                steps = objeto.stepsHanoi(number_of_disks,torre_1,torre_2,torre_3)
                if steps == "El valor ingresado no es valido":
                    print(steps)
                else:
                    valido = False
                    print(f'\nSe necesitan {steps} pasos para resolver las torres de Hanoi con {number_of_disks} discos')
main()