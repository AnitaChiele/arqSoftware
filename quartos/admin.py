from django.contrib import admin
from .models import StatusQuarto, Quarto, TipoCama, CamaQuarto

admin.site.register(StatusQuarto)
admin.site.register(TipoCama)


class CamaQuartoInline(admin.TabularInline):
    model = CamaQuarto
    extra = 1
    min_num = 1


@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    inlines = [CamaQuartoInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        quarto = form.instance
        quarto.save()
