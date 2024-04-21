from django.shortcuts import render,redirect, get_object_or_404
from.forms import handoverForm, NoticeForm,CommentForm
from.models import Handover,Notices,Comment

# Create your views here.
#creating home page which contains the forms
def Home(request):
    if request.method=='POST':
        form=handoverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('handover-page')
    else:
        form=handoverForm()
    return render(request, 'index.html',{'form':form})

#creating the page to display all the handovers

def Handover_list(request):
    display=Handover.objects.all()
    incomplete_handovers = Handover.objects.filter(Completed_task=False)
    if request.method=='POST':
        handover_id=request.POST.get('id')
        turnover= Handover.objects.get(id=handover_id)
        turnover.Completed_task=True
        turnover.completed_by = request.user
        turnover.save()
        #return redirect('completed-handovers')

       
    return render(request, 'handover.html',{'display':display,'incomplete_handovers':incomplete_handovers})


#create views for completed handover only.
def Completed_handovers(request):
    display_completed=Handover.objects.filter(Completed_task=True)
    return render(request, 'completed.html',{'display_completed': display_completed})

def Notice(request):
    
    if request.method=='POST':
        form= NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notice-display-page')
    else:
        form=NoticeForm()

    return render(request, 'notice.html', {'form':form})

def Notice_Display(request):
    All_display=Notices.objects.all()
    return render(request, 'notice-display.html',{'All_display':All_display})

def opinion(request, pk):
    publish=get_object_or_404(Notices, pk=pk)
    feedback=Comment.objects.filter(notice=publish)
    new_form=None

    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.notice=publish
            new_form.comment_by = request.user 
            new_form.save()
        return redirect('comment-page', pk=publish.pk)
    else:
        form=CommentForm()
    return render(request,'comments.html',{'publish':publish,
                                           'feedback':feedback,
                                           'form':form,
                                           'pk':pk,
                                           'new_form':new_form,
                                           'CommentForm':CommentForm

    } )
        

def data(request,pk):
    Handover_details=get_object_or_404(Handover,pk=pk)
    return render(request,'details.html', {'Handover_details':Handover_details})