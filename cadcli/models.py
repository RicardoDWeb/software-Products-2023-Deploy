from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=70)
    email_cliente = models.CharField(max_length=40)
    tel_cliente = models.CharField(max_length=20)

    class Meta:
        ordering = ['id_cliente']

    def __str__(self):
        return self.nome_cliente

    def get_absolute_url(self):
        return reverse('cadcli:alterar_um_cliente', args=[str(self.id_cliente)])
