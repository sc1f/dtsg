from django.forms import ModelForm
from elections.models import Candidate
from django.utils.translation import gettext_lazy as _

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ['name','position','major','year','image','image_credit','statement','platform','website','facebook','twitter']
        labels = {
            'name': _("What's your name?"),
            'race': _("Which race are you running in?"),
            'position': _("What position are you running for?"),
        }