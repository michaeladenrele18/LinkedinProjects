def display_menu(menu):#Function for dsiplaying menu to the user
    for item, details in menu.items():
        print(f"\n- {item}: ${details['price']}")

def display_food_info(menu, food_item):#Function to remove any weird characters
    clean_food_item = food_item.lower().replace(" ", "").replace("○", "").replace("(", "").replace(")", "")
    for item, details in menu.items():
        if clean_food_item in item.lower().replace(" ", ""):
            return f"\n{item}:\nDescription: {details['description']}\nPrice: ${details['price']}"
    return "Sorry, That item is not on the menu"

def calculate_total_1(order, menu):#Function to calculate the total for breakfast
    total = 0
    for item in order:
        total += menu[item]['price']
    return total
def calculate_total_2(order, menu):#Function to calculate the total for lunch/dinner 
    total = 0
    for item in order:
        total += lunch_menu[item]['price']
    return total

#Code to figure out if they want remove service or not
room_service = ""
while room_service.lower() not in ["yes", "no"]:
    room_service = input("Would you like room service? (yes/no): ")
    if room_service.lower() not in ["yes", "no"]:
        print("Please enter 'yes' or 'no'.")

if room_service.lower() == "no":
    print("Ok, a single charge of $50 will be added to your bill.")
#Breakfast Menu
else:
    menu = {
        "Strawberry Banana Pancakes": {
            "description": '''Four fluffy buttermilk pancakes
                              Fresh banana slices
                              Glazed strawberries''',
            "price": 10.49
        },
        "Butter Milk Chocolate Chip Pancakes": {
            "description": '''Four fluffy buttermilk pancakes
                              Chocolate chips
                              Drizzle of chocolate syrup''',
            "price": 10.49
        },
        "Original Buttermilk Pancakes": {
            "description": '''Five Buttermilk pancakes
                              Topped with real butter
		              Maple syrup''',
            "price": 10.49
        },
        "Blueberry Pancakes": {
            "description": '''Four buttermilk pancakes filled with blueberries
		              Topped with blueberry topping''',
            "price": 10.49
        },
        "Strawberry Cheesecake Waffle": {
            "description": '''Belgian waffle
		              Creamy cheesecake mousse
		              Fresh strawberries
		              Whipped topping''',
            "price": 7.99
        },
        "Oreo Cookie Crumble Waffle": {
            "description": '''Belgian waffle
		              Oreo cookie pieces
		              Creamy cheesecake mouse
		              Whipped topping''',
            "price": 7.99
        },
        "Original Waffle": {
            "description": ''' Belgian Waffles''',
            "price": 7.99
        },
        "Spicy poblano Omelet": {
            "description": '''Poblano peppers
		              Red bell peppers and onions
		              Shredded beef
		              Jack and cheddar cheese blend
		              Fresh avocado 
		              Poblano cream 
		              Chopped Serrano Peppers''',
            "price": 13.29
        },
        "Big Steak Omelet": {
            "description": '''Steak
                              Hashbrowns
		              Green peppers
		              Onions
		              Mushrooms
		              Tomatoes
		              Cheddar cheese''',
            "price": 13.59
        },
        "Chicken Fajita Omelet": {
            "description": '''Grilled chicken breast
                              Poblano and red bell peppers
		              Roasted onions
		              Jack and cheddar cheese''',
            "price": 13.29
        },
        "Bacon Temptation Omelet": {
            "description": '''Smoked bacon
                              Jack and Cheddar cheese
                              White cheese sauce
                              Tomatoes and more bacon''',
            "price": 12.29
        },
        "French Toast": {
            "description": '''Original French Toast''',
            "price": 5.99
        },
        "Orange Juice": {
            "description": '''Freshly squeezed Orange Juice''',
            "price": 1.99
        },
        "Apple Juice": {
            "description": '''Apple Juice''',
            "price": 1.99
        },
        "Chocolate Milk": {
            "description": '''Chocolate Milk''',
            "price": 1.99
        },
        "Regular Milk": {
            "description": '''Regular Milk''',
            "price": 1.99
        },
        "Water": {
            "description": '''Aquafina Water''',
            "price": 1.99
    }
    } 

    order = []
    while True:#while loopto keep asking if they want breakfast lunch or dinner
        meal_choice = input("What meal would you like? (breakfast/lunch/dinner): ")
        if meal_choice.lower() not in ["breakfast", "lunch", "dinner"]:
            print("Please enter 'breakfast', 'lunch', or 'dinner'.")
        else:
            break

    if meal_choice.lower() == "breakfast":
        print("\n-----------KAMT INN BREAKFAST MENU------------")
        display_menu(menu)
        while True:
            user_choice_food= input("What would you like to order? (CASE SENSITIVE)(Type 'done' when finished): ")#Another while loop that asks what they would like to order
            if user_choice_food.lower() == "done":
                break
            elif user_choice_food not in menu:
                print("That item is not on the menu. Please choose from the menu.")
            else:
                order.append(user_choice_food)
                user_input_info = input("Would you like info on this item? (yes/no): ")
                if user_input_info.lower() == "yes":
                    print(display_food_info(menu, user_choice_food))




