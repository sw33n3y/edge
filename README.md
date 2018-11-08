
# Installation

## Quick start

To set up a development environment quickly: 

    1. `$ python -m venv [project_name]`
    2. `$ WIN: activate /Scripts/activate.bat`  BASH: ./[project_name]/bin/activate
    3.  pip install -r requirements.txt
    4.  git clone *

Run migrations:

    python manage.py migrate


### Log Files 

* `django.log`: Contains logs by Django framework like executed SQL statements
* `project.log`: Contains logs from the `project` logger. For example:

        # At the top of your file/module
        import logging
        logger = logging.getLogger("project")

        # Anywhere else in the file
        logger.info('Started processing foo')
