import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_06_SumANumeros_V2_ConEstilo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los signals
        self.botonsumar.clicked.connect(self.suma)
        
#   self es igual a una variable de clase
#   self es el equivalente al this
    def suma(self):
            #el usuario ingresara los numeros separados por espacios...
            numeros = self.txtA.text()
            lista = numeros.split(' ')# convierte la entrada de numeros en una lista Ejemplo['1','2','3']
            lista_en_numeros = [int(i) for i in lista]
            print(lista_en_numeros)
            suma = sum(lista_en_numeros)
            self.txtResultado.setText(str(suma))




if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())