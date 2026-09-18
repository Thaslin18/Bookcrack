from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from .models import Book
from .forms import AddressForm

def add_to_cart(request, book_title):
    # Fallback to user_id = 1 if the user isn't logged in
    user_id = request.user.id if request.user.is_authenticated else 1  

    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO cart_items (user_id, book_title, quantity)
            VALUES (%s, TRIM(%s), 1)
            ON CONFLICT (user_id, book_title)
            DO UPDATE SET quantity = cart_items.quantity + 1;
        """, [user_id, book_title])
        
    return redirect('cart')

def cart(request):
    user_id = request.user.id if request.user.is_authenticated else 1
    
    cart_dict = {}
    with connection.cursor() as cursor:
        # Fetch just the items from your manually created cart table
        cursor.execute("""
            SELECT book_title, quantity 
            FROM cart_items 
            WHERE user_id = %s;
        """, [user_id])
        rows = cursor.fetchall()
        
    for row in rows:
        title, quantity = row
        # Use Django ORM to find the book safely, ignoring case/spacing issues
        book = Book.objects.filter(title__iexact=title.strip()).first()
        price = float(book.price) if (book and book.price) else 0.0
        
        cart_dict[title] = {
            'price': price,
            'quantity': quantity
        }
        
    total = sum(item['price'] * item['quantity'] for item in cart_dict.values())
    context = {'cart': cart_dict, 'total': total}
    return render(request, 'store/cart.html', context)

def remove_from_cart(request, book_title):
    user_id = request.user.id if request.user.is_authenticated else 1
    
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM cart_items 
            WHERE user_id = %s AND LOWER(TRIM(book_title)) = LOWER(TRIM(%s));
        """, [user_id, book_title])
        
    return redirect('cart')

def home(request):
    return render(request, 'store/index.html')

def about(request):
    return render(request, 'store/about.html')

def advdetails(request):
    return render(request, 'store/advdetails.html')

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
