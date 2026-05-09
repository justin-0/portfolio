from django import forms
from .models import AboutMe, Skill, Project, Certificate

class BaseGlassForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.Textarea, forms.EmailInput, forms.URLInput, forms.NumberInput, forms.Select)):
                field.widget.attrs['class'] = 'glass-input'

class AboutMeForm(BaseGlassForm):
    class Meta:
        model = AboutMe
        fields = '__all__'

class SkillForm(BaseGlassForm):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectForm(BaseGlassForm):
    class Meta:
        model = Project
        fields = '__all__'

class CertificateForm(BaseGlassForm):
    class Meta:
        model = Certificate
        fields = '__all__'
