from django.forms import ModelForm

from .models import Visit, Study, GroupSet, Group, SampleType

class VisitForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(VisitForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control',})
            
    class Meta:
        model = Visit
        exclude = ('number',)
        
class StudyForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudyForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control',})
            
    class Meta:
        model = Study
        fields = '__all__'
		
class GroupSetForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(GroupSetForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control',})
            
    class Meta:
        model = GroupSet
        exclude = ()
		
class GroupForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control',})
            
    class Meta:
        model = Group
        exclude = ()
		
class SampleTypeForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SampleTypeForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control',})
            
    class Meta:
        model = SampleType
        exclude = ('number',)