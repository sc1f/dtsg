from django.forms import ModelForm
from elections.models import Candidate
from django.utils.translation import gettext_lazy as _
from tinymce.widgets import TinyMCE

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ['name','position','major','year','image','image_credit','statement','platform','website','facebook','twitter']
        labels = {
            'name': _("What's your name?"),
            'major': _("What's your major?"),
            'position': _("What position are you running for?"),
            'year': _("What year are you?"),
            'image': _("Upload a photo of yourself"),
            'image_credit': _("Who took this photo?"),
            'statement': _("What's your campaign statement?"),
            'platform': _("What's your platform?"),
            'website': _("Website (optional)"),
            'facebook': _("Facebook (optional)"),
            'twitter': _("Twitter (optional)")
        }
        help_texts = {
            'image': _('IMAGE MUST BE LESS THAN 4MB, or you will receive an error. If you receive an error, compress your image and reupload it. Try to upload a square image, or make sure your face is near the center of the frame.'),
            'facebook': _("Full URL please."),
            'twitter': _("Full URL please.")
        }