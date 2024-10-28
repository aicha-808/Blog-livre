from django import forms
from articles.models import Livre


class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre # Utilisez le modèle Livre
        fields = ['titre','resume', 'contenu', 'image', 'lien_pdf', 'audio'] # Champs que je souhaite inclure dans le formulaire
        widgets = {
            'titre': forms.TextInput(attrs={'class':'form-control'}),
            'resume': forms.TextInput(attrs={'class':'form-control'}),
            'contenu': forms.Textarea(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'lien_pdf': forms.URLInput(attrs={'class': 'form-control'}),
            'audio':forms.URLInput(attrs={'class': 'form-control'})   
            }
       
