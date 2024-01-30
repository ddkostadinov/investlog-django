# InvestLog [![GitHub](https://img.shields.io/github/license/ddkostadinov/investlog?color=red)](https://github.com/ddkostadinov/investlog/blob/main/LICENSE)

## A minimalistic, easy-to-use application for logging and managing investments!

If you'd like to **contribute** and make this much better for other users, have a look at [Issues](https://github.com/ddkostadinov/investlog/issues).

Created something awesome for your fork of the portfolio and want to share it? Feel free to open a [pull request](https://github.com/ddkostadinov/investlog/pulls).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

You'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/).

```
python@v3.8.10 or higher
git@2.25.1 or higher
```

## How To Use

From your command line, clone InvestLog and create a virtual environment:

```bash
# Clone this repository
git clone https://github.com/ddkostadinov/investlog.git

# Go into the repository
cd investlog

# Create a virtual environment
python3 -m venv .venv

# Activate it
source ./.venv/bin/activate

# Go into the main project folder
cd investlog

# Setup default environment variables

# For Linux
cp env.example .env
# For Windows
copy env.example .env

# Install dependencies
pip install -r requirements.txt

```

Now lets create a new Django secret key:

```bash
# Open the Python shell in Django:
python manage.py shell

# Import the generator function:
from django.core.management.utils import get_random_secret_key

# Create a new secret key:
print(get_random_secret_key())

# Copy and paste the printed key inside the .env file that you created:
#.env
DJANGO_SECRET_KEY = "[new secret key]"
EMAIL_RECEIVER = ""
EMAIL_SENDER = ""
EMAIL_PASSWORD = ""

# You can exit the shell:
exit()

```

To start the application, create the migrations and run it:

```bash
# Create migrations:
python manage.py makemigrations

# Migrate them:
python manage.py migrate

# Run app:
python manage.py runserver

```

Now you can check your application at [localhost](http://localhost:8000).

## Sections

✔️ Home\
✔️ Contact\
✔️ About\
✔️ Login\
✔️ Logout\
✔️ Register\
✔️ Dashboard\
✔️ Add Investment\
✔️ Edit Investment\
✔️ Delete Investment\
✔️ Graphs\

## Technologies Used

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Postgres](https://www.postgresql.org/)
- [Bootstrap](https://getbootstrap.com/)
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

---
