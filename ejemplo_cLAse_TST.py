"""POO,OBJETO: LA INSTANCIA, CLASE, 
DEFINIR UNA CLASE ELECTRODOMESTICO"""

class electrodomestico:
 codigo =0
nombre= ""
categoria = ""
precio=0
def __init__(self,codigo,nombre,categoria,precio):
    self.nombre=nombre
    self.categoria=categoria
    self.precio=precio
    
    def get_codigo(self):...
    def set_codigo(self,codigo):...

    def get_categoria(self):...

    def set_categoria(self,categoria):...

    def get_precio(self):
        def set_precio(self,precio):

            def MostrarDatos(self):

                print('El nombre del electrodomestico es:' + 'su codigo es'+str(self.codigo)+
                'La categoria a la que pertenece es:'+ self.categoria + 'su precio es'+ str(self.precio) )



        