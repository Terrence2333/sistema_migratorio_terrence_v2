class ProductoForm:
    def __init__(self, request):
        self.nombre = request.form.get('nombre')
        self.cantidad = request.form.get('cantidad')
        self.precio = request.form.get('precio')

