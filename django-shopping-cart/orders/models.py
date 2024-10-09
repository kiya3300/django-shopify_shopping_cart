from django.contrib.auth.models import User
from django.db import models
from carts.models import Cart


ORDER_STATUS = (
    ('started', 'Started'),
    ('abandoned', 'Abandoned'),
    ('finished', 'Finished'),
)


class Order(models.Model):

    user = models.ForeignKey(User, blank=True, null=True)

    order_id = models.CharField(unique=True, max_length=120, default='abc')
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=255, choices=ORDER_STATUS, default='started')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    subtotal = models.DecimalField(default=1000.0, max_digits=300, decimal_places=2)
    tax_amount = models.DecimalField(default=1000.0, max_digits=300, decimal_places=2)

    def total(self):
        return self.subtotal + self.tax_amount

    def __unicode__(self):
        return '<Order:' + self.order_id + '> ' + self.status + ' | ' + unicode(self.created_at)



