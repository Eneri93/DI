from PySide6.QtWidgets import QApplication, QWidget ,QDial,QLabel
class VentanaPrincipal (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle ("Esto es una ventanaa")

        self.dial = QDial(self)
        self.dial.setFixedSize(50,30)
        

        self.etiqueta = QLabel(self)
        self.etiqueta.setFixedSize(50,30)
        self.etiqueta.move(50,0)

        self.dial.valueChanged.connect(self.etiqueta.setText)
        
if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()       