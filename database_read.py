# import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, MenuItem, Restaurant
# from square.client import Client

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#client = Client(
#    access_token=os.environ['SQUARE_ACCESS_TOKEN'],
#    environment='production')

#result = client.catalog.list_catalog()

#result_item = client.catalog.list_catalog(types = "ITEM")

#result_category = client.catalog.list_catalog(types = "CATEGORY")


#if result.is_success():
#  print(result.body)
#elif result.is_error():
#  print(result.errors)

# printing specific values from results


print("---Reading database---")

read_restaurants = session.query(Restaurant).all()
# read_items = session.query(MenuItems).all()

# read_restaurants = session.query(Restaurant).filter_by(id = restaurant_id).all()
# read_items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
#print(read_category)

for r in read_restaurants:
    # print(read_restaurants)
    # print(type(read_restaurants))
    print(r.name)
    # print(type(r.name))
    print(r.id)
    # print(type(r.id))
    read_items = session.query(MenuItem).filter_by(restaurant_id = r.id).all()
    # read_items = session.query(MenuItem).all()
    # print(read_items)
    # print(type(read_items))
    for i in read_items:
        print(i.name)
        # print(type(i.name))
        print(i.description)
        # print(type(i.description))
        print(i.id)
        # print(type(i.id))
        print(i.price)
        # print(type(i.price))
        print(i.course)
        # print(type(i.course))
    print("--------------------")



#if __name__ == '__main__':
#    app.secret_key = 'super_secret_key'
#    app.debug = True
#    app.run(host='0.0.0.0', port=5000)
