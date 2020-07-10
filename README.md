The app building process:
Signed up for Github and Gitpod.

Went to Code Institute's (CI) Gitpod template [repo.](https://github.com/Code-Institute-Org/gitpod-full-template) and clicked *Use this template*. The new repo. was named and openned in Gitpod, straight from Github.

followed the https://github.com/davidjbuchanan/boutique_ado_v1/blob/master/instructions.txt

at line 25 put SECRET_KEY into the github settings and created an any var before initial commit








The deployment process:

To deploy the app remotely the additional list of add-ons and code are required:

Signed up for a free Heroku accounts

Postgres: A server-based database that runs remotely from the Django app. Note: Django's db.sqlite3 is fine for local development but is not robust for long term storage of data. To install Postgres use `pip3 install psycopg2-binary` from the Git CLI.
dj-database-url: Enables the connection to the Postgress remote database. To install use `pip3 install dj_database_url` from the Git CLI.
Green Unicorn (gunicorn): A web browser for deployed browsing. To install Green Unicorn use `pip3 install gunicorn` from the Git CLI.

Generation of a requirements file for the purposes of informing Heroku which files to install using pip. Migration of installed files accomplished using `pip3 freeze --local > requirements.txt` from the Git CLI.

Generation of a Procfile file for the purposes of informing Heroku that this is to be a web application with a web server called Green Unicorn.
Generate from the Git CLI using `touch Procfile`.
Input `web: gunicorn boutique_ado.wsgi:application` to make Horoku start a web dyno (Note: wsgi allows the handling of HTTP requests like run server does in our local development environment.)

From the CI template it is possible to access the Heroku CLI from the Git CLI (otherwise installation is required from [Heroku]( https://devcenter.heroku.com/articles/heroku-cli)). Using the Heroku CLI you can login using `heroku login`. 

Once authenticated it is necessary to create an app in Heroku too:
Using the CLI enter `heroku apps:create` followed by the app's name and region of creation e.g. `heroku apps:create name --region eu` or region otherwise dependant on your location. 

From the Heroku GUI goto the app; then the resources tab, and then the add-ons input field. From there add Postgress. 

To link the Postgress database in Heroku to the Django app requires an update to the settings.py file with the relevant path information ([see example of settings.py]()): 
1) `Import dj_database_url`
2) Obtain the DATABASE_URL (From the Heroku GUI or CLI using `heroku config`) and save it as an environment variable. CAUTION: see deployment security section below.
3) Add to the existing Database section in settings.py to give: 
    `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}`
4) Run migrations using `python3 manage.py migrate` from the CLI if safe to do so.
5) Add the Heroku host name to the ALLOWED_HOSTS section.

Upload data using `python3 manage.py loaddata categories` and then `python3 manage.py loaddata products`

Temporarily disable the collection of static files to Heroku by using `heroku config:set DISABLE_COLLECTSTATIC=1 --app app name`. This is due to the Heroku's security system not accepting them. 

Before commiting and pushing to Github ensure secret keys are hidden in environment variables. 

Deployment security:
`.gitignore`: Create a file and add to it the following files: `*.sqlite3` ,`*.pyc` and `__pycache__/`. This prevents missuse of the development database.

Create and facilitate the use of environment variables within the settings.py file for the purposes hidding the Django SECRET_KEY; hidding the ALLOWED_HOSTS;hidding the DATABASE_URL; and the setting of debug to `true` for development and `false` for deployed app.

For the setting of debug to `true` for development mode and `false` for deployed mode:
1) Create a variable called development that obtains its value from the operating system level or returns `False`: `development = os.environ.get('DEVELOPMENT', False)`
2) Set DEVELEOPMENT to True in Gitpod's IDE settings section or create a hidden file with this data in a `.gitignore` file
3) Set debug to this variable's value i.e. `DEBUG = development`. This prevents internal source code being displayed on the Heroku hosted site if there are errors.


For the purpose of hidding the Django SECRET_KEY:
1) Set the SECRET_KEY value to one supplied in an environment variable in the operating system level or returns a fail: `SECRET_KEY = os.environ.get('SECRET_KEY', '')`
2) Set SECRET_KEY to a unique and secret string in Gitpod's IDE settings section (or create a hidden file with this data in a `.gitignore` file) to allow development database. Similarly create a second SECRET_KEY environment variable and deposit it in Heroku's GUI using the environment variables section; this will allow external deployment of the site.


For the purpose of hidding the ALLOWED_HOSTS:
1) Set the ALLOWED_HOSTS value to one supplied in an environment variable in the operating system level or returns a development host only: 
`if development:`
    `ALLOWED_HOSTS = ['localhost']`
`else:`
    `ALLOWED_HOSTS = [os.environ.get('HEROKU_HOSTNAME')]`
2) Set the `HEROKU_HOSTNAME` in Heroku's GUI using the environment variables section. This is the url address of the deployed app less the protocol.


For the purpose of hidding the DATABASE_URL:
1) Use an `if` statement to determine if the user is in developer mode or using it as a deployed app. Once that is determined allow access to the local database `db.sqlite3` or the Postgres database that was eluded to earlier. In the event of the latter an environment variable in Heroku will be required for security:
`if development:`
    `DATABASES = {`
        `'default': {`
            `'ENGINE': 'django.db.backends.sqlite3',`
            `'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}}`
`else:`
    `DATABASES = {`
        `'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}`
2) Set the `DATABASE_URL` in Heroku's GUI using the environment variables section.

Now that the IDE contents can be commited and pushed to Github and Heroku the app can be tested for deployment, albeit without the base.css file due to the `DISABLE_COLLECTSTATIC` command previously executed.

The Github repository can be connected to Heroku to minimise the number of dual commits required: Using the Heroku GUI's enter the Deploy tab and set the Deployment Method to Github masterfile. Direct to the appropriate repo and select auto deploy activated.


AWS S33 was used to host the static files and product images.
Created a group. Attached an access policy to the group that allows full S3 access to the S3 'bucket'.
Created a user, that is part of the group, with a unique special access keys.
