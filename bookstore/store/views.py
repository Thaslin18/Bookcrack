from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import AddressForm

def add_to_cart(request, book_id):
    # Retrieve the book from the database using its ID
    book = get_object_or_404(Book, id=book_id)
    
    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    cart = request.session['cart']
    book_id_str = str(book_id) # Session keys are stored as strings
    
    if book_id_str in cart:
        cart[book_id_str]['quantity'] += 1
    else:
        cart[book_id_str] = {
            'title': book.title,
            'price': float(book.price),
            'quantity': 1,
            'image': book.image.url if book.image else ''
        }
            
    request.session.modified = True
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    context = {'cart': cart, 'total': total}
    return render(request, 'store/cart.html', context)

def remove_from_cart(request, book_id):
    cart = request.session.get('cart', {})
    book_id_str = str(book_id)
    if book_id_str in cart:
        del cart[book_id_str]
        request.session.modified = True
    return redirect('cart')

def home(request):
    return render(request, 'store/index.html')

def about(request):
    return render(request, 'store/about.html')

def advdetails(request):
    return render(request, 'store/advdetails.html')

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')

def checkoutadv1(request):
    return render(request, 'store/checkoutadv1.html')

def checkoutadv2(request):
    return render(request, 'store/checkoutadv2.html')

def checkoutk1(request):
    return render(request, 'store/checkoutk1.html')

def checkoutk2(request):
    return render(request, 'store/checkoutk2.html')

def edudetails(request):
    return render(request, 'store/edudetails.html')

def fandetails(request):
    return render(request, 'store/fandetails.html')

def interest(request):
    return render(request, 'store/interest.html')

def kiddetails(request):
    return render(request, 'store/kiddetails.html')

def login(request):
    return render(request, 'store/login.html')

def products(request):
    # Fetch all books from the database to display them dynamically on your products page
    books = Book.objects.all()
    return render(request, 'store/products.html', {'books': books})

def scidetails(request):
    return render(request, 'store/scidetails.html')

def signup(request):
    return render(request, 'store/signup.html')

def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = AddressForm()
    
    return render(request, 'store/add_address.html', {'form': form})