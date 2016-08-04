from django.contrib import admin

from .models import(OrderModel)
from .models import(FeedbackModel)
from .models import(SetModel)
from .models import(RationModel)

admin.site.register(FeedbackModel)
admin.site.register(OrderModel)
admin.site.register(SetModel)
admin.site.register(RationModel)
# Register your models here.
