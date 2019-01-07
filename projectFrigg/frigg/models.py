from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    pass_key = models.CharField(max_length=100)
    date_added = models.DateField
    date_ended = models.DateField
    status = models.CharField(max_length=100)
    email = models.EmailField
    login = models.CharField(max_length=20)

class Client(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    company = models.CharField(max_length=100, null=True)
    phone_number = models.IntegerField(null=True)
    rfc = models.CharField(max_length=100, null=True)
    address_line1 = models.CharField(max_length=100, null=True)
    address_line2 = models.CharField(max_length=100, null=True)
    address_line_n = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=100, null=True)

class Design(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

class PrinterType(models.Model):
    name = models.CharField(max_length=100)
    cost_factor_time = models.CharField(max_length=100)
    cost_factor_material = models.CharField(max_length=100)
    material_options = models.CharField(max_length=100)

class Quote(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.PROTECT, null=True)
    company = models.CharField(max_length=100, null=True)
    type_of_print = models.CharField(max_length=20, null=True)
    #def if_stock_what_design(self):
    printer = models.ForeignKey(PrinterType, null=True, on_delete=models.PROTECT)
    material = models.CharField(max_length=100, null=True)
    time = models.IntegerField(null=True)
    amount_of_material = models.IntegerField(null=True)
    referral_person = models.CharField(max_length=100, null=True)
    date_time_code = models.DateField(null=True)
    user_id = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    cost = models.IntegerField(null=True)
    model_path = models.CharField(max_length=300, null=True)
    model_orientation_path = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=100, null=True)

class Instructions(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    date_time_code = models.DateTimeField
    ip_address = models.IPAddressField

class Job(models.Model):
    quote_id = models.ForeignKey(Quote, on_delete=models.PROTECT)
    date_time_code = models.DateTimeField
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)

class Flag(models.Model):
    flag_type = models.CharField(max_length=100)
    user_from = models.ForeignKey(User, default='', related_name='user_from', on_delete=models.PROTECT)
    user_to = models.ForeignKey(User, default='', related_name='user_to', on_delete=models.PROTECT)
    status = models.CharField(max_length=100)
    date_time_code = models.DateTimeField