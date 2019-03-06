from django import forms
from .models import Person, Game


# to sync person model to form
class NewUserForm(forms.ModelForm):
    class Meta():
        model = Person
        # SO FOREIGN KEY WILL NOT SHOW IN USER VIEW
        exclude = ["userForeignKey"]
        fields = '__all__'

# TO VALIDATE PASSWORDS
    def clean(self):
        # GRABBING PASSWORD OBJECTS
        pass1 = self.cleaned_data["password1"]
        pass2 = self.cleaned_data["password2"]

        # IN THE CASE THAT THEY DO NO MATCH
        if pass1 != pass2:
            raise forms.ValidationError("Passwords Do Not Match")

        # RETURN CANT CALL SPECIFIC VARIABLE, DOESNT WORK IF ONE IS CALLED
        return


# to sync game model to form
class NewGameForm(forms.ModelForm):
    class Meta():
        model = Game
        # SO FOREIGN KEY WILL NOT SHOW IN USER VIEW
        exclude = ["collectorForeignKey"]
        fields = '__all__'


        # AGE LIMIT VALIDATION
    def clean_ageLimit(self):
        agelimit = self.cleaned_data["ageLimit"]

        if agelimit < 12:
            raise forms.ValidationError("Not Required Age")

        return agelimit


    #AN ATTEMPT TO VALIDATE DATES..DONT RUN IT WITH CODE
    # def clean_dateMade(self):
    #     datemade = self.cleaned_data["dateMade"]
    #
    #     if datemade < 1960:
    #         raise forms.ValidationError("Games didnt exist then, or did they?")
    #
    #     return datemade