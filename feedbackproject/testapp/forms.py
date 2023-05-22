from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.CharField()
    feedback=forms.CharField(widget=forms.Textarea)