from django.db import models

class Auction(models.Model):

	art_id = models.IntegerField()
	highest_bid = models.IntegerField(default=0)
	highest_bidder = models.CharField(max_length=42,default="Unknown")
	owner =  models.CharField(max_length=42,default="XYZ")
	base_price = models.IntegerField(default=0)

	def __str__(self):
	 	return self.highest_bidder