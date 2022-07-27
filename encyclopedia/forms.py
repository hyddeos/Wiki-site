from django import forms

class EntryForm(forms.Form):
 
    title = forms.CharField(max_length = 100)
    text = forms.CharField(max_length = 2000, widget=forms.Textarea)

class EditForm(forms.Form):

    text = forms.CharField(max_length = 2000, widget=forms.Textarea) 
    
    def __init__(self, *args, **kwargs):
    
        super().__init__(*args, **kwargs)
        self.fields['text'].initial = "hej"
