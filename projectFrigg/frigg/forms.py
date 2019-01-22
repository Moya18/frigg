from django import forms

class QuoteForm(forms.Form):
    client = forms.CharField()
    date = forms.DateField()
    printFile = forms.CharField()
    orentationFile = forms.CharField()
    material = forms.CharField()
    layerThickness = forms.CharField()
    infill = forms.CharField()
    supports = forms.CharField()
    speed = forms.CharField()
    time = forms.CharField()
    weight = forms.CharField()
    quantity = forms.CharField()
    delivery = forms.CharField()
    showCost = forms.CharField()

class ClientForm(forms.Form):
    name = forms.CharField()
    company = forms.CharField()
    email = forms.CharField()
    rfc = forms.CharField()
    telephone = forms.CharField()
    addressLine1 = forms.CharField()
    addressLine2 = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    zip = forms.CharField()

class ApproveForm(forms.Form):
    quoteID = forms.CharField()