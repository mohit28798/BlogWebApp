from django.contrib import admin
from .models import post,category,feedbacks
# Register your models here.

class feedAdmin(admin.ModelAdmin):
    readonly_fields=('firstname','lastname','email','phone','message')
    list_display=('firstname','lastname','email','phone','message')


class UserAdmin(admin.ModelAdmin):
    list_display=('cate','heading','thumb','disc','footer')
def cate(self,obj):
    return obj.category.categories

cate.short_description='category'
cate.admin_order_field='category'

admin.site.register(post, UserAdmin)
admin.site.register(category)
admin.site.register(feedbacks, feedAdmin)