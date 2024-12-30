import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("database/ecommerce.db")
cursor = connection.cursor()

# Create products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
)
""")

# Create chat_logs table
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
""")

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

# Insert mock data (100 products)
products = [
    ("Smartphone", "High-end smartphone with advanced features", 699.99, 50),
    ("Laptop", "Lightweight laptop with powerful performance", 999.99, 30),
    ("Headphones", "Wireless headphones with noise cancellation", 199.99, 100),
    ("Book", "Inspirational book by a renowned author", 14.99, 200),
    ("T-shirt", "Comfortable and stylish cotton t-shirt", 19.99, 150),
    ("Tablet", "Portable tablet with high-resolution display", 499.99, 80),
    ("Smartwatch", "Wearable smartwatch with fitness tracking", 149.99, 60),
    ("Camera", "Digital camera with 4K video recording", 799.99, 40),
    ("Charger", "Fast-charging USB-C charger", 29.99, 120),
    ("Bluetooth Speaker", "Portable Bluetooth speaker with deep bass", 89.99, 75),
    ("Air Purifier", "Air purifier with HEPA filter", 129.99, 50),
    ("Washing Machine", "Energy-efficient washing machine", 399.99, 20),
    ("Refrigerator", "Compact refrigerator with cooling technology", 499.99, 25),
    ("Microwave", "Microwave oven with touch controls", 149.99, 40),
    ("Vacuum Cleaner", "Cordless vacuum cleaner for easy cleaning", 199.99, 30),
    ("Coffee Maker", "Automatic coffee maker with timer function", 79.99, 60),
    ("Blender", "High-speed blender for smoothies and shakes", 89.99, 50),
    ("Toaster", "4-slice toaster with adjustable browning", 39.99, 100),
    ("Iron", "Steam iron with quick heat-up", 49.99, 80),
    ("Hair Dryer", "Professional hair dryer with multiple heat settings", 59.99, 70),
    ("Sofa", "Comfortable 3-seat sofa with modern design", 399.99, 20),
    ("Dining Table", "Wooden dining table with six chairs", 499.99, 15),
    ("Bookshelf", "Wooden bookshelf with adjustable shelves", 129.99, 30),
    ("Lamps", "Adjustable desk lamp with LED light", 19.99, 100),
    ("Curtains", "Stylish curtains for living room", 29.99, 150),
    ("Desk Chair", "Ergonomic desk chair with adjustable height", 89.99, 60),
    ("Shampoo", "Hair shampoo for smooth and shiny hair", 10.99, 200),
    ("Conditioner", "Hair conditioner for moisturizing", 12.99, 180),
    ("Hand Wash", "Liquid hand wash with gentle formula", 3.99, 300),
    ("Toothpaste", "Mint-flavored toothpaste for fresh breath", 2.99, 500),
    ("Face Cream", "Moisturizing face cream with SPF", 19.99, 200),
    ("Deodorant", "Long-lasting deodorant with fresh scent", 5.99, 250),
    ("Sunscreen", "Broad spectrum sunscreen for skin protection", 15.99, 150),
    ("Shaving Cream", "Smooth shaving cream with rich lather", 4.99, 120),
    ("Body Lotion", "Hydrating body lotion for dry skin", 9.99, 180),
    ("Perfume", "Elegant perfume with floral fragrance", 49.99, 70),
    ("Nail Polish", "Long-lasting nail polish in vibrant colors", 7.99, 100),
    ("Mirror", "Full-length mirror with modern design", 59.99, 50),
    ("Yoga Mat", "Non-slip yoga mat for comfortable exercise", 19.99, 100),
    ("Dumbbells", "Adjustable dumbbells for home workout", 29.99, 70),
    ("Resistance Bands", "Set of resistance bands for strength training", 14.99, 60),
    ("Tennis Racket", "Professional tennis racket with high tension strings", 119.99, 40),
    ("Football", "High-quality football for outdoor play", 25.99, 150),
    ("Basketball", "Durable basketball for indoor and outdoor play", 19.99, 200),
    ("Baseball Glove", "Soft leather baseball glove for beginners", 39.99, 80),
    ("Camping Tent", "4-person camping tent with waterproof design", 159.99, 20),
    ("Sleeping Bag", "Insulated sleeping bag for cold weather", 49.99, 30),
    ("Cooler", "Portable cooler with ice retention", 79.99, 50),
    ("Hiking Boots", "Durable hiking boots for outdoor adventures", 89.99, 40),
    ("Sunglasses", "Polarized sunglasses with UV protection", 29.99, 100),
    ("Backpack", "Spacious backpack with multiple compartments", 39.99, 120),
    ("Wallet", "Genuine leather wallet with card holder", 19.99, 150),
    ("Watch", "Elegant wristwatch with stainless steel band", 99.99, 70),
    ("Hat", "Stylish baseball cap with adjustable strap", 14.99, 200),
    ("Gloves", "Winter gloves with thermal insulation", 19.99, 180),
    ("Scarf", "Soft wool scarf for warmth and style", 24.99, 100),
    ("Shoes", "Comfortable sneakers for daily wear", 49.99, 200),
    ("Sandals", "Casual sandals for warm weather", 19.99, 150),
    ("Jacket", "Waterproof jacket for outdoor activities", 59.99, 80),
    ("Sweater", "Cozy sweater for cold weather", 39.99, 70),
    ("Jeans", "Slim-fit jeans with stretchable fabric", 49.99, 200),
    ("Trousers", "Formal trousers with slim cut", 39.99, 180),
    ("Skirt", "Casual skirt for everyday wear", 29.99, 150),
    ("Dress", "Elegant dress for formal occasions", 69.99, 100),
    ("Blouse", "Stylish blouse with floral print", 24.99, 200),
    ("Jacket", "Leather jacket with classic design", 89.99, 50),
    ("Socks", "Cotton socks in various colors", 9.99, 300),
    ("Belt", "Leather belt with durable buckle", 19.99, 250),
    ("Pajamas", "Comfortable pajamas for a good night's sleep", 29.99, 150),
    ("Boots", "Winter boots with waterproof lining", 79.99, 60),
    ("Boots", "Cowboy boots with authentic design", 89.99, 40),
    ("Shorts", "Casual shorts for warm weather", 19.99, 150),
    ("Rug", "Decorative rug for living room", 49.99, 100),
    ("Shower Curtain", "Waterproof shower curtain with modern design", 14.99, 200),
    ("Mattress", "Memory foam mattress for comfort", 199.99, 20),
    ("Pillow", "Soft pillow for neck support", 19.99, 200),
    ("Blanket", "Warm blanket for chilly nights", 29.99, 180),
    ("Curtain", "Linen curtains for living room", 39.99, 100),
    ("Table Lamp", "Adjustable table lamp with touch controls", 29.99, 150),
    ("Fan", "Ceiling fan with energy-efficient motor", 49.99, 50),
    ("Heater", "Portable electric heater for winter", 59.99, 70),
    ("AC", "Window air conditioner with cooling capacity", 299.99, 10),
    ("Air Cooler", "Portable air cooler for cooling", 129.99, 60),
    ("Wall Art", "Decorative canvas wall art", 39.99, 80),
    ("Curtain Rod", "Metal curtain rod with adjustable length", 19.99, 200),
    ("Vase", "Elegant glass vase for home decor", 14.99, 250),
    ("Clock", "Wall clock with modern design", 24.99, 150),
    ("Mirror", "Wall mirror with decorative frame", 49.99, 100),
    ("Photo Frame", "Wooden photo frame for memories", 9.99, 300),
    ("Towel", "Soft cotton towel for bathroom use", 14.99, 200),
    ("Shower Mat", "Non-slip shower mat for bathroom", 19.99, 150),
    ("Soap Dish", "Ceramic soap dish for bathroom", 4.99, 300),
    ("Toothbrush Holder", "Plastic toothbrush holder with multiple slots", 5.99, 200)
]

cursor.executemany("""
INSERT INTO products (name, description, price, stock) VALUES (?, ?, ?, ?)
""", products)

connection.commit()
connection.close()
