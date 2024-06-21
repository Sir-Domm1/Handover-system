from django import forms
from.models import Handover, Notices, Comment


class handoverForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['Shift'].widget.attrs.update({"class":'form-control'})
        
        self.fields['Handover_To'].widget.attrs.update({"class":'form-control'})
        self.fields['title'].widget.attrs.update({"class":'form-control-1'})
        #self.fields['Handover_To'].widget.attrs.update({"class":'form-control'})
        #self.fields['Handover_To'].widget.attrs.update({"class":'form-control'})

    class Meta:
        model=Handover
        exclude = ['Handover_From', 'completed_by', 'Completed_task', 'Date'] 



class NoticeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'Notice-form'})
    class Meta:
        model=Notices
        exclude = ['Notice_by'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['remarks']


        