from django.db import models

# Create your models here.

# Create your models here.
class Grade(models.Model):

    g_name = models.CharField(max_length=20)
    g_name_date = models.DateField()
    g_girl_num = models.IntegerField()
    g_boy_num = models.IntegerField()
    is_delete = models.BooleanField(default=False)

    def report(self):
        return '%s--%d--%d'(self.g_name,self.g_boy_num,self.g_boy_num)


class Student(models.Model):

    s_name = models.CharField(max_length=20)
    s_age = models.IntegerField()
    s_sex = models.BooleanField(default=True)
    s_content = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
    # 外键
    s_grade = models.ForeignKey('Grade', on_delete=models.CASCADE)