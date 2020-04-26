from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Education(BaseModel):
    pass


class Skill(BaseModel):
    pass


class Sex(BaseModel):
    pass


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='media/pictures/', default='media/pictures/no-img.jpg')
    resume_file = models.FileField(blank=True, null=True, upload_to='media/files/')
    address = models.CharField(max_length=200, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True)
    sex = models.ForeignKey(Sex, on_delete=models.SET_NULL, null=True, related_name='sex')
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return str(self.user.id)


class ResumeEducation(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='resume_education')
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name='education')
    title = models.CharField(max_length=50)
    start_year = models.PositiveIntegerField(blank=True)
    end_year = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.title


class ResumeSkill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='resume_skill')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skill')
    level = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.skill.title


class ResumeExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='resume_experience')
    company = models.CharField(max_length=50)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    working_now = models.BooleanField(default=False)
