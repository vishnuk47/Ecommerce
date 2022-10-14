from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'baabtra/baabtrahome.html')
def page(request):
    return render(request,'baabtra/baabtrapage.html')
def about(request):
    return render(request,'baabtra/aboutus.html')
def sample(request):
    return render(request,'baabtra/sample.html')  
def cssexa(request):
    return render(request,'baabtra/cssexa.html')
def newpage(request):
    return render(request,'baabtra/newpage.html')  
def pad(request):
    return render(request,'baabtra/paddin.html')
def grid(request):
    return render(request,'baabtra/grid.html')
def grid1(request):
    return render(request,'baabtra/grid1.html')
def boot(request):
    return render(request,'baabtra/bootstrap.html')
def boots(request):
    return render(request,'baabtra/bootsgrid.html')
def baabtra(request):
    return render(request,'baabtra/baabtraindex.html')
def boo(request):
    return render(request,'baabtra/bootstrapgrids.html')       