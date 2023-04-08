from pytest_voluptuous import S
from schema.schema import *
import allure


@allure.story('Reqres.in tests')
@allure.feature('User')
@allure.title("User create")
def test_create_user(reqres):
    created_user = reqres.post("api/users", {"name": "Nikita", "job": "Quality Assurance"})
    assert S(create_user) == created_user.json()
    assert created_user.status_code == 201
    assert created_user.json()["name"] == "Nikita"
    assert created_user.json()["job"] == "Quality Assurance"
    assert created_user.json()["createdAt"] is not None
    assert created_user.json()["id"] is not None


@allure.story('Reqres.in tests')
@allure.feature('User')
@allure.title("User update")
def test_update_user(reqres):
    updated_user = reqres.put("api/users/2", {"name": "Nikita Fedotov", "job": "Quality Control"})
    assert updated_user.status_code == 200
    assert updated_user.json()["name"] == "Nikita Fedotov"
    assert updated_user.json()["job"] == "Quality Control"
    assert updated_user.json()["updatedAt"] is not None
    assert S(update_user) == updated_user.json()


@allure.story('Reqres.in tests')
@allure.feature('User')
@allure.title("User register successful")
def test_register_successful(reqres):
    user_register = reqres.post("api/register", {"email": "eve.holt@reqres.in", "password": "cityslicka"})
    assert user_register.status_code == 200
    assert S(register_user) == user_register.json()
    assert user_register.json()['id']
    assert user_register.json()["token"] == "QpwL5tke4Pnpja7X4"


@allure.story('Reqres.in tests')
@allure.feature('User')
@allure.title("User register unsuccessful")
def test_register_unsuccessful(reqres):
    user_register = reqres.post("api/register", {"email": "wrong@mail.ru"})
    assert user_register.status_code == 400
    assert S(unregister_user) == user_register.json()
    assert user_register.json()['error'] == 'Missing password'


@allure.story('Reqres.in tests')
@allure.feature('User')
@allure.title("User delete")
def test_delete_user(reqres):
    delete_user = reqres.delete("api/users/2")
    assert delete_user.status_code == 204


@allure.story('Reqres.in tests')
@allure.feature('User')
@allure.title("User not found")
def test_user_not_found(reqres):
    user_not_found = reqres.get("api/users/23")
    assert user_not_found.status_code == 404
