lifecubomed
===========

Initial setup
-------------

1. Clone this repository.

        git clone git@github.com:ygneo/lifecubomed.git

1. Create a virtualenv for the project.

        mkvirtualenv lifecubomed

1. Install required PyPI packages.

        pip install -r pip-requirements.txt

1. If PIL is being installed wrong, no JPEG or PNG support can be avaliable. As a workaround, uninstall it, if pillow has been correctly installed:

        pip uninstall PIL
        pip uninstall pillow
        pip install pillow

1. Edit settings.py
   - Set the languages you want to have avaliable, and the default one, in LANGUAGES and DEFAULT_LANGUAGE settings.
   - By default, sqlite3 db backend is used. You can change DATABASES setting to fit your needs.
   - Set your TIME_ZONE and your LANGUAGE_CODE.
   - If you're not going to use i18n and/or l10n, you can set USE_I8N and/ot USER_L10N to false.
   - Set your media root absolute path, where the user-uploaded files will be saved.
   - By default, STATIC_ROOT is set to 'static/' directory, relative to settings.py path. Change it if you need it.
   - Change SECRET_KEY to something unique.
   - Django CMS's templates will be loaded by default from 'templates/' directory, relative to settings.py path. Change TEMPLATES if you want something different.
   - Only one sample CMS template is set in CMS_TEMPLATES setting. Add yours.
   - Three sample django cms placeholders are configured. Feel free to change them.
   - A default configuration for logging is made and ready to be modified in LOGGING setting.

1. Use local_settings.py.tpl as a template for your own local_settings.py file, which is git-ignored so you can have different settings per enviroment. It's recommended to configure the DATABASE connection in local_settings.py, since password won't be pushed to the repository. Start by copying the template:

        cp local_settings.py.tpl local_settings.py

1. Optionaly, you can create fab_settings.py from fab_settings.py.tpl if you want to use fabric tasks (see section below).

        cp fab_settings.py.tpl fab_settings.py

1. Create your configured database, and run manage commands to create tables and apply migrations

        ./manage.py syncdb
        ./manage.py migrate

1. Now you should be able to run the development server.

        ./manage.py runserver
