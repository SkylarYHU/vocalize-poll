# Vocalize

Vocalize is a dynamic polling website where users can create, vote, and share polls with ease. It offers a seamless experience with user authentication, data visualization, and sharing options, making it ideal for gathering opinions and making decisions interactively.

- **Live Site**: [https://vocalize.up.railway.app/](https://vocalize.up.railway.app/)


## Features
- **User Authentication**: Login and register functionality.
- **Poll Management**: Create new polls, view all polls, and delete polls created by the user.
- **Voting System**: Users can cast their votes on available polls.
- **Results Visualization**: Doughnut charts dynamically display poll results.
- **Sharing Options**: Share polls via a link or social media platforms.
- **Media Storage**: Store and manage media files using AWS S3.

## Technology Stack
- **Backend**: Python 3.12.3, Django 5.1.1
- **Frontend**: HTML, CSS, JavaScript
- **Data Visualization**: Chart.js for dynamic doughnut charts
- **Storage**: AWS S3 for media file storage
- **Deployment**: Hosted on Railway

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/SkylarYHU/vocalize-poll.git
cd vocalize-poll
```

### 2. Set Up a Virtual Environment (Optional)
```bash
pipenv shell
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
- SECRET_KEY
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_STORAGE_BUCKET_NAME
- AWS_S3_REGION_NAME

### 5. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Collect Static Files
```bash
python manage.py collectstatic
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

### 8. Access the Website
Open your browser and navigate to: http://127.0.0.1:8000.

## License
This project is available for personal and educational use under a Non-Commercial Use License Agreement.

You may not use this work for commercial purposes without prior written permission from the creator.

For details or inquiries, please contact: skylarhyn@gmail.com.


