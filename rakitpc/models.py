# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Alamat(models.Model):
    id_alamat = models.CharField(db_column='ID_ALAMAT', primary_key=True, max_length=15)  # Field name made lowercase.
    id_kecamatan = models.ForeignKey('Kecamatan', models.DO_NOTHING, db_column='ID_KECAMATAN')  # Field name made lowercase.
    id_kota = models.ForeignKey('Kota', models.DO_NOTHING, db_column='ID_KOTA')  # Field name made lowercase.
    id_provinsi = models.ForeignKey('Provinsi', models.DO_NOTHING, db_column='ID_PROVINSI')  # Field name made lowercase.
    alamat = models.CharField(db_column='ALAMAT', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    kode_pos = models.CharField(db_column='KODE_POS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALAMAT'
    
    def __str__(self):
        return self.alamat

class Alamatmember(models.Model):
    id_alamatmember = models.CharField(db_column='ID_ALAMATMEMBER', primary_key=True, max_length=7)  # Field name made lowercase.
    id_alamat = models.ForeignKey(Alamat, models.DO_NOTHING, db_column='ID_ALAMAT')  # Field name made lowercase.
    id_member = models.ForeignKey('Member', models.DO_NOTHING, db_column='ID_MEMBER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALAMATMEMBER'
    def __str__(self):
        return self.alamat

class Barang(models.Model):
    id_barang = models.CharField(db_column='ID_BARANG', primary_key=True, max_length=10)  # Field name made lowercase.
    id_kategori = models.ForeignKey('Kategori', models.DO_NOTHING, db_column='ID_KATEGORI', blank=True, null=True)  # Field name made lowercase.
    nama_barang = models.CharField(db_column='NAMA_BARANG', max_length=60, blank=True, null=True)  # Field name made lowercase.
    harga_barang = models.IntegerField(db_column='HARGA_BARANG', blank=True, null=True)  # Field name made lowercase.
    deskripi = models.CharField(db_column='DESKRIPI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gambar = models.CharField(db_column='GAMBAR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    stok = models.IntegerField(db_column='STOK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BARANG'

    def __str__(self):
        return self.nama_barang

class Detailpesanan(models.Model):
    id_detailpesanan = models.CharField(db_column='ID_DETAILPESANAN', primary_key=True, max_length=7)  # Field name made lowercase.
    id_barang = models.ForeignKey(Barang, models.DO_NOTHING, db_column='ID_BARANG')  # Field name made lowercase.
    id_pesanan = models.ForeignKey('Pesanan', models.DO_NOTHING, db_column='ID_PESANAN', blank=True, null=True)  # Field name made lowercase.
    kuantitas = models.IntegerField(db_column='KUANTITAS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DETAILPESANAN'

    def __str__(self):
        return self.id_detailpesanan


class Kategori(models.Model):
    id_kategori = models.CharField(db_column='ID_KATEGORI', primary_key=True, max_length=4)  # Field name made lowercase.
    nama_kategori = models.CharField(db_column='NAMA_KATEGORI', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KATEGORI'
    
    def __str__(self):
        return self.nama_kategori

class Kecamatan(models.Model):
    id_kecamatan = models.CharField(db_column='ID_KECAMATAN', primary_key=True, max_length=7)  # Field name made lowercase.
    id_kota = models.ForeignKey('Kota', models.DO_NOTHING, db_column='ID_KOTA')  # Field name made lowercase.
    nama_kecamatan = models.CharField(db_column='NAMA_KECAMATAN', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KECAMATAN'
    
    def __str__(self):
        return self.nama_kecamatan

class Kota(models.Model):
    id_kota = models.CharField(db_column='ID_KOTA', primary_key=True, max_length=4)  # Field name made lowercase.
    id_provinsi = models.ForeignKey('Provinsi', models.DO_NOTHING, db_column='ID_PROVINSI')  # Field name made lowercase.
    nama_kota = models.CharField(db_column='NAMA_KOTA', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KOTA'

    def __str__(self):
        return self.nama_kota

class Member(models.Model):
    id_member = models.CharField(db_column='ID_MEMBER', primary_key=True, max_length=15)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=15, blank=True, null=True)  # Field name made lowercase.
    no_hp = models.CharField(db_column='NO_HP', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEMBER'

    def __str__(self):
        return self.nama

class Pesanan(models.Model):
    id_pesanan = models.CharField(db_column='ID_PESANAN', primary_key=True, max_length=10)  # Field name made lowercase.
    id_member = models.ForeignKey(Member, models.DO_NOTHING, db_column='ID_MEMBER')  # Field name made lowercase.
    tanggal_pesanan = models.DateTimeField(db_column='TANGGAL_PESANAN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PESANAN'

    def __str__(self):
        return self.tanggal_pesanan

class Provinsi(models.Model):
    id_provinsi = models.CharField(db_column='ID_PROVINSI', primary_key=True, max_length=2)  # Field name made lowercase.
    nama_provinsi = models.CharField(db_column='NAMA_PROVINSI', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROVINSI'

    def __str__(self):
        return self.nama_provinsi

class Wishlist(models.Model):
    id_wishlist = models.CharField(db_column='ID_WISHLIST', primary_key=True, max_length=8)  # Field name made lowercase.
    id_barang = models.ForeignKey(Barang, models.DO_NOTHING, db_column='ID_BARANG')  # Field name made lowercase.
    id_member = models.ForeignKey(Member, models.DO_NOTHING, db_column='ID_MEMBER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WISHLIST'
        
    def __str__(self):
        return self.id_wishlist

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
