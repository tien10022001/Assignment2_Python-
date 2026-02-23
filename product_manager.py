#Danh sách sản phẩm 
products = []
#Thêm sản phẩm 
# Ham nay dung de them 1 dict san pham vao list
def add_product(product):
    products.append(product)
#Hiển thị sản phẩm
def show_products():
    return products
#Tìm kiếm sản phẩm 
def find_product(product_id): # Tra ve dict san pham neu tim thay, hoac None neu khong thay
    for p in products:
        if p["id"] == product_id:
            return p
    return None
# xóa sản phẩm theo mã
def delete_product(product_id):
    for p in products:
        if p["id"] == product_id:
            products.remove(p)
            return True 
    return False