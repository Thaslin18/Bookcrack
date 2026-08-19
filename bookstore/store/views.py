from django.shortcuts import render
from django.shortcuts import render, redirect

# Catalog of books with prices
BOOKS_DATA = {
    'Harry Potter and the sorcerer\'s stone': {'price': 499, 'image': 'store/images/book 2 harry.jpg'},
    'Percy Jackson and the olympians': {'price': 499, 'image': 'store/images/book 3 adv.jpg'},
    'Pride and prejudice': {'price': 480, 'image': 'store/images/book 4 love.jpg'},
    'Shatter me': {'price': 380, 'image': 'store/images/book 5 rom thrill.jpg'},
    'The Ledger of Life': {'price': 480, 'image': 'store/images/ad0.jpg'},
    'Adventure': {'price': 300, 'image': 'store/images/ad1.jpg'},
    'The Maya Rivers Adventure': {'price': 400, 'image': 'store/images/ad2.jpg'},
    'The DreamKeeper Saga': {'price': 350, 'image': 'store/images/addd1.jpg'},
    'The Door In Green': {'price': 450, 'image': 'store/images/ad4.jpg'},
    'The Girl Who Borrowed Dreams': {'price': 400, 'image': 'store/images/ad5.jpg'},
    'The Lucky One': {'price': 600, 'image': 'store/images/ad6.jpg'},
    'The Messenger': {'price': 550, 'image': 'store/images/ad7.jpg'},
    'Defenders Of Myth': {'price': 650, 'image': 'store/images/ad8.jpg'},
    'The Return Of The Knights': {'price': 450, 'image': 'store/images/ad9.jpg'},
    'The Treasure that behind in us': {'price': 400, 'image': 'store/images/adv10.jpg'},
    'A Tale From Mithia': {'price': 450, 'image': 'store/images/adv11.jpg'},
    'The Red Pyramid': {'price': 650, 'image': 'store/images/adv12.jpg'},
    'The Lost Princess': {'price': 450, 'image': 'store/images/adv13.jpg'},
    'Dungeon Adventures': {'price': 600, 'image': 'store/images/adv14.jpg'},
    'Escape To A World Of Magic': {'price': 750, 'image': 'store/images/adv15.jpg'},
    'Dragens Storm': {'price': 590, 'image': 'store/images/adv16.jpg'},
    'Healer Land': {'price': 450, 'image': 'store/images/adv17.jpg'},
    'The Giver Lois Lowry': {'price': 480, 'image': 'store/images/e1.jpg'},
    'Power Of Your Subconscious Mind': {'price': 300, 'image': 'store/images/e2.jpg'},
    'The Science Of Rapid Skill Acquisition': {'price': 400, 'image': 'store/images/e3.jpg'},
    'Critical Thinking': {'price': 350, 'image': 'store/images/e4.jpg'},
    'Memory': {'price': 450, 'image': 'store/images/e5.jpg'},
    'Critical Thinking:The skill you need': {'price': 400, 'image': 'store/images/e6.jpg'},
    'Powerful Mindset Shifts': {'price': 600, 'image': 'store/images/e7.jpg'},
    'Thinking in Algorithms': {'price': 550, 'image': 'store/images/e8.jpg'},
    'Visual Intelligence': {'price': 650, 'image': 'store/images/e9.jpg'},
    'How To Analyze People': {'price': 450, 'image': 'store/images/e10.jpg'},
    'The Power Of Positive Thinking': {'price': 400, 'image': 'store/images/e11.jpg'},
    'The Art Of Self-Learning': {'price': 450, 'image': 'store/images/e12.jpg'},
    'Ahead Of The Curve': {'price': 650, 'image': 'store/images/e13.jpg'},
    'Getting To Yes': {'price': 450, 'image': 'store/images/e14.jpg'},
    'The Origin Of Wealth': {'price': 600, 'image': 'store/images/e15.jpg'},
    'Neurology And Religion': {'price': 750, 'image': 'store/images/e16.jpg'},
    'I, Human': {'price': 590, 'image': 'store/images/e17.jpg'},
    'Lead With AI, Stay Human': {'price': 450, 'image': 'store/images/e18.jpg'},
    "The Book That Wouldn't Burn": {'price': 480, 'image': 'store/images/f1.jpg'},
    'The Boundary': {'price': 300, 'image': 'store/images/f2.jpg'},
    'The Infinite Librarian': {'price': 400, 'image': 'store/images/f3.jpg'},
    'Where The Ivy Sleeps': {'price': 350, 'image': 'store/images/f4.jpg'},
    'Dream Dwellers': {'price': 450, 'image': 'store/images/f5.jpg'},
    'The Town That Keeps You': {'price': 400, 'image': 'store/images/f6.jpg'},
    'Mystery of The Midnight Sky': {'price': 600, 'image': 'store/images/f7.jpg'},
    'This Was Never An Accident': {'price': 550, 'image': 'store/images/f8.jpg'},
    'A Timeless Flower': {'price': 650, 'image': 'store/images/f9.jpg'},
    'Fractures Fairytale': {'price': 450, 'image': 'store/images/f10.jpg'},
    'Anything For Her': {'price': 400, 'image': 'store/images/f11.jpg'},
    'The Mystical Realms': {'price': 450, 'image': 'store/images/f12.jpg'},
    'Echoes Of Eternity': {'price': 650, 'image': 'store/images/f13.jpg'},
    'Mystic Whispers': {'price': 450, 'image': 'store/images/f14.jpg'},
    'The Wall Breakers': {'price': 600, 'image': 'store/images/f15.jpg'},
    'The Night Realm': {'price': 750, 'image': 'store/images/f16.jpg'},
    'The Eternal Night': {'price': 590, 'image': 'store/images/f17.jpg'},
    'The Silver Crow': {'price': 450, 'image': 'store/images/f18.jpg'},
    'Henry And Mudge': {'price': 480, 'image': 'store/images/kk1.jpg'},
    'Starry Journey': {'price': 300, 'image': 'store/images/k2.jpg'},
    'The whispering Latern': {'price': 400, 'image': 'store/images/k3.jpg'},
    'Mercy Watson To The Rescue': {'price': 350, 'image': 'store/images/kkk1.jpg'},
    'Milo And the Magic Mistake': {'price': 450, 'image': 'store/images/k5.jpg'},
    'The Moral Lessons In Cindrellas Stories': {'price': 400, 'image': 'store/images/k6.jpg'},
    'The Dino Detectives': {'price': 600, 'image': 'store/images/k7.jpg'},
    'Luna And The Talking Stars': {'price': 550, 'image': 'store/images/k8.jpg'},
    'The Lion And The Mouse': {'price': 650, 'image': 'store/images/k9.jpg'},
    'Beauty And The Beast': {'price': 450, 'image': 'store/images/k10.jpg'},
    'Rapunzel': {'price': 400, 'image': 'store/images/k11.jpg'},
    'Hansel And Gretel': {'price': 450, 'image': 'store/images/k12.jpg'},
    'Fiabe': {'price': 650, 'image': 'store/images/k13.jpg'},
    'Bella And The Big Feelings': {'price': 450, 'image': 'store/images/k14.jpg'},
    'The Kind Elephant': {'price': 600, 'image': 'store/images/k15.jpg'},
    'Forest Friends At First Site': {'price': 750, 'image': 'store/images/k16.jpg'},
    'The Forest Quest': {'price': 590, 'image': 'store/images/k17.jpg'},
    'Emara And The Kind Jungle': {'price': 450, 'image': 'store/images/k18.jpg'},
    'The First Traverse': {'price': 300, 'image': 'store/images/s2.jpg'},
    'The Archieve Between Stars': {'price': 400, 'image': 'store/images/s3.jpg'},
    'Nexux': {'price': 350, 'image': 'store/images/s4.jpg'},
    'The Final Frontier': {'price': 450, 'image': 'store/images/s5.jpg'},
    'Blue Sky graveyard': {'price': 400, 'image': 'store/images/s6.jpg'},
    'The Dead Lanes Are Close': {'price': 600, 'image': 'store/images/s7.jpg'},
    'Afterfall': {'price': 550, 'image': 'store/images/s8.jpg'},
    'The World In 2027': {'price': 650, 'image': 'store/images/s9.jpg'},
    'The Dogon Code': {'price': 450, 'image': 'store/images/s10.jpg'},
    'Who Ruled The Universe?': {'price': 400, 'image': 'store/images/s12.jpg'},
    'The Nile Beneath Carolina': {'price': 450, 'image': 'store/images/s13.jpg'},
    'Nirvana': {'price': 650, 'image': 'store/images/s14.jpg'},
    'The North Star': {'price': 450, 'image': 'store/images/s15.jpg'},
    'Beauty Blood And The Stars': {'price': 600, 'image': 'store/images/s16.jpg'},
    'The Awakening': {'price': 750, 'image': 'store/images/s17.jpg'},
    'Blood of Hercules': {'price': 590, 'image': 'store/images/s18.jpg'},
    'The Cursed': {'price': 450, 'image': 'store/images/s19.jpg'},
}

def add_to_cart(request, book_title):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    cart = request.session['cart']
    
    if book_title in cart:
        cart[book_title]['quantity'] += 1
    else:
        if book_title in BOOKS_DATA:
            cart[book_title] = {
                'price': BOOKS_DATA[book_title]['price'],
                'quantity': 1,
                'image': BOOKS_DATA[book_title]['image']
            }
            
    request.session.modified = True
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    context = {'cart': cart, 'total': total}
    return render(request, 'store/cart.html', context)

def remove_from_cart(request, book_title):
    cart = request.session.get('cart', {})
    if book_title in cart:
        del cart[book_title]
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
    return render(request, 'store/products.html')
def scidetails(request):
    return render(request, 'store/scidetails.html')
def signup(request):
    return render(request, 'store/signup.html')
from django.shortcuts import render, redirect
from .forms import AddressForm

from django.shortcuts import render, redirect
from .forms import AddressForm

def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to home or another page after successful save
            return redirect('home') 
    else:
        form = AddressForm()
    
    return render(request, 'store/add_address.html', {'form': form})