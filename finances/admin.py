from django.contrib import admin
from .models import BudgetRequest, Equipment, EventEquipment

admin.site.register(BudgetRequest)
admin.site.register(Equipment)
admin.site.register(EventEquipment)
