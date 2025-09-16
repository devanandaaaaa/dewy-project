# The Dewy Ritual

A modern, aesthetic skincare e-commerce web application built using Django, offering a seamless shopping experience for beauty enthusiasts.

## Features

- User Authentication (Register, Login, Logout)
- Product Listing with Categories
- Product Search
- Add to Cart & Update Cart Quantities
- Checkout with Stripe Payment Integration
- Order Tracking Page
- Review & Rating System for Products
- Wishlist Functionality
- Offers/Discounts Page
- AI Chatbot Integration (via OpenAI API)
- Profile Page for User Details
- Responsive Design (Works on Mobile & Desktop)
- Static & Media File Handling
- Order Location Tracking
- Admin Panel for Product Management

## Tech Stack

- Python 3.13  
- Django 4.2  
- SQLite (for Development)  
- Stripe API (for Payment)  
- OpenAI API (for AI Chatbot)  
- Bootstrap 5.3 (for Styling)  
- Static & Media File Management

## Environment Variables

Create a `.env` file in the project root with:

```env
DEBUG=False
SECRET_KEY=your-django-secret-key
ALLOWED_HOSTS=.onrender.com
OPENAI_API_KEY=your_openai_api_key
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_app_password
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
