from django.contrib import admin
from .models import Bands, Event, BandEvent
# Register your models here.
class BandEventAdminInline(admin.StackedInline):
    model = BandEvent
    extra = 0
class EventAdmin(admin.ModelAdmin):
    exclude = ['user','bands',]
    list_display = ('name', 'date')
    inlines = [BandEventAdminInline,]

    def has_add_permission(self, request):
        return request.user.is_superuser

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(EventAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return obj and obj.user == request.user

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user

class BandAdmin(admin.ModelAdmin):
    list_display = ("name", "country",)

admin.site.register(Bands, BandAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(BandEvent)

