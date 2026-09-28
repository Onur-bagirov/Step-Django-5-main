from django import forms

from .models import Comment, Post
from .models import Category

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "text"]
        labels = {"name": "Adın", "text": "Rəyin"}
        
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 2:
            raise forms.ValidationError("Ad ən azı 2 simvol olmalıdır.")
        if name.lower() == "admin":
            raise forms.ValidationError("Bu adla şərh yazmaq olmaz.")
        return name
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "author", "content", "category", "image", "tags"]
        labels = {
            "title": "Başlıq",
            "author": "Müəllif",
            "content": "Məzmun",
            "category": "Kateqoriya",
            "content": "Məzmun",
            "image": "Şəkil",
            "tags": "Təqlər",
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 5:
            raise forms.ValidationError("Başlıq ən azı 5 simvol olmalıdır.")
        if title.isupper():
            raise forms.ValidationError("Başlığı tam böyük hərflə yazma.")
        return title


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Adın")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Mesaj")

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if len(message) < 10:
            raise forms.ValidationError("Mesaj ən azı 10 simvol olmalıdır.")
        return message


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "slug", "description"]
        labels = {"name": "Ad", "slug": "Slug", "description": "Təsvir"}