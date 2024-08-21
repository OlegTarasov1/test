from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models
from courses.models import Course

class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()


class Balance(models.Model):
    """Модель баланса пользователя."""

    user = models.OneToOneField(get_user_model(),
        on_delete = models.CASCADE,
        related_name = 'balance')
    
    balance = models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
        default = 0.00
        )
    
    def balance_add(self, instance, number):
        if self.user.is_staff:
            instance.balance += number
            instance.save()
            return 'balance has been upgraded successfully!'
        else:
            return 'only staff can change balance'

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        ordering = ('-id',)


class Subscription(models.Model):
    """Модель подписки пользователя на курс."""

    user = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
        )

    date_enrolled = models.DateTimeField(
        auto_now_add = True
    )

    subscriptions = models.ManyToManyField(Course, related_name = 'users')

    def purchase(self, course):
        if self.subscriptions.filter(id=course.id).exists():
            balance = self.user.balance
            if balance.balance >= course.price:
                balance.balance -= course.price
                self.subscriptions.add(course)
                balance.save()
            else:
                return 'not enough money'
        else:
            return 'you already are signed up for the course'


    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)

