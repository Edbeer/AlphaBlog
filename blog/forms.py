from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(max_length=150, label='Title', widget=forms.TextInput(attrs={"class": "form-control"}))
    slug = forms.SlugField(max_length=150, label='URL', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Content', required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
    photo = forms.ImageField(label='IMG', required=False)
    is_published = forms.BooleanField(label='Published', initial=True)

