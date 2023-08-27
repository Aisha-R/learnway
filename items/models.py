from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    class Stage(models.IntegerChoices):
        INITIAL = 0
        DAY_1 = 1
        DAY_7 = 7
        DAY_16 = 16
        DAY_35 = 35

    stage = models.IntegerField(
        choices=Stage.choices,
        default=Stage.INITIAL
    )

    def __str__(self):
        return "{} - {} - ({})".format(self.title, self.description, self.stage)