from django.db import models
from django.contrib.auth.models import User
# Create your models here.
category_choices=(
    ("food","food"),
    ("bill","bill"),
    ("fuel","fuel")
)

payment_choices=(
    ("UPI","UPI"),
    ("card","card")

)

class ExpenseModel(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=8,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=100,choices=category_choices,default="food")
    payment=models.CharField(max_length=100,choices=payment_choices,default="UPI")

    def __str__(self):
        return f"{self.title}-{self.amount}"
