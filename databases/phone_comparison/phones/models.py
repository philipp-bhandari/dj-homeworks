from django.db import models


class Phone(models.Model):
    price = models.FloatField()
    os_sys = models.TextField()
    resolution = models.TextField()
    cam_matrix = models.TextField()
    ram_memory = models.TextField()


class Huawei(models.Model):
    fm_radio = models.BooleanField()
    ir_port = models.BooleanField()
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE)
    model = models.TextField()


class LG(models.Model):
    fm_radio = models.BooleanField()
    ir_port = models.BooleanField()
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE)
    model = models.TextField()

