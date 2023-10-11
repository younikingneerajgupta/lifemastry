from django import forms
from .models import UserProfile
from django.conf import settings

class UserProfileForm(forms.ModelForm):
    select_classes = [
        ('class i', 'Class I'),
        ('class ii', 'Class II'),
        ('class iii', 'Class III'),
        ('class iv', 'Class IV'),
        ('class v', 'Class V'),
        ('class vi', 'Class VI'),
        ('class vii', 'Class VII'),
        ('class viii', 'Class VIII'),
        ('class ix', 'Class IX'),
        ('class x', 'Class X'),
        ('class xi', 'Class XI'),
        ('class xii', 'Class XII'),
    ]
    
    select_class = forms.ChoiceField(choices=select_classes, required=False)

    class Meta:
        model = UserProfile
        fields = [
            'full_name',
            'email',
            'profile_image',
            'address',
            'phone_number',
            'mode',
            'skills',
            'subjects',
            'password',
            'role',
        ]
    
    def clean_profile_image(self):
        profile_image = self.cleaned_data.get('profile_image')
        if profile_image:
            if profile_image.size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError("File size is too large. Maximum allowed size is 5MB.")
            return profile_image
        else:
            raise forms.ValidationError("Couldn't read uploaded image.")
