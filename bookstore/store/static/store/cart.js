document.addEventListener('DOMContentLoaded', () => {
    // 1. HANDLE ADD TO CART CLICK & REDIRECTION
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    
    addToCartButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault(); // Stop instant jump to allow saving data

            const card = e.target.closest('.card');
            if (!card) return;

            const title = card.getAttribute('data-title');
            const price = parseFloat(card.getAttribute('data-price'));
            const targetUrl = e.target.getAttribute('href');

            if (!title || isNaN(price)) return;

            let cart = JSON.parse(localStorage.getItem('bookcrack_cart')) || [];
            
            let existingItem = cart.find(item => item.title === title);
            if (existingItem) {
                existingItem.quantity += 1;
            } else {
                cart.push({ title, price, quantity: 1 });
            }

            // Save data to localStorage
            localStorage.setItem('bookcrack_cart', JSON.stringify(cart));

            // Short delay to ensure local storage updates, then navigate to cart
            setTimeout(() => {
                window.location.href = targetUrl;
            }, 100);
        });
    });

    // 2. RENDER CART ITEMS AUTOMATICALLY ON CART PAGE
    const cartContainer = document.getElementById('cart-items-container');
    if (cartContainer) {
        renderCart();
    }
});

function renderCart() {
    let cart = JSON.parse(localStorage.getItem('bookcrack_cart')) || [];
    const cartContainer = document.getElementById('cart-items-container');
    const cartTotalElem = document.getElementById('cart-total');
    const shopNowContainer = document.getElementById('shop-now-container');
    
    cartContainer.innerHTML = '';

    if (cart.length === 0) {
        cartContainer.innerHTML = '<p>Your cart is empty.</p>';
        if (cartTotalElem) cartTotalElem.innerText = '0';
        if (shopNowContainer) shopNowContainer.style.display = 'none';
        return;
    }

    if (shopNowContainer) shopNowContainer.style.display = 'inline-block';
    let total = 0;

    cart.forEach((item, index) => {
        let itemTotal = item.price * item.quantity;
        total += itemTotal;

        const itemDiv = document.createElement('div');
        itemDiv.className = 'book-card';
        itemDiv.style.marginBottom = '15px';
        itemDiv.style.padding = '15px';
        itemDiv.style.border = '1px solid #ddd';
        itemDiv.style.background = '#fff';
        itemDiv.innerHTML = `
            <h2 class="book-title" style="font-size: 18px;">${item.title}</h2>
            <p class="book-price">Price: ₹${item.price} × ${item.quantity} = <strong>₹${itemTotal}</strong></p>
            <button class="buy-now-btn" style="background-color: #dc3545; color: white; padding: 5px 10px; border: none; border-radius: 4px; cursor: pointer;" onclick="removeItem(${index})">Remove</button>
        `;
        cartContainer.appendChild(itemDiv);
    });

    if (cartTotalElem) cartTotalElem.innerText = total;
}

// 3. REMOVE ITEM LOGIC
window.removeItem = function(index) {
    let cart = JSON.parse(localStorage.getItem('bookcrack_cart')) || [];
    cart.splice(index, 1);
    localStorage.setItem('bookcrack_cart', JSON.stringify(cart));
    renderCart();
}