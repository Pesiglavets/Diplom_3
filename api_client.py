import requests
from faker import Faker

fake = Faker()

BASE_URL = "https://stellarburgers.education-services.ru/api"


class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL
    
    def generate_user_data(self):
        email = fake.email()
        password = fake.password(length=8)
        name = fake.first_name()
        return email, password, name
    
    def register_new_user(self):
        email, password, name = self.generate_user_data()
        payload = {"email": email, "password": password, "name": name}
        response = requests.post(f'{self.base_url}/auth/register', data=payload)
        
        if response.status_code == 200:
            return email, password, name
        elif response.status_code == 403:
            email, password, name = self.generate_user_data()
            payload = {"email": email, "password": password, "name": name}
            response = requests.post(f'{self.base_url}/auth/register', data=payload)
            
            if response.status_code == 200:
                return email, password, name
        return None, None, None
    
    def login_user(self, email, password):
        payload = {"email": email, "password": password}
        response = requests.post(f'{self.base_url}/auth/login', data=payload)
        return response
    
    def delete_user(self, auth_token):
        if auth_token:
            headers = {'Authorization': auth_token}
            response = requests.delete(f'{self.base_url}/auth/user', headers=headers)
            return response
        return None
    
    def get_ingredients(self):
        response = requests.get(f'{self.base_url}/ingredients')
        if response.status_code == 200:
            return response.json()["data"]
        return None

    def create_order(self, ingredients, auth_token=None):
        payload = {"ingredients": ingredients}
        headers = {}
        if auth_token:
            headers['Authorization'] = auth_token
        response = requests.post(f'{self.base_url}/orders', data=payload, headers=headers)
        return response
    
    def create_order_and_get_number(self, ingredients, auth_token=None):
        response = self.create_order(ingredients, auth_token)
        if response.status_code == 200:
            return response.json()["order"]["number"]
        return None

    def get_first_ingredient_id(self):
        ingredients = self.get_ingredients()
        if ingredients and len(ingredients) > 0:
            return ingredients[0]["_id"]
        return None