
# Ваше решение, ниже - мое описание


@classmethod
def buy(cls, user, item_id):
    product_qs = Product.objects.filter(item_id=item_id)
    if product_qs.exists():
        product = product_qs[0]
    if product.available:
    # списание средств со счета пользователя
        user.withdraw(product.price)
        # информация о купленном товаре
        send_email_to_user_of_buy_product(user)
        product.available = False
        product.buyer = user
        product.save()
        return True
    else:
        return False

# 1 - if product.available -  условие ссылается на переменую которая в случае отсуствия продукта, выдаст ошибку


