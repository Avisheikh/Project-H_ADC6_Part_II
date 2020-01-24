from django.shortcuts import render,HttpResponseRedirect,reverse
from store.models import *
from django.http import *
from django.db.models import Q
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import permission_required

# Create your views here.
def store(request):
    get_spec = product.objects.all()[0:8]
    return render(request,'store.html',{'prod':get_spec})
# ,{'v_img':get_v}
# def store_add(request,id):
#     add_id = product.objects.get(id=id)
#     return render(request,'cart.html',{'s_id':add_id})



@permission_required('store.add_product', login_url='restricted/')
def admin_page(request):
    obj=product.objects.all()[0:8]  
    return render(request,'CRUD_Inventory/Admin_CRUD_Products.html',{'product':obj})

def admin_restricted(request):
    return render(request,'CRUD_Inventory/restricted.html')

def upload(request):
    return render(request,'CRUD_Inventory/upload.html')
    
def uploaded_save(request):
    if request.method == 'POST':
        getall=request.POST
        name=request.POST['Product_Name']
        typ=request.POST['Product_Type']
        price=request.POST['Product_Price']
        qty=request.POST['Product_Quantity']
        imagee = request.FILES['Product_Image']

        product.objects.create(Product_Name=name, Product_Type=typ,Product_Price=price,Product_Quantity=qty, img=imagee )
    return HttpResponseRedirect('/store/admin_products/')

def get_product(request,id):
    get_id = product.objects.get(id=id)
    return render(request,'CRUD_Inventory/update.html',{'product':get_id})



def update_product(request,id):
    get_id = product.objects.get(id=id)
    get_request = request.POST
    get_id.Product_Name = request.POST['name']
    get_id.Product_Type = request.POST['type']
    get_id.Product_Price = request.POST['price']
    get_id.Product_Quantity = request.POST['qty']
    get_id.save()
    return HttpResponseRedirect('/store/admin_products/')

def delete_product(request,id):
    x = product.objects.get(id = id)
    x.delete()
    return HttpResponseRedirect('/store/admin_products/')
   
def search(request):
    if request.method == 'GET':
        search = request.GET['searchs']

        if search:
            match = product.objects.filter(
                Q( Product_Name__icontains=search) | Q(Product_Type__icontains=search)
            )

            if match:
                return render(request,'CRUD_Inventory/Admin_CRUD_Products.html',{'sr':match})

            else:
                messages.error(request,'No Result Found')

        else:
            return HttpResponseRedirect('/store/admin_products/')

    return render(request, 'CRUD_Inventory/Admin_CRUD_Products.html')

def store_search(request):
    if request.method == 'GET':
        search = request.GET['search']

        if search:
            match = product.objects.filter(
                Q( Product_Name__icontains=search) | Q(Product_Type__icontains=search)
            )

            if match:
                return render(request,'store.html',{'search':match})

            else:
                messages.error(request,'No Result Found')

        else:
            return HttpResponseRedirect('/store/')

    return render(request, 'store.html')

def upload_list(request):
    list_upload = upload_files.objects.all()
    return render(request,'CRUD_Inventory/uploaded.html',{'lists':list_upload})

    

def upload_file(request):
    if request.method == 'POST':
        form = request.POST 
        uploaded_file = request.FILES['document']
        file_namee = request.POST['file']
        file_type = request.POST['format']
        upload_files.objects.create(File_Name = file_namee,File_Type =file_type, pdf=uploaded_file)
        
        
    return render(request,'CRUD_Inventory/upload_file.html')

def run(request,id):
    a = upload_files.objects.get(id=id)
    a.delete()
    return HttpResponseRedirect('/store/admin_products/uploaded_file/')

# def uploaded_file(request):
#     return render(request,)


def pagination(request,pageNo):
    get_all = product.objects.all()
    if request.method == "GET":
        if pageNo == 1:
            pageNo=0
            count=0
            for i in range(8):
                try:
                    if get_all.get(id=i+1) is not None:
                       count=count+1
                    else:
                       break
                except:
                    pass
            get_spec=get_all[pageNo:count]
            return render(request,'store.html',{'v_img':get_spec})
        else:
            count=0
            i=(pageNo-1)*8
            for i in range(pageNo*8):
                try:
                    if get_all.get(id=i+1) is not None:
                        count=i+1
                    else:
                        break
                except:
                    pass
            get_spec=get_all[(pageNo-1)*8:count]
            return render(request,'store.html',{'v_img':get_spec})


def paginationForCRUD(request,pageNo):
    get_all=product.objects.all()
    if request.method == "GET":
        if pageNo == 1:
            pageNo=0
            count=0
            for i in range(8):
                try:
                    if get_all.get(id=i+1) is not None:
                       count=count+1
                    else:
                       break
                except:
                    pass
            get_spec=get_all[pageNo:count]
            return render(request,'CRUD_Inventory/Admin_CRUD_Products.html',{'prod':get_spec})
        else:
            count=0
            i=(pageNo-1)*8
            for i in range(pageNo*8):
                try:
                    if get_all.get(id=i+1) is not None:
                        count=i+1
                    else:
                        break
                except:
                    pass
            get_spec=get_all[(pageNo-1)*8:count]
            return render(request,'CRUD_Inventory/Admin_CRUD_Products.html',{'prod':get_spec})



