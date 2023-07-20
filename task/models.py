from django.db import models


# Create your models here.
# 1. Модель Task (Задача):
# • Поле title (Заголовок) типа CharField с максимальной длиной 100 символов.
# • Поле description (Описание) типа TextField.
# • Поле status (Статус) типа BooleanField со значением по умолчанию False.
# • Поле created_at (Дата создания) типа DateTimeField с автоматическим добавлением значения при создании записи.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} --> {self.status}'
