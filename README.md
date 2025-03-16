# VibeTune

VibeTune is a Django-based music streaming application that allows users to upload, browse, and listen to songs.

## Features

- **User Authentication**: Register, login, and logout functionality.  
- **Music Streaming**: Browse and play songs uploaded by users.  
- **Song Management**: Upload your own songs with cover images.  
- **Watchlater List**: Save songs to listen to later.  

## Technologies Used

- **Backend**: Django  
- **Database**: SQLite  
- **Frontend**: HTML, CSS, Bootstrap  
- **Media Handling**: Django's built-in file management  

## Installation

1. **Clone the repository**  
   ```sh
   git clone https://github.com/yourusername/VibeTune.git
   cd VibeTune
   ```

2. **Create and activate a virtual environment**  
   ```sh
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On MacOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```sh
   pip install django Pillow
   ```

4. **Run migrations**  
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (admin)**  
   ```sh
   python manage.py createsuperuser
   ```

6. **Start the development server**  
   ```sh
   python manage.py runserver
   ```

7. **Access the application**  
   Open your browser and visit:  
   ```
   http://127.0.0.1:8000/
   ```

## Usage

### Admin Panel
- Admin dashboard is available at `http://127.0.0.1:8000/admin/`.  
- Login using the superuser credentials.  
- Manage users and uploaded songs from the panel.  

### User Features
- **Sign Up**: Create an account.  
- **Login**: Access the platform.  
- **Browse Songs**: View and play available songs.  
- **Watchlater**: Save songs for future listening.  
- **Upload**: Upload and share music with others.  

## Project Structure

```
VibeTune/
├── myapp/                 # Main application
│   ├── models.py          # Database models for songs & watchlater
│   ├── views.py           # View functions for handling requests
│   ├── urls.py            # URL routing for the application
│   ├── templates/         # HTML templates
│   ├── static/            # Static assets (CSS, JS)
├── media/                 # Uploaded media files
│   ├── images/            # Song cover images
│   ├── songs/             # Song audio files
├── manage.py              # Django management script
└── requirements.txt       # List of dependencies
```

## Demo

![VibeTune Demo](demo.gif)

## Developer & Owner

- **Vishal K** - Creator & Developer  

## Feedback

For feedback or inquiries, contact me at: **vishalk16801680@gmail.com**
