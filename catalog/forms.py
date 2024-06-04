from django.forms import ModelForm, forms

from catalog.models import Product


class ProductForm(ModelForm):
    stop_word = (
        "казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар"
    )

    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        cleaned_data = self.cleaned_data.get("name")

        if cleaned_data.lower() in self.stop_word:
            raise forms.ValidationError(f" {cleaned_data} - Недопустимое название")
        else:
            return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get("description")

        for word in cleaned_data.split():
            if word.lower() in self.stop_word:
                raise forms.ValidationError(f"{word} - запрещенное слово в описании")
            else:
                continue
        return cleaned_data
