from django.contrib import admin

from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_filter = ('username',)
    search_fields = ('username',)
    readonly_fields = ('id',)

    fieldsets = (
        ('', {
            'fields': ('username',)
        }),
    )


admin.site.register(Account, AccountAdmin)
