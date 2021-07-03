from django.db import models

class StateMeta(type):
    def __getattr__(cls,key):
        state = key.strip('get_')
        if state not in [state for state in dict(cls.CHOICES).values()]:
            raise AttributeError(key)
        else:
            state_index = list(dict(cls.CHOICES).values().index(state))
            state_pk = list(dict(cls.CHOICES).keys())[state_index]
            return lambda: cls.objects.get(pk=state_pk)


class DeliveryState(metaclass=StateMeta):

        class Meta:
            verbose_name = 'Состояние доставки'
            verbose_name_plural = 'Состояние доставок'

        def __str__(self):
            return f'{self.__class__.__name__}({self.pk})'

        STATE_NEW = 1  # Новая
        STATE_ISSUED = 2  # Выдана курьеру
        STATE_DELIVERED = 3  # Доставлена
        STATE_HANDED = 4  # Курьер сдал
        STATE_REFUSED = 5  # Отказ
        STATE_PAID_REFUSED = 6  # Отказ с оплатой курьеру
        STATE_COMPLETE = 7  # Завершена
        STATE_NONE = 8  # Не определен

        CHOICES = (
            (STATE_NEW,'new'),
            (STATE_ISSUED,'issued'),
            (STATE_DELIVERED,'delivered'),
            (STATE_HANDED,'handed'),
            (STATE_REFUSED,'refused'),
            (STATE_PAID_REFUSED,'paid_refused'),
            (STATE_COMPLETE,'complete'),
            (STATE_NONE,'none'),
        )