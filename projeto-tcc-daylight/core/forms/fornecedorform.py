# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.fornecedormodel import Fornecedor


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'

        widgets = {
            'fornecedorname': forms.TextInput(attrs={'class':'form-control form-control-sm textcapitalize'}),
            'email': forms.EmailInput(attrs={'class':'form-control form-control-sm textlowercase'}),
            'numero_fiscal': forms.TextInput(attrs={'class':'form-control form-control-sm cpfcnpj'}),
            'endereco': forms.TextInput(attrs={'class':'form-control form-control-sm textcapitalize rua'}),
            'bairro': forms.TextInput(attrs={'class':'form-control form-control-sm textcapitalize bairro'}),
            'cidade': forms.TextInput(attrs={'class':'form-control form-control-sm textcapitalize cidade'}),
            'cep': forms.TextInput(attrs={'class':'form-control form-control-sm cep'}),
            'uf': forms.TextInput(attrs={'class':'form-control form-control-sm textuppercase uf'}),
            'telefone': forms.TextInput(attrs={'class':'form-control form-control-sm telefone'}),
            'class_fiscal': forms.Select(attrs={'class':'form-control form-control-sm class_fiscal'}),
            }
