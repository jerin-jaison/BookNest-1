from django.contrib import admin
from .models import (
	Customer, Category, Product, ProductImage, ProductOffer,
	CategoryOffer, ReferralOffer, ReferralCode, ReferralHistory,
	Coupon, CouponUsage, Review
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'price', 'stock', 'status')
	prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'is_active')


admin.site.register(ProductImage)
admin.site.register(ProductOffer)
admin.site.register(CategoryOffer)
admin.site.register(ReferralOffer)
admin.site.register(ReferralCode)
admin.site.register(ReferralHistory)
admin.site.register(Coupon)
admin.site.register(CouponUsage)
admin.site.register(Review)
admin.site.register(Customer)
