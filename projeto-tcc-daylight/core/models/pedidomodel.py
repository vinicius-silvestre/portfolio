import uuid
from django.db import models

STATUS_CHOICES = (('Orçamento', 'Orçamento'), ('Em andamento', 'Em andamento'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado'),)
FORM_PGTO_CHOICES = (('Débito', 'Débito'), ('Crédito', 'Crédito'), ('Boleto', 'Boleto'), ('Transferência', 'Transferência'),)
PRAZO_PGTO_CHOICES = (('À vista', 'À vista'), ('1x', '1x'), ('2x', '2x'), ('3x', '3x'),)
ESTAMPA_CHOICES = (('Sim', 'Sim'), ('Não', 'Não'),)

###################### PEDIDO

class Pedido(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_pedido = models.IntegerField('Numero do Pedido', unique=True, null=True, blank=True)
    cliente = models.ForeignKey(to='Cliente', on_delete=models.CASCADE, null=False, blank=False)
    data_pedido = models.DateField('Data de Compra', max_length=10, null=False)
    data_entrega = models.DateField('Data de Entrega', max_length=10, null=False)
    valor_total = models.DecimalField('Valor Total', max_digits=10, decimal_places=2, null=False, max_length=5000, blank=False)
    forma_pagamento = models.CharField('Forma de Pagamento', default='', choices=FORM_PGTO_CHOICES, max_length=15, null=True, blank=True)
    prazo_pagamento = models.CharField('Prazo de Pagamento', default='', choices=PRAZO_PGTO_CHOICES, max_length=20, null=True, blank=True)
    endereco_entrega = models.CharField('Endereço Entrega', max_length=100, null=True, blank=True)
    solicitante = models.CharField('Nome do Solicitante', max_length=50, null=True, blank=True)
    status = models.CharField('Status do Pedido', default='Orçamento', choices=STATUS_CHOICES, max_length=20, null=False, blank=False)
    personalizacao = models.CharField('Estampa', choices=ESTAMPA_CHOICES, max_length=3, null=False, blank=False)
    observacao = models.TextField('Observação', max_length=1000, null=True, blank=True)

    class Meta:
        db_table = 'Pedido'


    def __str__(self):
        return '{}'.format(self.numero_pedido)


    def save(self, *args, **kwargs):
        if self._state.adding:
            last_pedido = type(self).objects.all().aggregate(largest=models.Max('numero_pedido'))['largest']
            if last_pedido is None:
                self.numero_pedido = 1
            else:
                self.numero_pedido = last_pedido + 1
        super(Pedido, self).save(*args, **kwargs)
