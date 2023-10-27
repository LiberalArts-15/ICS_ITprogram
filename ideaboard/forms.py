from django import forms
from .models import Post, User

class PostForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=(
            ('all', '自由'),
            ('minutes', '会議録'),
            ('notice', 'お知らせ'),
        ),
        widget=forms.Select(attrs={'id': 'post-category', 'name': 'category'}),
    )

    class Meta:
        model = Post
        fields = [
            "title",
            "keyword",
            "content",
            "image1",
            "image2",
            "image3",
            "content",
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
         "username",
         "profile_pic",
         "intro",   
        ]
        widgets = {
            "intro": forms.Textarea,
        }