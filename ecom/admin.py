from django.contrib import admin
from .models import Customer,Product,Orders,Feedback, News, Comment
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)

class NewsAdmin(admin.ModelAdmin):
    pass
admin.site.register(News, FeedbackAdmin)
# Register your models here.


admin.site.register(Comment)