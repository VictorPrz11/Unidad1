import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_04_SumaAritmeticas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los signals
        self.botonsumar.clicked.connect(self.operacion)
        self.botonresta.clicked.connect(self.operacion)
        self.botonmult.clicked.connect(self.operacion)
        self.botondivision.clicked.connect(self.operacion)

    #   self es igual a una variable de clase
    #   self es el equivalente al this
    def operacion(self):
        try:
            objeto = self.sender()
            nombre = objeto.objectName()
            A = int(self.txtA.text())
            B = int(self.txtB.text())
            if nombre == "botonsumar":
                resultado = str(A + B);
                self.txtResultado.setText(resultado)
                self.txtA.clear()
                self.txtB.clear()
            elif nombre == "botonresta":
                resultado = str (A-B)
                self.txtResultado.setText(resultado)
                self.txtA.clear()
                self.txtB.clear()
            elif nombre == "botonmult":
                resultado = str(A*B)
                self.txtResultado.setText(resultado)
                self.txtA.clear()
                self.txtB.clear()
            elif nombre == "botondivision":
                resultado = str(A/B)
                self.txtResultado.setText(resultado)
                self.txtA.clear()
                self.txtB.clear()
        except Exception as error:
            print(error)


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())