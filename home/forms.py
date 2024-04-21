from django import forms
from.models import Handover, Notices, Comment

class handoverForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['Shift'].widget.attrs.update({"class":'form-control'})
        self.fields['Handover_From'].widget.attrs.update({"class":'form-control'})
        self.fields['Handover_To'].widget.attrs.update({"class":'form-control'})
        self.fields['title'].widget.attrs.update({"class":'form-control-1'})
        #self.fields['Handover_To'].widget.attrs.update({"class":'form-control'})
        #self.fields['Handover_To'].widget.attrs.update({"class":'form-control'})

    class Meta:
        model=Handover
        fields= ['Shift','Handover_From','Handover_To','title','Tasks_In_Progress','Important_Notes']



class NoticeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'Notice-form'})
    class Meta:
        model=Notices
        fields='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment_by','remarks']
        