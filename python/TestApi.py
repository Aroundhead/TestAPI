import requests

URL = 'http://localhost:3000/productos'

response = requests.get(URL)

if response.status_code == 200:
    print("Productos:")
    for producto in response.json():
        print(f"- {producto['nombre']} (${producto['precio']})")
else:
    print("Error:", response.status_code)
