def main():
    pass
    # # Создание корзины покупок и добавление товаров
    # cart = ShoppingCart()
    # cart.add_item("Книга")
    # cart.add_item("Ноутбук")
    # cart.add_item("Телефон")
    #
    # # Заказ 1: Оплата кредитной картой
    # credit_card = CreditCardPayment("1234-5678-9012-3456", "Иван Иванов", "123", "12/25")
    # cart.set_payment_strategy(credit_card)
    # cart.checkout()
    # print()
    #
    # # Заказ 2: Оплата через PayPal
    # pay_pal = PayPalPayment("ivan@example.com", "securepassword")
    # cart.set_payment_strategy(pay_pal)
    # cart.checkout()
    # print()
    #
    # # Заказ 3: Оплата через Bitcoin
    # bitcoin = BitcoinPayment("1BoatSLRHtKNngkdXEeobR76b53LETtpyT")
    # cart.set_payment_strategy(bitcoin)
    # cart.checkout()
    # print()
    #
    # # Заказ 4: Оплата через Apple Pay
    # apple_pay = ApplePayPayment("D1234567890")
    # cart.set_payment_strategy(apple_pay)
    # cart.checkout()

if __name__ == "__main__":
    main()