##Lunch/Dinner Menu
    elif meal_choice.lower() == "lunch" or meal_choice.lower() == "dinner" :

            lunch_menu = {
        "Tomato Basil Pasta": {
            "description": '''Grilled chicken
                              Fresh Mozzarella
			      Touch of garlic
			      Penne pasta ''',
            "price": 18.95
        },
        "Fettuccini Alfredo": {
            "description":
            '''Rich parmesan cream sauce
               Either chicken or shrimp''',
            "price": 27.95
        },
        "Pasta Carbonara": {
            "description": '''Spaghetti with smoked bacon
                              Green peas
                              Garlic parmesan cream sauce ''',
            "price": 21.95
        },
        "Spicy Rigatoni Vodka": {
            "description": '''Rigatoni pasta
                              Italian cherry tomatoes
                              Parmesan
                              Fresh basil
                              Pancetta tossed with spicy vodka sauce''',
            "price": 22.95
        },
        "Louisiana Chicken Pasta": {
            "description": '''Parmesan crusted chicken
                              Pasta with mushrooms
                              Peppers and onions in a spicy new Orleans sauce''',
            "price": 23.95
        },
        "Fish and Chips": {
            "description": '''Hand battered and fried crisp
                              Served with Cole slaw
                              French fries
                              Tartar sauce ''',
            "price": 22.50
        },
        "Fried Shrimp Platter": {
            "description": '''Lightly Breaded and fried crisp
                              French fries
                              Cole slaw''',
            "price": 23.95
        },
        "Cajun Salmon": {
            "description": '''A Louisiana classic
                              Blackened with Creole Sauce
                              Mashed Potatoes
                              Buttered corn''',
            "price": 27.95
        },
        "Grilled Rib Eye Steak": {
            "description": '''Served with mashed potatoes and Green beans''',
            "price": 38.95
        },
        "Filet Mignon": {
            "description": '''Served with mashed potatoes and Green beans''',
            "price": 42.95
        },
        "Petite Filet": {
            "description": '''Served with mashed potatoes and Green beans''',
            "price": 36.95
        },
        "The Club Sandwich": {
            "description": '''Freshly roasted turkey breast
                              Bacon
                              Lettuce
                              Tomato
                              Mayonnaise
                              White toast ''',
            "price": 18.95
        },
        "Grilled Chicken and Avocado Club": {
            "description": '''Grilled chicken breast
                              Avocado
                              Bacon
                              Tomato
                              Melted Swiss
                              Herb mayonnaise''',
            "price": 18.95
        },
        "Cuban Sandwich": {
            "description": '''Slow roasted Por
                              Ham
                              Swiss Cheese
                              Pickles
                              Mustard
                              Mayonnaise
                              On a grill pressed roll''',
            "price": 17.95
        },
        "Chicken Parmesan Sandwich": {
            "description": '''Tender chicken lightly coated in Parmesan Breadcrumbs
                              Tomato sauce
                              Melted Cheese
                              Freshly Grilled French roll''',
            "price": 18.95
        },
        "Tossed Green Salad": {
            "description": '''Mixed Greens
                              Assorted Vegetables
                              Tomato and croutons with choice of dressing''',
            "price": 10.95
        },
        "Ceasar Salad": {
            "description": '''Croutons
                              Parmesan Cheese
                              Special Caesar dressing ''',
            "price": 13.95
        },
        "Factory Chopped Salad": {
            "description": '''A blend of julienne romaine
                              Grilled chicken
                              Tomato
                              Avocado
                              Corn
                              Bacon
                              Blue cheese
                              Apple
                              Vinaigrette''',
            "price": 16.95
        },
        "Vegan Cobb Salad": {
            "description": '''Crisp Lettuce
                              Grilled Asparagus
                              Avocado
                              Roasted Beets
                              Green beans
                              Tomato
                              Cucumber
                              Carrot
                              Quinoa
                              Farro almonds
                              Toasted pepitas
                              Vinaigrette''',
            "price": 18.50
        },
        "Hot Fudge Sundae": {
            "description": '''Hot fudge topped with whipped cream and almonds''',
            "price": 12.50
        },
        "Ultimate Red Velvet Cake": {
            "description": '''Layers of red velvet cake and cheesecake
                              Covered in cream cheese frosting
                              White chocolate''',
            "price": 10.50
        },
        "Coconut Cream Pie Cheesecake": {
            "description": '''Coconut cheesecake
                              Vanilla Custard
                              Layer of chocolate
                              Coconut Macaroon crust''',
            "price": 10.50
        },
        "Smirnoff Red Label Vodka": {
            "description": '''750ml''',
            "price": 15.25
        },
        "Absolut Vodka": {
            "description": '''750ml''',
            "price": 25.90
        },
        "Grey Goose Vodka": {
            "description": '''750ml''',
            "price": 35.25
        },
        "Belvedere Vodka": {
            "description": '''750ml''',
            "price": 50.45
        },
        "Yellow Tail Shiraz": {
            "description": '''750ml''',
            "price": 10.20
        },
        "Santa Rita 120 Cabernet Sauvignon": {
            "description": '''750ml''',
            "price": 15.45
        },
        "Meiomi Pinot Noir": {
            "description": '''Regular Milk''',
            "price": 25.20
        },   
        "Opus One Red Blend": {
            "description": '''750ml''',
            "price": 400.90
    }
    }
    print("\n-----------KAMT INN LUNCH/DINNER MENU------------")#Another while loop that continues to ask what they would like to order
    display_menu(lunch_menu)
    while True:
        user_choice_food= input("What would you like to order? (CASE SENSITIVE)(Type 'done' when finished): ")
        if user_choice_food.lower() == "done":
            break
        elif user_choice_food not in lunch_menu:
            print("That item is not on the menu. Please choose from the menu.")
        else:
            order.append(user_choice_food)
            user_input_info = input("Would you like info on this item? (yes/no): ")
            if user_input_info.lower() == "yes":
                print(display_food_info(lunch_menu, user_choice_food))

    total = calculate_total_2(order, lunch_menu)
    print(f"Your total bill is: ${total}")
    print("Thank you for using our room service!")

