import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_03_Sumar2Numeros.ui"
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
       if(self.txtA.text()!='' and self.txtB.text()):
           a = float(self.txtA.text())
           b = float(self.txtB.text())
           resultado = str(a + b);
           self.txtSuma.setText(resultado)
           self.txtA.clear()
           self.txtB.clear()
       else:
            msj = QtWidgets.QMessageBox()
            msj.setText('Alguno de los campos esta vacio')
            msj.exec_()




if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())