from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    subject = forms.CharField(label='Subject', max_length=50)
    message = forms.CharField(label='Message', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        content = f"{name}\nE-mail: {email}\nSubject: {subject}\nMessage: {message}"

        mail = EmailMessage(
            subject="Email from django intermediate",
            body=content,
            from_email='marcus-v@outlook.com',
            headers={"Reply-To": email}
        )
        mail.send()


