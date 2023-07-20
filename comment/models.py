from django.db import models

from task.models import Task


# Create your models here.
# 3. Модель Comment (Комментарий):
# • Поле task (Задача) типа ForeignKey, связано с моделью Task.
# • Поле user (Пользователь) типа ForeignKey, связано с моделью User.
# • Поле content (Содержание комментария) типа TextField.
# • Поле created_at (Дата создания комментария) типа DateTimeField с автоматическим добавлением значения при создании записи.


class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} --> {self.task} --> {self.content[:25]}'


