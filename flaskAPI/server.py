from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from flask import Flask, request, jsonify
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import linked_list
from random import randrange
from faker import Faker
from hash_table import HashTable
from binary_search_tree import BinarySearchTree
import random



now = datetime.now()

# Configure sqlite3 to enforece foreign key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 0
# initialize the app with the extension
db.init_app(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost", cascade="all, delete")


class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


# Routes

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(
        name = data["name"],
        email = data["email"],
        address = data["address"],
        phone= data["phone"]
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created!"}), 200
    

@app.route("/user/descending_id", methods=["GET"])
def get_all_users_descending():
    users = User.query.all()
    all_users_ll = linked_list.LinkedList()

    for user in users:
        all_users_ll.insert_beginning(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone
            }
        )


    return jsonify({"data": all_users_ll.to_list()}), 200


@app.route("/user/ascending_id", methods=["GET"])
def get_all_users_ascending():
    users = User.query.all()
    all_user_ll = linked_list.LinkedList()
    for user in users:
        all_user_ll.insert_end(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone
            }
        )
    return jsonify(all_user_ll.to_list()), 200
    

@app.route("/user/<user_id>", methods=["GET"])
def get_one_user(user_id):
    users = User.query.all()
    all_users_ll = linked_list.LinkedList()
    
    for user in users:
        all_users_ll.insert_beginning(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone
            }
        )
    user = all_users_ll.get_user_by_id(user_id)
    return jsonify(user), 200


@app.route("/user/delete/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    # get user to be deleted
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"user with id {user_id} deleted successfuly"}), 200


@app.route("/blog_post/<user_id>", methods=["POST"])
def create_blog_post(user_id):
    data = request.get_json()

    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"message": "User with id, does not exists1"})
    ht = HashTable(10)
    
    ht.add_key_value("title", data["title"])
    ht.add_key_value("body", data["body"])
    ht.add_key_value("date", now)
    ht.add_key_value("user_id", user_id)

    new_blog_post = BlogPost(
        title=ht.get_value("title"),
        body=ht.get_value("body"),
        date=ht.get_value("date"),
        user_id=ht.get_value("user_id")
    )
    db.session.add(new_blog_post)
    db.session.commit()

    return jsonify({"message": f"Blog Post created successfuly by user with id {user_id}"})

@app.route("/blog_post", methods=["POST"])
def get_all_blog_posts():
    pass

@app.route("/blog_posts/<blog_post_id>", methods=["GET"])
def get_one_blog_post(blog_post_id):
    blog_posts = BlogPost.query.all()
    random.shuffle(blog_posts)
    bst = BinarySearchTree()
    for post in blog_posts:
        bst.insert({
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "user_id": post.user_id
        })
        
    post = bst.search(blog_post_id)
    if not post:
        return jsonify({"message": "Post not found"})
    return jsonify(post)
    

@app.route("/blog_post/<blog_post_id>", methods=["DELETE"])
def delete_blog_post():
    pass

def create_dumy_data():
    # create dummy users
    faker = Faker()
    with app.app_context():
        for i in range(200):
            name = faker.name()
            address = faker.address()
            phone = faker.msisdn()
            email = f'{name.replace(" ", "_")}@email.com'
            new_user = User(name=name, address=address, phone=phone, email=email)
            db.session.add(new_user)
            db.session.commit()
        
        # create dummy blog posts
        for i in range(200):
            title = faker.sentence(5)
            body = faker.paragraph(190)
            date = faker.date_time()
            user_id = randrange(1, 200)
        
            new_blog_post = BlogPost(
                title=title, body=body, date=date, user_id=user_id
            )
            db.session.add(new_blog_post)
            db.session.commit()


if __name__ == "__main__": 
    app.run(debug=True)