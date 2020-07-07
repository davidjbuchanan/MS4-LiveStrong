How I wrote the app:

Signed up for Github, Gitpod and Heroku accounts

Went to Code Institute's (CI) Gitpod template [repo.](https://github.com/Code-Institute-Org/gitpod-full-template) and clicked *Use this template*. The new repo. was named and openned in Gitpod, straight from Github.

Add ons:
Postgres: A server-based database that runs remotely from our Django app. Note: Django's db.sqlite3 is fine for local development but is not robust for long term storage of data. To install Postgres use `pip3 install psycopg2-binary` from the Git CLI.
dj-database-url: Enables the connection to the Postgress remote database. To install use `pip3 install dj_database_url` from the Git CLI.
Green Unicorn: A web browser for deployed browsing. To install Green Unicorn use `pip3 install gunicorn` from the Git CLI.

Generation of a requirements file for the purposes of informing Heroku which files to install using pip. Migration of installed files accomplished using `pip3 freeze --local > requirements.txt` from the Git CLI.

Generation of a Procfile file for the purposes of informing Heroku that this is to be a web application with a web server called Green Unicorn.
Generate from the Git CLI using `touch Procfile`. This should link to wsgi ang gunicorn
( wsgi module: allows it to handle HTTP requests like run server does in our local development environment.)

From the CI template it is possible to access the Heroku CLI from the Git CLI (otherwise installation is required from [Heroku]( https://devcenter.heroku.com/articles/heroku-cli)). Using the Heroku CLI you can login using `heroku login`. 

Once authenticated it is possible to create an app in Heroku too:
Using the CLI enter `heroku apps:create` followed by the app's name and region of creation e.g. `heroku apps:create name --region eu`. 

From the Heroku GUI goto the app; then the resources tab, and then the add-ons input fireld. From there add Postgress. 

To link the Postgress database (created in Heroku) to the Django app requires an update to the settings.py file with the relevant path information:
To do this requires 5 actions: 
1) Import dj_database_url
2) Obtain the DATABASE_URL (From the Heroku GUI or CLI using `heroku config`).
3) Paste the DATABASE_URL into the Database section to give: 
4) Run migrations using `python3 manage.py migrate` from the CLI
5) Add the Heroku host name to the ALLOWED_HOSTS section.


For security a .gitignore file should be created and in it `*.squlite3` and `__pycache__/` should be typed to ensure all cache and database data is hidden from the repo. 


This will have to be "pushed" to both the Github repo. (for commit history) and Heroku app. (for deployment)  


