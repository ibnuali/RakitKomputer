from .models import Alamat , Alamatmember ,Barang ,Detailpesanan ,Kategori , Kecamatan ,Kota ,Member ,Pesanan ,Provinsi , Wishlist
from rest_framework import viewsets , permissions
from .serializers import AlamatSerializer, AlamatmemberSerializer ,BarangSerializer ,DetailpesananSerializer ,KategoriSerializer ,KecamatanSerializer ,KotaSerializer ,MemberSerializer ,PesananSerializer ,ProvinsiSerializer ,WishlistSerializer 
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class AlamatViewSet(viewsets.ModelViewSet):

    queryset = Alamat.objects.all()
    serializer_class = AlamatSerializer

class AlamatmemberViewSet(viewsets.ModelViewSet):

    queryset = Alamatmember.objects.all()
    serializer_class = AlamatmemberSerializer

class BarangViewSet(viewsets.ModelViewSet):

    queryset = Barang.objects.all()
    serializer_class = BarangSerializer

class DetailViewSet(viewsets.ModelViewSet):

    queryset = Detailpesanan.objects.all()
    serializer_class = DetailpesananSerializer

class KategoriViewSet(viewsets.ModelViewSet):

    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class KecamatanViewSet(viewsets.ModelViewSet):

    queryset = Kecamatan.objects.all()
    serializer_class = KecamatanSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class KotaViewSet(viewsets.ModelViewSet):

    queryset = Kota.objects.all()
    serializer_class = KotaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
class MemberViewSet(viewsets.ModelViewSet):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class PesananViewSet(viewsets.ModelViewSet):

    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer

class ProvinsiViewSet(viewsets.ModelViewSet):

    queryset = Provinsi.objects.all()
    serializer_class = ProvinsiSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
class WishlistViewSet(viewsets.ModelViewSet):

    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer