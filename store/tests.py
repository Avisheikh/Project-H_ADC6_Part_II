from django.test import TestCase, Client
from .models import *
from .views import *
from django.urls import reverse
import json
# Create your tests here.


class Test(TestCase):

    def test_Price_and_quantity(self):
        prod=product.objects.create(Product_Name="samsung",Product_Type="wire",
        Product_Price=1000.000,Product_Quantity=3)
        self.assertTrue(prod.TestPrice())
    
    def test_Product_type(self):
        product_type=product.objects.create(Product_Name="samsung",Product_Type="wireless",
        Product_Price=1000.000,Product_Quantity=3)
        if product_type.Product_Type == "wire":
         self.assertTrue(product_type.TestProductType())
        elif product_type.Product_Type == "wireless":
         self.assertTrue(product_type.TestProductType())

    def test_not_same_filename_and_filetype(self):
        file_validation=upload_files.objects.create(File_Name="EssayAboutMyCountry",File_Type=".doc")
        self.assertTrue(file_validation.Test_name_type())
    
    def test_not_same_productname_and_productype(self):
        name_validation=product.objects.create(Product_Name="AppleAirpod",Product_Type="wireless",
        Product_Price=300,Product_Quantity=3)
        self.assertTrue(name_validation.TestProductNameAndType())
    
    def test_description_grt_ten(self):
        desc=product.objects.create(Product_Name="A60",Product_Type="wireless",
        Product_Price=300,
        Product_Description="This is A60 new wireless air phone device with varities of scolor available"
        ,Product_Quantity=3)
        self.assertTrue(desc.TestProductDescription())



