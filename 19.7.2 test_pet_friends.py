from api import PetFfiends
from settings import valid_email, valid_password
import os


pf=PetFfiends()

def test_get_api_key_for_valid_user(email=valid_email,password=valid_password):
    status,result = pf.get_api_key(email,password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    _,auth_key=pf.get_api_key(valid_email,valid_password)
    status,result=pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets'])>0

def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()

def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name

    else:
        raise Exception("There is no my pets")


     #Задание 19.7.2 - - - - - - - - 10 тестов

     #Тест №1
from settings import invalid_email, invalid_password
def test_get_api_key_for_invalid_user(email=invalid_email,password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert "This user wasn't found in database" in result

     #Тест №2
from settings import invalid_email, invalid_password
def test_get_api_key_for_invalid_user_status_failed(email=invalid_email,password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert "This user wasn't found in database" in result

     #Тест №3

from settings import invalid_email, invalid_password
def test_get_api_key_for_invalid_user_result_failed(email=invalid_email,password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' in result

     #Тест №4
from settings import invalid_email, invalid_password
def test_get_all_pets_with_invalid_user_failed(filter=""):
    _,auth_key=pf.get_api_key(invalid_email,invalid_password)
    status,result=pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets'])>0

     #Тест №5
def test_get_all_pets_with_valid_key_amount_of_pets_failed(filter=''):
    _,auth_key=pf.get_api_key(valid_email,valid_password)
    status,result=pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) == 0


     #Тест №6

def test_add_new_pet_with_invalid_data(name='Sobaka', animal_type='Dog',
                                     age='4'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_with_invalid_data(auth_key, name, animal_type, age)

    assert status == 400
    assert "Bad Request" in result

     #Тест №7

def test_add_new_pet_with_invalid_data_failed(name='Sobaka', animal_type='Dog',
                                     age='4'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_with_invalid_data(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name

     #Тест №8

def test_get_list_of_my_pets_with_valid_key(filter='my_pets'):
    _,auth_key=pf.get_api_key(valid_email,valid_password)
    status,result=pf.get_list_of_my_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0
    print(result)

      #Тест №9

def test_get_list_of_my_pets_with_valid_key_failed(filter='my_pets'):
    _,auth_key=pf.get_api_key(valid_email,valid_password)
    status,result=pf.get_list_of_my_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) == 0

      #Тест №10

def test_update_my_pets_no_pets_exception(name='Kosha', animal_type='Koshka', age=5):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name

    else:
        raise Exception("There is no my pets")