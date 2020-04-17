from django.contrib import admin
from . import models


admin.site.register(models.Resume)
admin.site.register(models.Skill)
admin.site.register(models.Education)
admin.site.register(models.Sex)
admin.site.register(models.ResumeEducation)
admin.site.register(models.ResumeSkill)
admin.site.register(models.ResumeExperience)


