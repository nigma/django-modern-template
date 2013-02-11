Preparing project for deployment on Heroku
==========================================

Start a Heroku project
----------------------

The `very first step <https://devcenter.heroku.com/articles/quickstart>`_
is to sign up and install `Heroku Toolbel <https://toolbelt.heroku.com/>`_
utilities for interacting with the Heroku API and deploying apps.

To start with Heroku you need your project to be versioned using GIT
(if it is not already)::

    $ git init
    Initialized empty Git repository in ...
    $ git add .
    $ git commit -m "my django app"

The next step is to create a new Heroku application instance or
link your project to an existing one (for example when working in a team
that is already using Heroku for the project).

This should give you a *new* project instance::

    $ heroku apps:create my-project-name
    Creating my-project-name... done, stack is cedar
    http://my-project-name.herokuapp.com/ | git@heroku.com:my-project-name.git
    Git remote heroku added

And this link the repository to an existing one::

    $ heroku git:remote -a my-project-name
    Git remote heroku added.

To verify type::

    $ git remote -v
    heroku     git@heroku.com:my-project-name.git (fetch)
    heroku     git@heroku.com:my-project-name.git (push)

More info:

 - https://devcenter.heroku.com/articles/git
 - https://devcenter.heroku.com/articles/django
 - https://devcenter.heroku.com/articles/multiple-environments

Before actually pushing you project code to Heroku there's a couple of
one-time actions that should performed first. Read on.

Generate a secret key
---------------------

Use django command to generate a fresh secret key and save it in Heroku
environment instead of hard-coding it in the settings file::

    dj generate_secret_key
    heroku config:add DJANGO_SECRET_KEY=<secret key>


Prepare Amazon S3 access keys
-----------------------------

A good practice is to use `AWS IAM`_ to configure access management
and generate a separate pair of Amazon AWS API keys for each project
and project environment (i.e. dev, staging, production, etc.).

.. _AWS IAM: http://aws.amazon.com/iam/

First start with creating Amazon S3 buckets for storing public static files
and media content.

    1. Go to https://console.aws.amazon.com/s3/home
    2. Create a bucket and name it according to your project (for example
       ``project-media`` or similar)

Now use the IAM service to generate API keys and configure access rights for
that bucket:

    1. Go to https://console.aws.amazon.com/iam/home#s=Users
    2. Create new user (name: ``heroku-project-media`` or similar)
    3. On the confirmation screen click "show credentials" and write down
       the access and secret key for further use
    4. Then select the newly created user, click the permissions tab
       at the bottom and click "attach user policy".

       Now in order to create a policy that will narrow access to the media
       bucket only, choose "custom policy" and name it
       ``heroku-project-media-s3`` (or similar).

       Then paste the following sample configuration as the policy content
       (remember to replace the ``project-media`` with your project media
       bucket name)::

        {
            "Statement": [{
                "Effect": "Allow",
                "Action": "s3:*",
                "Resource": [
                    "arn:aws:s3:::project-media",
                    "arn:aws:s3:::project-media/*"
                ]
            }]
        }

After getting the AWS config done, the next step is to save the access keys
in the Heroku config. These will be later read from the server environment
variables by the settings file.

::

    heroku config:add AWS_ACCESS_KEY_ID=<aws access key>
    heroku config:add AWS_SECRET_ACCESS_KEY=<aws secret key>
    heroku config:add AWS_STORAGE_BUCKET_NAME=<aws bucket name>

Additionally make the environment variables available for the
[Slug compilation](https://devcenter.heroku.com/articles/slug-compiler) build
phase. This is required for the ``collectstatic`` and ``compress`` commands to
store static files on S3::

    heroku labs:enable user-env-compile


Install common Heroku addons
----------------------------

::

    heroku addons:add heroku-postgresql:dev
    heroku addons:add pgbackups:auto-month
    heroku addons:add memcachier:dev
    heroku addons:add mailgun:starter
    heroku addons:add newrelic:standard

Deploying project on Heroku
---------------------------

Use GIT to push code changes to Heroku::

    git push heroku master

To invoke Django commands invoke ``heroku run`` with command
to be run on the server as a param. For example to synchronize
the db::

    heroku run dj syncdb
    heroku run dj migrate

