from django import forms
from .models import Person, Game


# to sync person model to form
class NewUserForm(forms.ModelForm):
    class Meta():
        model = Person
        exclude = ["userForeignKey"]
        fields = '__all__'


# to sync game model to form
class NewGameForm(forms.ModelForm):
    class Meta():
        model = Game
        exclude = ["collectorForeignKey"]
        fields = '__all__'


        # AGE LIMIT VALIDATION
    def clean_ageLimit(self):
        agelimit = self.cleaned_data["ageLimit"]

        if agelimit < 12:
            raise forms.ValidationError("Not Required Age")

        return agelimit


    #
    # def clean_dateMade(self):
    #     datemade = self.cleaned_data["dateMade"]
    #
    #     if datemade < 1960:
    #         raise forms.ValidationError("Games didnt exist then, or did they?")
    #
    #     return datemade