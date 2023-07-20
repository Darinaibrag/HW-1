from django.db import models

# Create your models here.
# Модель Project (Проект):
# • Поле name (Название проекта) типа CharField с максимальной длиной 100 символов.
# • Поле description (Описание проекта) типа TextField.
# • Поле start_date (Дата начала проекта) типа DateField.
# • Поле end_date (Дата окончания проекта) типа DateField.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
