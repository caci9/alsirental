from django.contrib import admin
from .models import *
from django.contrib import admin
from .models import Customer, Car, Reservation


# Register your models here.
admin.site.register(Payment)
admin.site.register(Reservation)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('car', 'image')
    search_fields = ('car__name', )


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'winter_rental_price', 'summer_rental_price', 'year', 'transmission_type')
    search_fields = ('id', 'transmission_type', 'name') 
    list_filter = ('name',)
    list_editable = ('winter_rental_price', 'summer_rental_price')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'last_name', 'phone', 'address', 'license_number')
    search_fields = ('user__username', 'name', 'last_name')  # Search by username or customer name
    list_filter = ('user',)

    def save_model(self, request, obj, form, change):
        # Automatically link the logged-in user as the customer
        if not obj.user:
            obj.user = request.user  # Set the user to the currently logged-in user if not set
        obj.save()

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarImage, ImagesAdmin)

