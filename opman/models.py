from django.contrib.auth.models import User
from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=10)                                  # Order Id
    seq_num = models.SmallIntegerField(default=1)                               # Sequence Number
    customer_po = models.CharField(max_length=100, null=True, blank=True)       # PO Number
    customer = models.CharField(max_length=30)                                  # Customer
    order_type = models.CharField(max_length=2)                                 # Order Type
    order_date = models.DateField()                                             # Order Date
    rtd = models.DateField(null=True, blank=True)                               # RTD
    etd = models.DateField(null=True, blank=True)                               # ETD
    brand = models.CharField(max_length=30)                                     # Brand
    item = models.CharField(max_length=50)                                      # Item
    color_code = models.CharField(max_length=30)                                # Color Code
    pattern = models.CharField(max_length=30)                                   # Pattern
    spec = models.CharField(max_length=30)                                      # Specification
    order_qty = models.SmallIntegerField(default=0)                             # Ordery Q'ty
    unit = models.CharField(max_length=10)                                      # Unit
    price = models.DecimalField(max_digits=5, decimal_places=2)                 # Price($)
    model_name = models.CharField(max_length=100, null=True, blank=True)        # Model Name
    sample_step = models.CharField(max_length=100, null=True, blank=True)       # Sample Step
    material_type = models.CharField(max_length=10, null=True, blank=True)                             # Material Type
    remark = models.CharField(max_length=100, null=True, blank=True)            # Remark
    modify_date = models.DateTimeField(null=True, blank=True)                   # Modified Date
    modify_log = models.TextField(null=True, blank=True)                        # Modified Log
    state = models.NullBooleanField()                                           # Order State
    watch_users = models.ManyToManyField(User,
                                         through='WatchlistInfo',
                                         related_name="watchlist")

class WatchlistInfo(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    deadline = models.DateField(null=True, blank=True)
    memo = models.TextField(null=True, blank=True)


class Process(models.Model):

    # Order 속성
    id = models.CharField(max_length=20, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    process_qty = models.IntegerField(default=0)
    procedure = models.CharField(max_length=10, null=True, blank=True)      # Production Procedure
    first_update = models.DateField(null=True, blank=True)                   # Update Date
    last_state = models.CharField(max_length=30, null=True, blank=True)         # Status
    last_update = models.DateField(null=True, blank=True)                   # Update Date
    plan_state = models.CharField(max_length=30,null=True, blank=True)
    plan_date = models.DateField(null=True, blank=True)                     # Plan Date
    state_last = models.CharField(max_length=30,null=True, blank=True)
    date_last = models.DateField(null=True, blank=True)
    plan_qty = models.SmallIntegerField(null=True, blank=True)              # Plan Q'ty
    pd_state = models.CharField(max_length=30,null=True, blank=True)
    pd_date = models.DateField(null=True, blank=True)                       # Production Date
    pd_qty = models.SmallIntegerField(null=True, blank=True)                # Production Q'ty
    bf_state = models.CharField(max_length=30,null=True, blank=True)
    bf_date = models.DateField(null=True, blank=True)                       # Buffing Date
    bf_qty = models.SmallIntegerField(null=True, blank=True)                # Buffing Q'ty
    eb_state = models.CharField(max_length=30,null=True, blank=True)
    eb_date = models.DateField(null=True, blank=True)                       # Embo Date
    eb_qty = models.SmallIntegerField(null=True, blank=True)                # Embo Q'ty
    pt_state = models.CharField(max_length=30,null=True, blank=True)
    pt_date = models.DateField(null=True, blank=True)                       # Color Print Date
    pt_qty = models.SmallIntegerField(null=True, blank=True)                # Color Print Q'ty
    ins_state = models.CharField(max_length=30,null=True, blank=True)
    ins_date = models.DateField(null=True, blank=True)                      # Inspection Date
    ins_qty = models.SmallIntegerField(null=True, blank=True)               # Inspection Q'ty
    shp_date = models.DateField(null=True, blank=True)                      # Shipment Date
    shp_qty = models.SmallIntegerField(null=True, blank=True)               # Shipment Q'ty

class Mention(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

class Brand(models.Model):
    brand = models.CharField(max_length=30)
    brand_code = models.CharField(max_length=3)

class Customer(models.Model):
    customer = models.CharField(max_length=30)



# Create your models here.
