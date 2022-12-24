products = [
    {"p_name":"Apple Iphone 11","brand":"Apple","Category":"Mobile","price":98000},
    {"p_name":"Redmi Note 6","brand":"Xiaomi","Category":"Mobile","price":15000},
    {"p_name":"Sports Shoes","brand":"Puma","Category":"Shoes","price":3400},
    {"p_name":"JBL Headphones bluetooth","brand":"JBL","Category":"Headphones","price":1200},
    {"p_name":"Leather Jacket","brand":"Zara","Category":"Clothes","price":4500},
    {"p_name":"Puma Shoes","brand":"Puma","Category":"Shoes","price":2070},
    {"p_name":"Adidas Sports Shoes","brand":"Adidas","Category":"Shoes","price":1900},
    {"p_name":"Macbook Pro","brand":"Apple","Category":"Laptop","price":128000},
    {"p_name":"Lenovo thinkpad","brand":"Lenovo","Category":"Laptop","price":78000},
    {"p_name":"Asus Zenbook","brand":"Asus","Category":"Laptop","price":88000},
    ]
'''
    - user can enter product name, product brand or category
    - now store the data in a different list (searchResults = [])
    - ask user if he wants to sort data based on price
    - ask the order of sorting
'''
toSearch = input("Search Here : ")
toSearch = toSearch.lower()

searchResults = []

for i in range(len(products)):
    if products[i]["p_name"].lower() == toSearch:
        print("Name :",products[i]["p_name"])
        print("Category :",products[i]["Category"])
        print("Price :",products[i]["price"])
