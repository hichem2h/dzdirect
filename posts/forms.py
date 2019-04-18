from django import forms
from .models import Video, Message


class VideoForm(forms.ModelForm):

    def save(self, request):
        self.instance.user = request.user
        self.instance.save()

    class Meta:
        model = Video
        fields = ['title', 'category', 'description', 'video']


class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=30,
                           label='Nom',
                           widget=forms.TextInput(
                                   attrs={'placeholder':
                                          'Nom',
                                          'autofocus': 'autofocus'}))
    email = forms.EmailField(required=True, label='Email',
                             widget=forms.TextInput(
                                    attrs={'placeholder':
                                           'Email',
                                           'autofocus': 'autofocus'}))
    message = forms.CharField(required=True, max_length=1024,
                              label='Message',
                              widget=forms.Textarea(
                                   attrs={'placeholder':
                                          'Message',
                                          'autofocus': 'autofocus',
                                          'class': 'form-control'}))

    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
