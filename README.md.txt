# 📝 Django Blog CRUD Application

A clean and functional **Django Blog Application** that lets users **Create, Read, Update, and Delete (CRUD)** blog posts.  
Built with Django and styled using simple, responsive CSS — perfect for learning and showcasing Django fundamentals.

## 🌐 Live Deployment  
Your can view the live running project here:
https://blog-crud-arman-e7x1.onrender.com/

🚀 Features

✅ Create new blog posts  
✅ View all posts on the homepage  
✅ Update or edit existing blogs  
✅ Delete unwanted blogs  
✅ Responsive and minimal UI design  


🛠️ Tech Stack

| Layer | Technology |
|--------|-------------|
| **Backend** | Django (Python) |
| **Frontend** | HTML, CSS |
| **Database** | SQLite (default Django DB) |
| **Environment** | Virtualenv / venv |



📂 Project Structure

blog_project/
│
├── blog_app/
│ ├── migrations/
│ ├── templates/
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── create_blog.html
│ │ └── update_blog.html
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── blog_project/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── static/
│ └── css/
│ └── style.css
│
├── db.sqlite3
├── manage.py


⚙️ Installation & Setup

Follow these steps to run the project locally 👇

1️⃣ Clone the Repository
git clone https://github.com/arman2255/blog-crud-arman.git
cd blog-crud-arman
2️⃣ Create & Activate a Virtual Environment
python -m venv venv
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
3️⃣ Install Dependencies
pip install django
4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Start the Development Server
python manage.py runserver
6️⃣ Open in Browser
👉 Visit http://127.0.0.1:8000/ to access your blog.

🎨 UI Overview
Header: Displays “My Blogs” and “Create Blog” buttons

Homepage: Lists all created blogs with title and content previews

Create Page: Form for adding new posts

Update Page: Edit existing posts

Delete Option: Remove posts instantly

👨‍💻 Author
   Arman Khan

💼 Web Developer
📧 armankhan702161@gmail.com
🔗 https://github.com/arman2255

🌟 Support
If you like this project, consider giving it a ⭐ on GitHub!
It helps others discover it and motivates further development.


