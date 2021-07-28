from django.db import models

DEVICE_TYPE_CHOICE = (
    ("SR", "Сирена"),
    ("SP", "Громкоговоритель"),
)


class Device(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название устройства")
    location_address = models.CharField(max_length=150, verbose_name="Адрес размещения")
    latitude = models.DecimalField(max_digits=15, decimal_places=6, verbose_name="Широта")
    longitude = models.DecimalField(max_digits=15, decimal_places=6, verbose_name="Долгота")
    zone_radius = models.IntegerField(null=False, verbose_name="Радиус зоны звукопокрытия")
    device_type = models.CharField(max_length=16, default=DEVICE_TYPE_CHOICE[0], choices=DEVICE_TYPE_CHOICE,
                                verbose_name="Тип устройства")

    def __str__(self):
        return "Название устройства - {0}, Тип устройства {1}".format(self.name, self.device_type)

    class Meta:
        verbose_name = "Устройствa"
        verbose_name_plural = "Устройств"
        ordering = ["name"]
