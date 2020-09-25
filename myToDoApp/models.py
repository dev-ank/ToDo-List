from django.db import models



class Content(models.Model):
	text=models.CharField(max_length=200)
	time=models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.text}'
