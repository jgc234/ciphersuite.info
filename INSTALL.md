# Installation Notes

There is one submodule (static/bootstrap) that needs to be updated before we can continue

```bash
git submodule update --init --recursive
```

Get a database ready for django to write to.  Unfortunately SQLite doesn't support
the particular query filters in this project, so you'll need to pick another database.

Create some environment variables to keep Django happy:

```bash
export DJANGO_SECRET_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
export DATABASE_URL=pgsql://username:password@localhost:5432/database
```

For development, sort out a virtual environment and install the dependencies.

```bash
python3 -m venv .venv
source .venv/bin/active
pip install --upgrade pip
pip install -r requirements/requirements-dev.txt
```

```bash
./manage.py makemigrations
./manage.py makemigrations directory
./manage.py migrate
```


