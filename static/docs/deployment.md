
# Deployment

[Click here to return to the main README file](README.md)

---

## Environment Variables

### GitPod IDE

| Key | Value |
|---|---|
| SECRET_KEY | ## YOUR SECRET_KEY ## |
| DATABASE_URL | ## YOUR DATABASE_URL ## |

### Non-GitPod IDE

```python
os.environ["SECRET_KEY"] = "## YOUR SECRET_KEY ##"
os.environ["DATABASE_URL"] = "## YOUR DATABASE_URL ##"
os.environ["DEVELOPMENT"] = True
```

### Key-value Pairs

To find the values of each key:

- SECRET_KEY: This is a custom string set up to keep sessions secure. Suggested to create one via [RandomKeygen](https://randomkeygen.com/).
- DATABASE_URL: Use to connect to your database's address. 

---

## Initial Deployment

This site was deployed to Heroku by following these steps:

1. Heroku needs to be told what the requirements are for this project, so go into your GitPod terminal, and create files to explain the requirements by using the following commands:
    - `pip3 freeze --local > requirements.txt`
    - `echo web: python run.py > Procfile` - Ensure there is no blank line after the contents of this file.
2. Push these changes to your repository.
3. Login or sign up to [Heroku](https://www.heroku.com).
4. Select '**Create New App**' in the top right of your dashboard.
5. Choose a unique app name, and select the region closest to you, before clicking '**Create App**'.
6. Go to the '**Deploy**' tab, find '**Deployment Method**', and select '**GitHub**'.
7. Search to find your GitHub repository, and click '**Connect**'. Don't enable automatic deployment yet, as this can cause errors.
8. Go to the '**Settings**' tab, find '**Config Vars**', and click '**Reveal Config Vars**'.
9. Enter key-value pairs that match those in your project files, as shown above in [Environment Variables](#environment-variables).
10. In Heroku, go to the '**Resources**' tab, and add on '**Heroku Postgres**' with the free plan.
11. Make migrations to start using PostgreSQL by running `python3 manage.py makemigrations` then `python3 manage.py migrate`.
12. If it returns `django.db.utils.OperationalError: FATAL: role "xxxxxxxx" does not exist`, then run `unset PGHOSTADDR` in your terminal and run the commands in step 11 again.
13. Load the category and product fixtures by running `python3 manage.py loaddata categories`, then `python3 manage.py loaddata products`.
14. Create a superuser to access the Django admin panel by running `python3 manage.py createsuperuser` then following the instructions in the terminal.
15. Remove the DATABASE_URL from your environment variables or env.py file.
16. Install the Heroku CLI and log in using either `heroku login` or `heroku login -i`.
17. Run `heroku config:set DISABLE_COLLECTSTATIC=1 --app ms4-lead-shot-hazard`.
18. Run `git add .`, `git commit -m "Your commit message here"`, `git push`.
19. Add the hostname of your Heroku app to '**ALLOWED HOSTS**' in your settings.py file. This can be found in Heroku Settings > App Name.
20. Connect Heroku to Git using `git remote add heroku {your heroku git url}`.
21. If you'd like to automatically deploy to Heroku whenever you push to GitHub, do the following:
    - Go to the '**Deploy**' tab in Heroku, and click '**Enable Automatic Deployment**'.
    - In '**Manual Deploy**', choose which branch you'd like to deploy from (I chose '**main**' branch, this is sometimes '**master**').
    - Click '**Deploy Branch**' to deploy your app onto the Heroku servers.
    - Once the app has finished building, click '**Open App**' to open your site.
22. If you don't want to automatically deploy to Heroku, do the following:
    - Enter `git push -u heroku main` or `git push -u heroku master`.
23. Your app will now be running at **<https://{your-app-name}.herokuapp.com/>**

[Back to the top](#deployment-steps)

---

## Forking repo

1. Login or Sign Up to [GitHub](www.github.com).
2. On GitHub, go to [Khalanar/ribbit](https://github.com/Khalanar/ribbit).
3. In the top right, click '**Fork**'.
4. Store your environment variables
    - GitPod
        - Go to GitPod Workspaces.
        - Click '**Settings**'.
        - Store your variables in the '**Variables**' section, as shown above in [Environment Variables](#environment-variables).
    * Another IDE
        - Create an `env.py` file in the root directory of the project.
        - Enter your variables, as shown above in [Environment Variables](#environment-variables).
5. You will also need to install all of the project requirements. This can be done using the command `pip3 install -r requirements.txt`.
6. Type `python3 manage.py runserver` in your GitPod terminal to run your local site of this project.

[Back to the top](#deployment-steps)

---

## Making a Local Clone

1. Clone from GitHub
    - Log in to [GitHub](https://www.github.com) and locate the [Repository](https://github.com/Khalanar/ribbit).
    - Under the repository name, above the list of files, click '**Code**'.
    - Here you can either Clone or Download the repository.
    - Open Git Bash.
    - Change the current working directory to the new location, where you want the cloned directory to be.
    - Type `git clone`, and then paste the URL that was copied in Step 4.
    - Press Enter, and your local clone will be created.
    - Run `git remote rm origin` in your terminal to remove the link to this repo.
2. Install Python's required packages
    - You will need to install all of the project requirements, using the command `pip3 install -r requirements.txt`.
3. Store environment variables
    - GitPod
        - Go to GitPod Workspaces.
        - Click '**Settings**'.
        - Store your variables in the '**Variables**' section, as shown above in [Environment Variables](#environment-variables).
    * Another IDE
        - Create an `env.py` file in the root directory of the project.
        - Enter your variables, as shown above in [Environment Variables](#environment-variables).
4. Migrate database models
    - Run `python3 manage.py makemigrations`.
    - Run `python3 manage.py migrate`.
5. Create a Superuser
    - A superuser is required to access the Django admin panel.
    - Run `python3 manage.py createsuperuser`.
    - Follow the instructions in the terminal.
6. Run the project locally
    - Type `python3 manage.py runserver` in your IDE terminal to run your local site of this project.

For a more detailed version of these steps, go to the [Github Docs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) page on this topic.

