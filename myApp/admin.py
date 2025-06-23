from django.contrib import admin

# Register your models here.
from .models import TrackDatas
from .models import Contacts
from .models import Testimonial
from .models import Newsletter

admin.site.register(TrackDatas)
admin.site.register(Contacts)
admin.site.register(Newsletter)
admin.site.register(Testimonial)

