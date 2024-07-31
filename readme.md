# Pic Talk

Pic Talk is a Django-based web application designed for managing and organizing media content. The application allows users to upload, view, and manage their media files with ease. It is built with Django and uses modern web technologies to provide a seamless user experience.

## Features

- **User Authentication**: Users can sign up, log in, and manage their accounts.
- **Media Upload**: Upload media files and associate them with user accounts.
- **Media Management**: View, edit, and delete media files.
- **Responsive Design**: The application is designed to be accessible and usable across different devices.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Django
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/SAHIL-Sharma21/Pic-Talk.git
   cd pic-talk

2. **Set up a virtual environment**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

3. **Install the required dependencies**

    ```bash
    pip install -r requirements.txt

4. **Apply database migrations**
    ```bash
    python manage.py migrate

5. **Create a superuser (optional)**
    ```bash
    python manage.py createsuperuser

6. **Run the development server**
    ```bash
    Run the development server

Open your browser and navigate to http://127.0.0.1:8000/ to see the application in action.

