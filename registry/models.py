from django.db import models

class Gift(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'Disponível'),
        ('RESERVED', 'Reservado (Aguardando Pagamento)'),
        ('PURCHASED', 'Comprado'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_base64 = models.TextField(blank=True, null=True, help_text="String da imagem em Base64")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AVAILABLE')
    buyer_name = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"
