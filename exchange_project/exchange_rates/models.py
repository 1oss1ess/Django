from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100, unique=True)
    course_code = models.CharField(max_length=3, unique=True)
    course_to_bgn = models.DecimalField(max_digits=15, decimal_places=5)
    reverse_course = models.DecimalField(max_digits=15, decimal_places=5)
    count_currency = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        ordering = ('course_code',)
        verbose_name_plural = 'currencies'

    def __str__(self):
        return '{} : {}'.format(self.course_code, self.course_to_bgn)
