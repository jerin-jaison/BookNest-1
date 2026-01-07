from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from .models import (
	Customer, Category, Product, ProductImage, ProductOffer,
	CategoryOffer, ReferralOffer, ReferralCode, ReferralHistory,
	Coupon, CouponUsage, Review
)


class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'price', 'stock', 'status')
	prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'is_active')


def safe_register(model, admin_class=None):
	try:
		if admin_class:
			admin.site.register(model, admin_class)
		else:
			admin.site.register(model)
	except AlreadyRegistered:
		pass


safe_register(Product, ProductAdmin)
safe_register(Category, CategoryAdmin)
safe_register(ProductImage)
safe_register(ProductOffer)
safe_register(CategoryOffer)
safe_register(ReferralOffer)
safe_register(ReferralCode)
safe_register(ReferralHistory)
safe_register(Coupon)
safe_register(CouponUsage)
safe_register(Review)
safe_register(Customer)
