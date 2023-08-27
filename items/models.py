from django.db import models
from django.utils.timezone import datetime, timedelta

class Item(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    init_date = models.DateField(auto_now_add=True)

    def calculate_next_date(init_date):
        date = datetime.strptime(init_date, '%y-%m-%d')                    
        return date + timedelta(days=1)

    next_date = models.DateField(default=calculate_next_date)

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
        return "{} - {} - ({}) @ {} --> {}".format(self.title, self.description, self.stage, self.init_date, self.next_date)