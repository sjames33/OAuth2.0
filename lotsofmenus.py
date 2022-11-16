from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Restaurant, Base, MenuItem
 
engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



#Menu for UrbanBurger
restaurant1 = Restaurant(name = "Urban Burger")

session.add(restaurant1)
session.commit()


menuItem11 = MenuItem(name = "French Fries", description = "with garlic and parmesan", price = "$2.99", course = "Appetizer", restaurant = restaurant1)

session.add(menuItem11)
session.commit()

menuItem12 = MenuItem(name = "Chicken Burger", description = "Juicy grilled chicken patty with tomato mayo and lettuce", price = "$5.50", course = "Entree", restaurant = restaurant1)

session.add(menuItem12)
session.commit()

menuItem13 = MenuItem(name = "Chocolate Cake", description = "fresh baked and served with ice cream", price = "$3.99", course = "Dessert", restaurant = restaurant1)

session.add(menuItem13)
session.commit()

menuItem14 = MenuItem(name = "Sirloin Burger", description = "Made with grade A beef", price = "$7.99", course = "Entree", restaurant = restaurant1)

session.add(menuItem14)
session.commit()

menuItem15 = MenuItem(name = "Root Beer", description = "16oz of refreshing goodness", price = "$1.99", course = "Beverage", restaurant = restaurant1)

session.add(menuItem15)
session.commit()

menuItem16 = MenuItem(name = "Iced Tea", description = "with Lemon", price = "$.99", course = "Beverage", restaurant = restaurant1)

session.add(menuItem16)
session.commit()

menuItem17 = MenuItem(name = "Grilled Cheese Sandwich", description = "On texas toast with American Cheese", price = "$3.49", course = "Entree", restaurant = restaurant1)

session.add(menuItem17)
session.commit()

menuItem18 = MenuItem(name = "Veggie Burger", description = "Made with freshest of ingredients and home grown spices", price = "$5.99", course = "Entree", restaurant = restaurant1)

session.add(menuItem18)
session.commit()




#Menu for Super Stir Fry
restaurant2 = Restaurant(name = "Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem21 = MenuItem(name = "Chicken Stir Fry", description = "with your choice of noodles vegetables and sauces", price = "$7.99", course = "Entree", restaurant = restaurant2)

session.add(menuItem21)
session.commit()

menuItem22 = MenuItem(name = "Peking Duck", description = " a famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price = "$25", course = "Entree", restaurant = restaurant2)

session.add(menuItem22)
session.commit()

menuItem23 = MenuItem(name = "Spicy Tuna Roll", description = "", price = "", course = "Entree", restaurant = restaurant2)

session.add(menuItem23)
session.commit()

menuItem24 = MenuItem(name = "Nepali Momo ", description = "", price = "", course = "Entree", restaurant = restaurant2)

session.add(menuItem24)
session.commit()

menuItem25 = MenuItem(name = "Beef Noodle Soup", description = "", price = "Entree", course = "Entree", restaurant = restaurant2)

session.add(menuItem25)
session.commit()

menuItem26 = MenuItem(name = "Ramen", description = "", price = "", course = "Entree", restaurant = restaurant2)

session.add(menuItem26)
session.commit()




#Menu for Panda Garden
restaurant3 = Restaurant(name = "Panda Garden")

session.add(restaurant3)
session.commit()


menuItem31 = MenuItem(name = "Pho", description = "a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.", price = "", course = "Entree", restaurant = restaurant3)

session.add(menuItem31)
session.commit()

menuItem32 = MenuItem(name = "Chinese Dumplings", description = "a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.", price = "", course = "Entree", restaurant = restaurant3)

session.add(menuItem32)
session.commit()

menuItem33 = MenuItem(name = "Gyoza", description = "The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner", price = "", course = "Entree", restaurant = restaurant3)

session.add(menuItem33)
session.commit()

menuItem34 = MenuItem(name = "Stinky Tofu", description = "Taiwanese dish, deep fried fermented tofu served with pickled cabbage.", price = "", course = "Entree", restaurant = restaurant3)

session.add(menuItem34)
session.commit()



#Menu for Thyme for that
restaurant4 = Restaurant(name = "Thyme for That Vegetarian Cuisine ")

session.add(restaurant4)
session.commit()


menuItem41 = MenuItem(name = "Tres Leches Cake", description = "Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.", price = "", course = "Dessert", restaurant = restaurant4)

session.add(menuItem41)
session.commit()

menuItem42 = MenuItem(name = "Mushroom risotto", description = "Portabello mushrooms in a creamy risotto", price = "", course = "Entree", restaurant = restaurant4)

session.add(menuItem42)
session.commit()

menuItem43 = MenuItem(name = "Honey Boba Shaved Snow", description = "Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", price = "", course = "Dessert", restaurant = restaurant4)

session.add(menuItem43)
session.commit()

menuItem44 = MenuItem(name = "Cauliflower Manchurian", description = "Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions", price = "", course = "Entree", restaurant = restaurant4)

session.add(menuItem44)
session.commit()

menuItem45 = MenuItem(name = "Aloo Gobi Burrito", description = "Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom", price = "", course = "Entree", restaurant = restaurant4)

session.add(menuItem45)
session.commit()




#Menu for Tony's Bistro
restaurant5 = Restaurant(name = "Tony\'s Bistro ")

session.add(restaurant5)
session.commit()


menuItem51 = MenuItem(name = "Shellfish Tower", description = "", price = "", course = "Entree", restaurant = restaurant5)

session.add(menuItem51)
session.commit()

menuItem52 = MenuItem(name = "Chicken and Rice", description = "", price = "", course = "Entree", restaurant = restaurant5)

session.add(menuItem52)
session.commit()

menuItem53 = MenuItem(name = "Mom's Spaghetti", description = "", price = "", course = "Entree", restaurant = restaurant5)

session.add(menuItem53)
session.commit()

menuItem54 = MenuItem(name = "Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)", description = "", price = "", course = "Dessert", restaurant = restaurant5)

session.add(menuItem54)
session.commit()

menuItem55 = MenuItem(name = "Tonkatsu Ramen", description = "Noodles in a delicious pork-based broth with a soft-boiled egg", price = "", course = "Entree", restaurant = restaurant5)

session.add(menuItem55)
session.commit()




#Menu for Andala's 
restaurant6 = Restaurant(name = "Andala\'s")

session.add(restaurant6)
session.commit()


menuItem61 = MenuItem(name = "Lamb Curry", description = "Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.", price = "", course = "Entree", restaurant = restaurant6)

session.add(menuItem61)
session.commit()

menuItem62 = MenuItem(name = "Chicken Marsala", description = "Chicken cooked in Marsala wine sauce with mushrooms", price = "", course = "Entree", restaurant = restaurant6)

session.add(menuItem62)
session.commit()

menuItem63 = MenuItem(name = "Potstickers", description = "Delicious chicken and veggies encapsulated in fried dough.", price = "", course = "Entree", restaurant = restaurant6)

session.add(menuItem63)
session.commit()

menuItem64 = MenuItem(name = "Nigiri SamplerMaguro, Sake, Hamachi, Unagi, Uni, TORO!", description = "", price = "", course = "Entree", restaurant = restaurant6)

session.add(menuItem64)
session.commit()




#Menu for Auntie Ann's
restaurant7 = Restaurant(name = "Auntie Ann\'s Diner ")

session.add(restaurant7)
session.commit()

menuItem79 = MenuItem(name = "Chicken Fried Steak", description = "Fresh battered sirloin steak fried and smothered with cream gravy", price = "$8.99", course = "Entree", restaurant = restaurant7)

session.add(menuItem79)
session.commit()

menuItem71 = MenuItem(name = "Boysenberry Sorbet", description = "An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness", price = "", course = "Dessert", restaurant = restaurant7)

session.add(menuItem71)
session.commit()

menuItem72 = MenuItem(name = "Broiled salmon", description = "Salmon fillet marinated with fresh herbs and broiled hot & fast", price = "", course = "Entree", restaurant = restaurant7)

session.add(menuItem72)
session.commit()

menuItem73 = MenuItem(name = "Morels on toast (seasonal)", description = "Wild morel mushrooms fried in butter, served on herbed toast slices", price = "", course = "Entree", restaurant = restaurant7)

session.add(menuItem73)
session.commit()

menuItem74 = MenuItem(name = "Tandoori Chicken", description = "Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.", price = "", course = "Entree", restaurant = restaurant7)

session.add(menuItem74)
session.commit()




#Menu for Cocina Y Amor
restaurant8 = Restaurant(name = "Cocina Y Amor ")

session.add(restaurant8)
session.commit()


menuItem81 = MenuItem(name = "Super Burrito Al Pastor", description = "Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", price = "", course = "Entree", restaurant = restaurant8)

session.add(menuItem81)
session.commit()

menuItem82 = MenuItem(name = "Cachapa", description = "Golden brown, corn-based venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ", price = "", course = "Entree", restaurant = restaurant8)

session.add(menuItem82)
session.commit()

print "added menu items!"

