from django.shortcuts import render
from restapi.models import product
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create or View Product 
@csrf_exempt
def View_And_Create(request):
    
    if request.method == "GET":
        try:
            prod_obj=product.objects.all()
            con_json_obj=list(prod_obj.values("product_name","product_type","product_price"))
            py_dict={"ProductDetails":con_json_obj}
            return JsonResponse(py_dict)
        except:
            return JsonResponse({"Message":"Data Doesnot Exist"})
    

    if request.method == "POST":
        print(request.body)
        py_dict_obj=json.loads(request.body)
        product.objects.create(product_name=py_dict_obj['productName'],
        product_type=py_dict_obj['productType'],
        product_price=py_dict_obj['productPrice'])
        return JsonResponse({"message":"successfully created row in database"})
    

# View, Delete, Update specific product by Id
@csrf_exempt
def ViewId_Delete_Update(request,Id):
    try:
        get_details=product.objects.get(id=Id)
    
        if request.method == "GET":
            return JsonResponse({
            "product_name":get_details.product_name,
            "product_type":get_details.product_type,
            "product_price":get_details.product_price})
    

        elif request.method == "DELETE":
            get_details.delete()
            return JsonResponse({"message":"Deleted"})
                
                
        elif request.method == "PUT":
            update=json.loads(request.body) 
            get_details.product_name=update['productName']
            get_details.product_type=update['productType'] 
            get_details.product_price=update['productPrice']
            get_details.save()
            return JsonResponse({"message":"Updated"})
    except:
        return JsonResponse({"Message":"Data doesnot Exists"})    

@csrf_exempt
def pagination(request,pageNo,Size):
    get_prod=product.objects.all()
    get_prod_slice=None
    
    if request.method == "GET":

        strt_slice=(pageNo-1) * Size
        end_slice=(pageNo-1) * Size
        max_len=pageNo * Size
        data_avilbl=get_prod.count()

        while end_slice < data_avilbl and end_slice < max_len:
            get_prod_slice=get_prod[strt_slice:end_slice+1]
            end_slice=end_slice+1
        try:
            conv_list=list(get_prod_slice.values("product_name","product_type","product_price"))
            conv_dict={"ProductDetails":conv_list}
            return JsonResponse(conv_dict)
        except:
            return JsonResponse({"Message":"Data is not available for page No {}".format(pageNo)})
    




