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

Setup project
-------------

Prepare project
"""""""""""""""
::

    django-admin.py startproject --template=https://github.com/nigma/django-modern-template/zipball/master <project_name>

    cd <project_name>
    git init
    git add .
    git commit -m "Initial commit"

Set heroku env
""""""""""""""
::

    heroku create

    dj generate_secret_key --settings=my_site.conf.test
    heroku config:add DJANGO_SECRET_KEY=<secret key>

    heroku config:add AWS_ACCESS_KEY_ID=<aws access key>
    heroku config:add AWS_SECRET_ACCESS_KEY=<aws secret key>
    heroku config:add AWS_STORAGE_BUCKET_NAME=<aws bucket name>

    heroku labs:enable user-env-compile


Install heroku addons
"""""""""""""""""""""
::

    heroku addons:add heroku-postgresql:dev
    heroku addons:add pgbackups:auto-month
    heroku addons:add memcachier:dev
    heroku addons:add mailgun:starter
    heroku addons:add newrelic:standard


Push and migrate
""""""""""""""""
::

    git push heroku master
    heroku run python manage.py syncdb
    heroku run python manage.py migrate

See docs/deploy-on-heroku.rst for more info.

Commercial Support
------------------

This project has been created to make Django development faster and follow
best practices for own sites and our clients. Contact us at en@ig.ma for
your next project.

.. _en.ig.ma: http://en.ig.ma/
