from django.db import models

# Create your models here.


class Integer(models.Model):
    val = models.IntegerField(default=-1)


class TxId(models.Model):
    pid = models.IntegerField(default=-1)
    bid = models.IntegerField(default=-1)
    txNum = models.IntegerField(default=-1)
    worker = models.IntegerField(default=-1)

    def __str__(self):
        return '[%d%d%d%d]'.format(self.worker, self.pid, self.bid, self.txNum)
