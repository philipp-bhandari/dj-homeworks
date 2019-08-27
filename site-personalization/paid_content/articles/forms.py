from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class ProfileRegisterForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''
