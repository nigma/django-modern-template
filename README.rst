Modern Django project template
==============================

Opinionated Django project template by `en.ig.ma`_.

- Preconfigured requirements and application settings
- Settings divided into modules (no ``local_settings.py`` madness)
- Ready to deploy on Heroku
- Static files compression
- Basic app structure and templates
- Simple ``dj`` command that invokes ``python manage.py <command>`` from
  any project directory

Prerequisites
-------------

- Python 2.7
- PostgreSQL
- Node.js, npm and lessc for .less development
- AWS S3 storage account (see ``docs/deploy-on-heroku.rst``)

Setup project
-------------

Prepare project
"""""""""""""""

Start with creating a new Django project based on this project template::

    django-admin.py startproject --template=https://github.com/nigma/django-modern-template/zipball/master <project_name>
    cd <project_name>

This will set up and preconfigure your project. Now amend the domain
and site name settings in the ``conf/prod.py``and ``conf/dev.py``
files and you are almost ready for the first commit.

**Note:** the ``startproject`` command seems to skip the
``.heroku/collectstatic_disabled`` source file while copying files
from the template. If the ``.heroku`` directory  is not present in the generated
project root directory, just create it manually and add an empty file
named ``collectstatic_disabled``::

    mkdir .heroku
    touch .heroku/collectstatic_disabled

First commit
""""""""""""

After configuring the project settings you are ready for the
initial commit::

    git init
    git add .
    git commit -m "Initial commit"

Set heroku env
""""""""""""""

Once your project structure is ready, the next step is to create and configure
a heroku instance::

    heroku create

    dj generate_secret_key --settings=my_site.conf.test
    heroku config:add DJANGO_SECRET_KEY=<secret key>

    heroku config:add AWS_ACCESS_KEY_ID=<aws access key>
    heroku config:add AWS_SECRET_ACCESS_KEY=<aws secret key>
    heroku config:add AWS_STORAGE_BUCKET_NAME=<aws bucket name>

    heroku labs:enable user-env-compile

As well as enable basic addons for database, cache and mail::

    heroku addons:add heroku-postgresql:dev
    heroku addons:add pgbackups:auto-month
    heroku addons:add memcachier:dev
    heroku addons:add mailgun:starter
    heroku addons:add newrelic:standard


Push and migrate
""""""""""""""""

You should now be ready to deploy your new project to heroku::

    git push heroku master
    heroku run python manage.py syncdb
    heroku run python manage.py migrate

See ``docs/deploy-on-heroku.rst`` for more info.

Out of the box
""""""""""""""

This is what you get: `dmt.herokuapp.com <http://dmt.herokuapp.com>`_

Commercial Support
------------------

This project has been created to make Django development faster and follow
best practices for own sites and our clients. Contact us at en@ig.ma for
your next project.

.. _en.ig.ma: http://en.ig.ma/
