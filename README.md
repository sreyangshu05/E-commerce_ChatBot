# **E-commerce Chatbot and User Authentication System**

This project implements a simple e-commerce chatbot with user authentication and product search functionality. The chatbot interacts with users to provide information about products, and the system supports user registration, login, and session management.

## Table of Contents:
- Overview
- Features
- Technologies
- Installation
- Usage
- Database Schema


## Overview:

This project includes an interactive chatbot for an e-commerce site, where users can search for products, view product details, and clear chat history. It also features a user authentication system, where users can register, log in, and log out.

## Key Components:

- Chatbot UI: Allows users to interact with the e-commerce chatbot and search for products.
- User Authentication: Users can register and log in to access the chatbot and perform product searches.
- SQLite Database: Used to store user data, chat logs, and product information.

## Features:

- Chatbot: Provides information about products based on user input.
- User Registration and Login: Users can register and log in using a username and password.
- Product Search: Users can search for products and view details such as name, description, price, and stock.
- Chat Log Storage: User queries and chatbot responses are logged and stored in an SQLite database.
- Responsive UI: The application is mobile-friendly and optimized for various devices.

## Technologies:

- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Database: SQLite
- Security: Werkzeug for password hashing

## Installation:
      ```bash
       git clone https://github.com/sreyangshu05/E-commerce_ChatBot.git
       cd ecommerce-chatbot
       python database_setup.py
       python app.py

   

## Usage:

- Register: To use the chatbot, users must first register by providing a username and password.
- Login: After registering, users can log in to access the chatbot.
- Search Products: Type product queries in the chatbot input box to search for items in the database.

### Example:

- Type smartphone in the chatbot to search for smartphone products.
- View the product details like name, description, price, and stock.

## Database Schema:

- users: Stores user information (username, password).
- products: Stores product details (name, description, price, stock).
- chat_logs: Logs user queries and chatbot responses.

  ```bash
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
  );

  CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
  );

  CREATE TABLE IF NOT EXISTS chat_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
  );
