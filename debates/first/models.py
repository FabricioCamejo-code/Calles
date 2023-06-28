from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"


class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.pais}"


#class Calle(models.Model):
#    nombre = models.CharField(max_length=100)
#    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

#    def __str__(self):
#        return self.nombre
class Calle(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    estado_actual = models.CharField(max_length=255)
    problemas_actuales = models.TextField()
    detalles_renovacion = models.TextField()
    imagen = models.ImageField(upload_to='calle', null=True, blank=True)
    pdf = models.FileField(upload_to='calle', null=True, blank=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    fecha_finalizacion = models.DateTimeField(null=True, blank=True)
    fecha_inicio = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"{self.nombre} {self.ciudad} {self.ubicacion} {self.direccion} {self.estado_actual} {self.problemas_actuales} {self.detalles_renovacion} {self.imagen} {self.pdf} {self.fecha_hora}"


from django.db.models import UUIDField
import uuid


class Voto(models.Model):
    nombre_persona = models.CharField(max_length=30, null=True, blank=True)
    apellido = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField()
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    calle = models.ForeignKey(Calle, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False, max_length=255)
    confirmado = models.BooleanField(default=False)
    confirmation_token = models.CharField(default=uuid.uuid4, editable=False, max_length=255)


    def __str__(self):
        return f"{self.nombre_persona} {self.apellido} {self.email} {self.dni} {self.telefono} {self.calle} {self.ciudad} {self.pais} {self.token}  {self.confirmation_token}  {self.confirmado}"



class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.message} {self.email} - {self.created_at}"
    

class Visit(models.Model):
    ip_address = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    operating_system = models.CharField(max_length=100)
    browser = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.ip_address}  {self.timestamp} {self.operating_system}  {self.browser} {self.user_agent}"