from django.db import models
from django.utils import timezone
from users.models import CustomUser

class Item(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    init_date = models.DateField(auto_now_add=True)

    def calculate_next_date():                   
        return timezone.now() + timezone.timedelta(days=1)

    next_date = models.DateField(default=calculate_next_date, editable=False)

    class Stage(models.IntegerChoices):
        INITIAL = 0
        DAY_1 = 1
        DAY_7 = 7
        DAY_16 = 16
        DAY_35 = 35

    stage = models.IntegerField(
        choices=Stage.choices,
        default=Stage.INITIAL,
        editable=False
    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='items',
        blank=False,
        null=False
    )

    def __str__(self):
        return "{} / {} / AT STAGE {} / BEGUN ON {} / NEXT REVISION DUE ON {} by {}".format(self.title, self.description, self.stage, self.init_date, self.next_date, self.user)