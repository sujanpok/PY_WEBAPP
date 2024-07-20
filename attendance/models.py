from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    class Meta:
        db_table = 'employee_table'  # Custom table name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
