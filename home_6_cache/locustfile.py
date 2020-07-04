from locust import HttpUser, task, between
import faker

fake = faker.Faker()

class CommonUser(HttpUser):

    @task(1)
    def get_product_id(self):
        payload={"name" : fake.word(),"price" : 13.6}
        self.client.post('/otusapp/products', json=payload)

    @task(10)
    def search(self):
        response = self.client.get('/otusapp/products')
        json_var = response.json()
        for product in json_var:
            print(product)
            self.client.get('/otusapp/products/find?name='+str(product['name']) +'&version='+str(product['version']))

    wait_time = between(2, 5)