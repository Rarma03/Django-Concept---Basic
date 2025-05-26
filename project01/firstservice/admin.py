from django.contrib import admin

from .models import chaiVariety     #added-01
from .models import ChaiCertificate, ChaiReview, Store      #added-02

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2   

@admin.register(chaiVariety)          # New Method to register using decorators
class chaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added', 'image')  # Add any fields you want shown
    inlines = [ChaiReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varities',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')

# admin.site.register(chaiVariety,chaiVarietyAdmin)    # Old Method
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
admin.site.register(Store, StoreAdmin)