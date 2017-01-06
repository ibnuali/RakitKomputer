from rest_framework import serializers
from .models import Alamat , Alamatmember ,Barang ,Detailpesanan ,Kategori  , Kecamatan ,Kota ,Member ,Pesanan ,Provinsi , Wishlist

class AlamatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alamat
        fields = '__all__'

class AlamatmemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alamatmember
        fields = '__all__'

class BarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = '__all__'

class DetailpesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detailpesanan
        fields = '__all__'

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class KecamatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kecamatan
        fields = '__all__'
        depth = 3

class KotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kota
        fields = '__all__'
        depth = 2

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class PesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesanan
        fields = '__all__'

class ProvinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinsi
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'