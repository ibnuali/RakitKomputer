from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rakitpc import views

router = routers.DefaultRouter()
router.register(r'Alamat', views.AlamatViewSet)
router.register(r'AlamatMember', views.AlamatmemberViewSet)
router.register(r'Barang', views.BarangViewSet)
router.register(r'DetailPesanan', views.DetailViewSet)
router.register(r'Kategori', views.KategoriViewSet)
router.register(r'Kecamatan', views.KecamatanViewSet)
router.register(r'Kota', views.KotaViewSet)
router.register(r'Member', views.MemberViewSet)
router.register(r'Pesanan', views.PesananViewSet)
router.register(r'Provinsi', views.ProvinsiViewSet)
router.register(r'Wishlist', views.WishlistViewSet)

schema_view = get_swagger_view(title='RakitPC API')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/docs/', schema_view)
]
