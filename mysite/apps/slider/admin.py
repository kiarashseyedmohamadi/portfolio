from django.contrib import admin
from .models import Slider
from django.utils.html import format_html

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'is_active', 'create_at')
    list_filter = ('is_active', 'create_at')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:100px; height:auto;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'تصویر'
