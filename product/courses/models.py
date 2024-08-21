from django.db import models
from django.contrib.auth import get_user_model

class Course(models.Model):
    """Модель продукта - курса."""

    author = models.CharField(
        max_length=250,
        verbose_name='Автор',
    )
    title = models.CharField(
        max_length=250,
        verbose_name='Название',
    )
    start_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата и время начала курса'
    )

    # TODO
    price = models.DecimalField(
        max_digits=10,
        decimal_places = 2,
        default=0.00
    )

    # END

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('-id',)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Модель урока."""

    title = models.CharField(
        max_length=250,
        verbose_name='Название',
    )
    link = models.URLField(
        max_length=250,
        verbose_name='Ссылка',
    )

    # TODO
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name = 'lessons')
    
    time_started = models.DateTimeField(
        auto_now_add = True
        )

    # END

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Group(models.Model):
    """Модель группы."""

    # TODO

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('-id',)
