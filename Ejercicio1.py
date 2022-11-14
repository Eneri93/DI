from PySide6.QtWidgets import QLineEdit,QLabel,QMainWindow,QApplication

class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("titulo ventana")

        self.etiq=QLabel("etiqueta",self)
        self.edita=QLineEdit(self)
        self.etiq.move(150,0)
    def OT(self):
        self.edita.setText(self)

if __name__ == "__main__":
    app=QApplication([])
    ventana1=Ventana()
    ventana1.show()
    app.exec()

          
  