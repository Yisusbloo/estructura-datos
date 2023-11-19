from .tipos import Item

class Nodo:
    def __init__(self, valor: Item, mensaje_id: int):
        self.valor = valor         
        self.mensaje_id = mensaje_id  
        self.siguiente = None       

class Cola:
    def __init__(self):
        self.primero = None           
        self.ultimo = None            
        self.contador_id = 1          

    # Método para verificar si la cola está vacía
    def esta_vacia(self):
        return self.primero is None

    # Método para encolar un nuevo mensaje en la cola
    def encolar(self, valor: Item):
        nuevo_nodo = Nodo(valor, self.contador_id)  # Creamos un nuevo nodo con un ID único
        if self.esta_vacia():
            self.primero = nuevo_nodo  # Si la cola está vacía, el nuevo nodo se convierte en el primero
        else:
            self.ultimo.siguiente = nuevo_nodo      # Enlazamos el último nodo con el nuevo nodo
        self.ultimo = nuevo_nodo                    # El nuevo nodo se convierte en el último
        self.contador_id += 1                       # Se incrementa el contador de IDs para el siguiente mensaje

    # Método para desencolar el primer mensaje de la cola
    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.primero.valor                   # Obtenemos el valor del primer mensaje
        mensaje_id = self.primero.mensaje_id         # Obtenemos el ID del primer mensaje
        self.primero = self.primero.siguiente        # El siguiente nodo se convierte en el primero
        if self.primero is None:
            self.ultimo = None
        return {"mensaje_id": mensaje_id, "valor": valor}  # Devolvemos el mensaje desencolado como un diccionario

    # Método para ver todos los mensajes en la cola
    def ver_listado(self):
        elementos = []
        actual = self.primero
        while actual:
            elementos.append({"mensaje_id": actual.mensaje_id, "valor": actual.valor})
            actual = actual.siguiente
        return elementos  # Devolvemos una lista de mensajes como diccionarios

    # Método para ver el último mensaje en la cola
    def ver_ultimo(self):
        if self.ultimo:
            return {"mensaje_id": self.ultimo.mensaje_id, "valor": self.ultimo.valor}
        else:
            return None

    # Método para ver el primer mensaje en la cola
    def ver_primero(self):
        if self.primero:
            return {"mensaje_id": self.primero.mensaje_id, "valor": self.primero.valor}
        else:
            return None

    # Método para contar la cantidad de mensajes en la cola
    def contar(self):
        count = 0
        actual = self.primero
        while actual:
            count += 1
            actual = actual.siguiente
        return count # El mensaje o solicitud se eliminó exitosamente

    # Método para eliminar un mensaje específico de la cola por su mensaje_id
    def eliminar_mensaje(self, mensaje_id: int):
        actual = self.primero
        anterior = None

        while actual and actual.mensaje_id != mensaje_id:
            anterior = actual
            actual = actual.siguiente

        if actual:
            if anterior:
                anterior.siguiente = actual.siguiente
            else:
                self.primero = actual.siguiente

            if not actual.siguiente:
                self.ultimo = anterior
            return True  # El mensaje se eliminó exitosamente

        return False  # El mensaje con el mensaje_id no se encontró en la cola
    