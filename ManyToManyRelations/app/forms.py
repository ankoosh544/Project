from django import forms
from app.models import CustomerModel,FoodItemsModel
import re

class FoodItemsForm(forms.ModelForm):
    class Meta:
        model = FoodItemsModel
        fields = "__all__"
    def clean_ino(self):
        res = self.cleaned_data["ino"]
        if res < 100:
            return res
        else:
            raise forms.ValidationError("Invalid Item Number")

    def clean_name(self):
        name = self.cleaned_data["name"]
        if re.findall(r"^[a-z,A-Z]*$", name):
            return name
        else:
            raise forms.ValidationError("Invalid Item Name")

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = "__all__"

    def clean_cno(self):
        no = self.cleaned_data["cno"]
        if no<1000:
            return no
        else:
            raise forms.ValidationError("Invalid Customer Number")
    def clean_cname(self):
        name = self.cleaned_data["cname"]
        if re.findall(r"^[a-z,A-Z]*$", name):
            return name
        else:
            raise forms.ValidationError("Invalid Customer Name")


