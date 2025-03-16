# VibeTune

A simple Django-based music streaming application that allows users to upload, browse, and listen to songs.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Music Streaming**: Browse and play songs uploaded by users
- **Song Management**: Upload your own songs with cover images
- **Watchlater List**: Save songs to listen to later

## Technologies Used

- **Backend**: Django
- **Database**: SQLite
- **Frontend**: HTML, CSS, Bootstrap
- **Media Handling**: Django's built-in file handling

## Installation

1. Clone the repository
```
git clone https://github.com/yourusername/VibeTune.git
cd VibeTune
```

2. Create and activate a virtual environment
```
python -m venv venv
# On Windows
venv\Scripts\activate
# On MacOS/Linux
source venv/bin/activate
```

3. Install dependencies
```
pip install django Pillow
```

4. Run migrations
```
python manage.py migrate
```

5. Create a superuser (admin)
```
python manage.py createsuperuser
```

6. Start the development server
```
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000/` in your browser

## Usage

### Admin Panel
- Access the admin panel at `http://127.0.0.1:8000/admin/`
- Use the superuser credentials to login
- Manage songs and users from the admin interface

### User Features
- **Sign Up**: Create a new account
- **Login**: Access your account
- **Browse Songs**: View all available songs
- **Song Details**: View details and play a specific song
- **Watchlater**: Save songs to listen to later
- **Upload**: Share your own music with others

## Project Structure

- **myapp/**: Main application
  - **models.py**: Database models for songs and watchlater
  - **views.py**: View functions for rendering templates and handling requests
  - **urls.py**: URL routing for the application
  - **templates/**: HTML templates
  - **static/**: Static files (CSS, JS, etc.)
- **media/**: User-uploaded files
  - **images/**: Song cover images
  - **songs/**: Song audio files
- **VibeTune/**: Project settings and configuration

## Demo

![VibeTune](demo.gif)

## Contributors
- **Vishal K** - Creator & Developer

## Feedback

If you have any feedback, please reach me out at vishalk16801680@gmail.com

