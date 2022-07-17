from django import forms

from .models import postModel


class postForm(forms.ModelForm):
    class Meta:
        model = postModel
        fields = [
            'author',
            'judul',
            'kategori',
            'konten',
        ]
        widgets = {
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukan nama penulis'
                }
            ),
            'judul': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukan Judul'
                }
            ),
            'kategori': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'konten': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }
