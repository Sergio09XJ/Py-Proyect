import requests 

def get_products():
    r = requests.get(" https://api.escuelajs.co/api/v1/products")
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    products = r.json() 
    for product in products: 
        print(product["price"])