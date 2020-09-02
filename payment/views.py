from django.shortcuts import render,redirect,reverse
import stripe
# Create your views here.
def home(request):
  return render(request,'index.html')

def charge(request):
  print(request.POST)
  stripe.api_key = "#secret key is here"
  stripe.Customer.create(
    name=request.POST.get('name'),
    email=request.POST.get('email'),
    description="My First Test Customer (created for API docs)",
  )
  amount=int(request.POST.get('amount'))*100
  stripe.Charge.create(
  amount=amount,
  currency="usd",
  source="tok_visa",
  description="My First Test Charge (created for API docs)",
  )
  amount_in_D=amount//100
  return redirect(reverse('sucess',args=[amount_in_D]))

def success(request,args):
  context={
    'amount':args
  }
  return render(request,'payment-success.html',context)