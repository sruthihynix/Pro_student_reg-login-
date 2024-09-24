from django.db import models

class Student_Info(models.Model):
    s_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    class Meta:
        db_table='table_Student'

    def __str__(self):
        return self.username
