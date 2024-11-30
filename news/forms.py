from django import forms

from news.models import Post


class EditPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'file']
