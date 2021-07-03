from django.db import models

class LeadState(models.Model):

    STATE_NEW = 1  # Новый
    STATE_IN_PROGRESS = 2  # В работе
    STATE_POSTPONED = 3  # Приостановлен
    STATE_DONE = 4  # Завершен

    STATE_CHOICES = ((STATE_NEW,'Новый'),
                     (STATE_IN_PROGRESS, 'В работе'),
                     (STATE_POSTPONED, 'Приостановлен'),
                     (STATE_DONE, 'Завершен'))

    name = models.CharField(u"Название",max_length=50,unique=True,)


class Lead(models.Model):
    name = models.CharField(max_length=255,db_index=True,verbose_name=u"Имя",)
    state = models.ForeignKey(LeadState,
                              on_delete=models.PROTECT,
                              choices=LeadState.STATE_CHOICES,
                              verbose_name=u"Состояние",)


# Новый -> В работе
# В работе -> Приостановлен
# В работе -> Завершен
# Приостановлен -> В работе
# Приостановлен -> Завершен