from datetime import datetime

from django.db import models


class category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class notify_method(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class member(models.Model):
    name = models.CharField(max_length=100)
    fk_category = models.ForeignKey(category, models.DO_NOTHING)
    notify_method = models.ForeignKey(notify_method, models.DO_NOTHING)
    notify_address = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' info over: ' + self.fk_category.name


class error(models.Model):
    fk_category = models.ForeignKey(category, models.DO_NOTHING)
    impacted_systems = models.TextField(max_length=1000)

    def __str__(self):
        return 'error of:' + self.fk_category.name


class states(models.Model):
    state = models.IntegerField(default=3)
    desc = models.CharField(max_length=20)

    def __str__(self):
        return self.desc


class error_updates(models.Model):
    fk_error = models.ForeignKey(error, models.CASCADE)
    status = models.ForeignKey(states, models.DO_NOTHING)
    timestamp = models.DateTimeField(default=datetime.now())
    reason = models.TextField(max_length=1000)

    def __str__(self):
        return 'update ' + str(self.timestamp) + ' on ' + self.fk_error.fk_category.name
