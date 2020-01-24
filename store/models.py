from django.db import models


class product(models.Model):
    Product_Name = models.CharField(max_length=120)
    Product_Type = models.CharField(max_length=120)
    Product_Price = models.DecimalField(max_digits=20000,decimal_places=3)
    Product_Description = models.TextField(blank=True)
    Product_Quantity = models.IntegerField()
    img = models.FileField(upload_to='photos/')

    
    def __str__(self):
        return self.Product_Name

    def TestPrice(self):
        return (self.Product_Price > 0.000)  and (self.Product_Quantity > 0)

    def TestProductType(self):
        return (self.Product_Type == "wire") or (self.Product_Type == "wireless")

    def TestProductNameAndType(self):
        return (self.Product_Name != self.Product_Type)
        
    def TestProductDescription(self):
        return (len(self.Product_Description) > 50)



class upload_files(models.Model):
    File_Name = models.CharField(max_length=140)
    File_Type = models.CharField(max_length=140,null=True)
    pdf = models.FileField(upload_to='files/',null=True)

    def __str__(self):
        return self.File_Name
    
    def Test_name_type(self):
        return (self.File_Name != self.File_Type)





