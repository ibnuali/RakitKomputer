from django.contrib import admin
from .models import Alamat , Alamatmember ,Barang ,Detailpesanan ,Kategori , Kecamatan ,Kota ,Member ,Pesanan ,Provinsi , Wishlist
# Register your models here.

admin.site.register(Alamat),
admin.site.register(Alamatmember),
admin.site.register(Barang),
admin.site.register(Detailpesanan),
admin.site.register(Kategori),
admin.site.register(Kecamatan),
admin.site.register(Kota),
admin.site.register(Member),
admin.site.register(Pesanan),
admin.site.register(Provinsi),
admin.site.register(Wishlist)
