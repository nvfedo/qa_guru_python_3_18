import allure
from selene import have


def test_auth(app):
    app.open("")
    with allure.step('Check successful auth'):
        app.element(".account").should(have.text("nvfedoqaguru3_16@mail.ru"))


def test_delete_product_from_wishlist(demowebshop, app):
    app.open("")
    with allure.step('Add product to wishlist'):
        demowebshop.add_product_to_wishlist()
    with allure.step('Check delete product from wishlist'):
        app.element('.ico-wishlist').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
        app.element('.wishlist-content').should(have.text('The wishlist is empty!'))


def test_add_product_to_cart(demowebshop, app):
    app.open("")
    with allure.step("Check successful add to cart"):
        demowebshop.add_product_to_cart()
        app.element(".ico-cart").click()
        app.element(".product-name").should(have.text("Laptop"))


def test_delete_product_from_cart(demowebshop, app):
    app.open("")
    with allure.step('Add product to cart'):
        demowebshop.add_product_to_cart()
    with allure.step('Delete product from cart'):
        app.element('.ico-cart').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
        app.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_logout(app):
    app.open("")
    with allure.step('Check successful logout'):
        app.element('.ico-logout').click()
        app.element('.ico-login').should(have.text('Log in'))
