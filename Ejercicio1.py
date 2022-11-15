from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
class VentanaPrincipal (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle ("Esto es una ventanaa")

        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setFixedSize(50,30)
        self.lineedit1.setMaxLength(5)
        

        self.label1 = QLabel(self)
        self.label1.setFixedSize(50,30)
        self.label1.move(50,0)

        self.lineedit1.textChanged.connect(self.label1.setText)
        
if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()       