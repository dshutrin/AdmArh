from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=500, verbose_name='Название поста')
	file = models.FileField(upload_to='posts/', verbose_name='Файл (не обязательно)', null=True, blank=True, default=None)
	category = models.CharField(max_length=100, verbose_name='Категория', null=True, blank=True, default=None)
	pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
	author = models.CharField(max_length=255, verbose_name='Автор публикации', default=None, null=False)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'
