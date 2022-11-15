from PySide6.QtWidgets import QDateTimeEdit,QLabel,QMainWindow,QApplication

class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("titulo ventana")

        self.etiq=QLabel(self)
        self.fecha=QDateTimeEdit(self)
        
        self.fecha.timeChanged.connect(self.funcion)
        self.fecha.setFixedSize(120,30)
    def funcion(self):
        i= self.fecha.dateTime().toString()
        self.etiq.setText(i)

    
    
if __name__ == "__main__":
    app=QApplication([])
    ventana1=Ventana()
    ventana1.show()
    app.exec()
