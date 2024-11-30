from django import forms

from news.models import Post


class EditPostForm(forms.ModelForm):
	category = forms.ChoiceField(choices=(
		('Администрация', 'Администрация'),
		('Совет депутатов', 'Совет депутатов')
	), label='Категория')

	class Meta:
		model = Post
		fields = ['title', 'file', 'category']
