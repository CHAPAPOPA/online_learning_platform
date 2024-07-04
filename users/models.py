from django.contrib.auth.models import AbstractUser
from django.db import models

from course.models import Course
from lesson.models import Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Введите почту"
    )
    phone = models.CharField(
        max_length=11,
        verbose_name="Телефон",
        help_text="Введите номер телефона",
        **NULLABLE
    )
    city = models.CharField(
        max_length=50, verbose_name="Город", help_text="Укажите город", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatar/",
        verbose_name="Аватар",
        help_text="Загрузите аватар",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("id",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    METHOD_LIST = [
        ('cash', 'Оплата наличными'),
        ('non_cash', 'Безналичная оплата'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateField(verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    payment_amount = models.FloatField(default=0.0, verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=10, choices=METHOD_LIST, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.user}: {self.paid_course if self.paid_course else self.paid_lesson}'

    class Meta:
        ordering = ('-payment_date', )
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'
