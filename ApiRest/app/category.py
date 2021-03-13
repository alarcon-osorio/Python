from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/pythonapi?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

#Creacion de Tabla Categiry
class Category(db.Model):
    cat_id= db.Column(db.Integer, primary_key=True)
    cat_nom= db.Column(db.String(100))
    cat_desp= db.Column(db.String(100))

    def __init__(self, cat_nom, cat_desp):
        self.cat_nom = cat_nom
        self.cat_desp = cat_desp

db.create_all()

#Schema Category
class CategorySchema(ma.Schema):
    class Meta:
        fields = ('cat_id','cat_nom','cat_desp')

#Una respuesta
category_schema = CategorySchema()

#Muchas respuestas
categories_schema = CategorySchema(many=True)

#Mensaje de Bienvenida
@app.route('/', methods=['GET'])
def index():
    return jsonify({'Mensaje':'Bienvenido al tuto'})

#GET - ###############################
@app.route('/categoria', methods = ['GET'])
def get_category():
    all_categories = Category.query.all()
    result = categories_schema.dump(all_categories)
    return jsonify(result)

#GET_BY_ID - ##############################
@app.route('/categoria/<id>', methods = ['GET'])
def get_category_by_id(id):
    one_category = Category.query.get(id)
    return category_schema.jsonify(one_category)

#POST - ##################################
@app.route('/categoria', methods = ['POST'])
def insert_category():
    data = request.get_json(force=True)
    cat_nom = data['cat_nom']
    cat_desp = data['cat_desp']

    new_category = Category(cat_nom, cat_desp)
    
    db.session.add(new_category)
    db.session.commit()
    return category_schema.jsonify(new_category)

#PUT - ##################################
@app.route('/categoria/<id>', methods = ['PUT'])
def update_category(id):
    category_update = Category.query.get(id)

    data = request.get_json(force=True)
    cat_nom = data['cat_nom']
    cat_desp = data['cat_desp']

    category_update.cat_nom = cat_nom
    category_update.cat_desp = cat_desp

    db.session.commit()
    return category_schema.jsonify(category_update)

#DELETE - ############################
@app.route('/categoria/<id>', methods = ['DELETE'])
def delete_category(id):
    category_delete = Category.query.get(id)
    db.session.delete(category_delete)
    db.session.commit()
    return category_schema.jsonify(category_delete)

#Metodo main
if __name__ == '__main__':
    app.run(debug=True)