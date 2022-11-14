from PySide6.QtWidgets import QApplication,QLabel,QWidget
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("nueva ventana")
        self.etiqueta1=QLabel("Hola mundo",self)
if __name__ == "__main__":
    app=QApplication([])
    ventana1=Ventana()
    ventana1.show()
    app.exec()
