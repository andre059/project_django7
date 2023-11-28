from django.contrib import admin

from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'payment_date', 'course_paid', 'payment_amount', 'payment_method')
    list_filter = ('first_name', 'course_paid')
