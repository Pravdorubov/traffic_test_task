from django.contrib import admin

# Register your models here.

from .models import Employer
from .models import Duty
from .models import Department

admin.site.register(Employer)
admin.site.register(Duty)
admin.site.register(Department)
