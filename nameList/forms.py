from django import forms

class InsertInstallmentForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    address_diffshift = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    prename = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'js-data-prename-ajax w-100 select2-lg', 'required': 'required'})
    )

    def __init__(self, *args, **kwargs):
        prename_choices = kwargs.pop('prename_choices', [])
        super().__init__(*args, **kwargs)
        
        self.fields['prename'].choices = [('', '-- เลือกคำนำหน้า --')] + prename_choices
