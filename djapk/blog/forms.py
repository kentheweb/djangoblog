from django import forms


class addPost(forms.Form):
    title = forms.CharField(max_length=60, widget=forms.TextInput(attrs={
        'placeholder' : 'enter your blog title',
        'class': 'form-control form-control-sm'
    }))
    post = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'type your blog here',
        'class': 'form-control form-control-sm'
    }))
