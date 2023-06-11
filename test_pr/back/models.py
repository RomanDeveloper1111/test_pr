from back.abstracts.abstract_models import CreateData, models


class Producer(CreateData):
    name = models.CharField(max_length=255, verbose_name='Name of producer')

    def __str__(self):
        return self.name


class Product(CreateData):
    name = models.CharField(max_length=64, verbose_name='Name of product')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='producer_products',
                                 verbose_name='Producer')
    credit_order = models.ForeignKey('CreditOrder', on_delete=models.CASCADE, related_name='credit_products',
                                     verbose_name='Credit order')

    def __str__(self):
        return self.name


class CreditOrder(CreateData):
    contract = models.OneToOneField('Contract', on_delete=models.CASCADE, verbose_name='Contract')

    def __str__(self):
        return str(self.created_at)


class Contract(CreateData):
    pass

    def __str__(self):
        return str(self.created_at)





