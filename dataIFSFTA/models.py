from django.db import models

class Tbusers(models.Model):
    uid = models.IntegerField(db_column='UID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30)  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.
    foto = models.TextField(db_column='Foto')  # Field name made lowercase.
    typetalents = models.CharField(db_column='TypeTalents', max_length=50)  # Field name made lowercase.
    detailtalents = models.TextField(db_column='DetailTalents')  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=30)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=30)  # Field name made lowercase.
    contactnumber = models.IntegerField(db_column='ContactNumber')  # Field name made lowercase.
    ktp = models.TextField(db_column='KTP')  # Field name made lowercase.
    videolinks = models.TextField(db_column='Videolinks', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbusers'
