from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field


class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('name', placeholder="Enter your name"),
            Field('email', placeholder="Enter your email"),
            Field('message', placeholder="Enter your message"),
            Submit('submit', 'Submit', css_class="btn-warning"),
        )
