from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///productos.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Product(db.Model):
       __tablename__ = "products"

       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String, nullable=False)
       price = db.Column(db.Float, nullable=False)
       stock = db.Column(db.Integer, default=0)        

def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock})>"



def init_db():
    with app.app_context():  
        db.drop_all()        
        db.create_all()   
        print("Base de datos creada satisfactoriamente")



def insert_products():
    with app.app_context():
        print("\n CREATE: Inserción de productos ")

        product1 = Product(name="Laptop", price=4500.50, stock=10)
        product2 = Product(name="Mouse", price=85.00, stock=50)
        product3 = Product(name="Teclado", price=150.75)   
        product4 = Product(name="Monitor", price=1200.00, stock=5)

        db.session.add(product1)
        db.session.add(product2)
        db.session.add(product3)
        db.session.add(product4)

        db.session.commit()
        print("Productos insertados")
def query_products():
    with app.app_context():
        print("\n=== READ: Listado de productos ===")
       
        products = Product.query.all()
        for item in products:
            print(item)

       
        print("\nListado de productos con precio mayor a 100")
        filtrados = Product.query.filter(Product.price > 100).all()
        for item in filtrados:
            print(item)

     
        print("\nObtener un solo registro")
        product = Product.query.filter_by(id=1).first()
        if product:
            print(product)
        else:
            print("Producto no encontrado")

def update_product():
    with app.app_context():
        print("\n UPDATE: Actualización de un registro ")

        product = Product.query.filter_by(id=2).first()
        if product:
            product.name = "Mouse Inalámbrico"
            product.price = 120.00
            product.stock = 30
            db.session.commit()
            print("Producto actualizado:", product)
        else:
            print("Producto no encontrado")

def delete_product():
    with app.app_context():
        print("\n DELETE: Eliminación de registros ")
        product = Product.query.filter_by(id=3).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            print("Producto eliminado satisfactoriamente:", product.name)
        else:
            print("Producto no encontrado")

def show_final():
    with app.app_context():
        print("\n Estado final de la tabla products ")
        for item in Product.query.all():
            print(item)

if __name__ == "__main__":
    #init_db()        
    #insert_products()   
    #query_products()    
    #update_product()    
   # delete_product()    
    show_final()        