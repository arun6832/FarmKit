from django import forms

class SoilDataForm(forms.Form):
    nitrogen_level = forms.FloatField(label='Nitrogen Level', required=True)
    phosphorus_level = forms.FloatField(label='Phosphorus Level', required=True)
    potassium_level = forms.FloatField(label='Potassium Level', required=True)
    temperature = forms.FloatField(label='Temperature (°C)', required=True)
    humidity_level = forms.FloatField(label='Humidity Level (%)', required=True)
    ph_level = forms.FloatField(label='pH Level', required=True)
    rainfall = forms.FloatField(label='Rainfall (mm)', required=True)
