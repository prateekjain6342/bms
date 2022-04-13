from django.db import models

# Create your models here.

class StateMaster(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField()

    class Meta:
    	db_table = 'state_master'

class CityMaster(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField()
    state = models.ForeignKey(StateMaster, on_delete=models.CASCADE, to_field='id')

    class Meta:
    	db_table = 'city_master'

class CinemaMaster(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField()
    city = models.ForeignKey(CityMaster, on_delete=models.CASCADE, to_field='id')
    state = models.ForeignKey(StateMaster, on_delete=models.CASCADE, to_field='id')

    class Meta:
    	db_table = 'cinema_master'


class AudiMaster(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField()
    seating_arrangment = models.TextField()
    cinema = models.ForeignKey(AudiMaster, on_delete=models.CASCADE, to_field='id')

    class Meta:
    	db_table = 'audi_master'

class MovieMaster(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    run_time = models.TimeField(null=True, blank=True)

    class Meta:
    	db_table = 'movie_master'

class MovieTimings(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(MovieMaster, on_delete=models.CASCADE, to_field='id')
    start_time = models.DateTimeField()
    cinema = models.ForeignKey(CinemaMaster, on_delete=models.CASCADE, to_field='id')
    audi = models.ForeignKey(AudiMaster, on_delete=models.CASCADE, to_field='id')

    class Meta:
    	db_table = 'movie_timings'

class Bookings(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie_timing = models.ForeignKey(MovieTimings, on_delete=models.CASCADE, to_field='id')

    class Meta:
    	db_table = 'bookings'
