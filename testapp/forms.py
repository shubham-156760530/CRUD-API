from django import forms

class EmployeeForm(forms.ModelForm):
    def clear_esal():
        inputsal=self.cleaned_data['esal']
        if inputsal<500:
            raise forms.ValidationError('Minimum Salary should be 5000')
        return inputsal
    class Meta:
        model = Employee
        fields = '__all__'
