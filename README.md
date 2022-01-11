# goblin

This is the greatest nano forum application of all time. 

## Libraries used:
- MySQL Connector
- Bcrypt
- Flask
- PyJWT
- requests
- python-dotenv

## Usage

1. Create a new environment
```bash
python -m venv venv
```

2. Activate environment (This has to be done every time you run vscode)
```bash
venv/Scripts/activate
```

3. Install required libraries (Do this once)
```bash
python -m pip install -r requirements.txt
```

4. Duplicate `.env.template` file, and rename it into `.env`. Then, fill it with
appropriate details for your application. (If you want to only run backend,
fill the backend section. If only frontend, only fill the frontend section.)

5a. For backend, run the program by executing the `startdevserver.py` file.

5b. For frontend, run the program by executing the `src/frontend.main.py` file.

## Deploying on our web server
To deploy your backend to our web server, reference this tutorial:
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04

For the credentials and how to login to our server, take a look at the TA
Google Drive! (Because the password is there, I don't include it here. DM me
or look in the CS 2024 group)

## How JWT authentication works:
https://www.akana.com/blog/what-is-jwt

## Better things that could be done:
- I've recently seen more and more projects use the `fastapi` library as a flask
alternative in python. From what i've seen it's newer and more performant.
Maybe it's better?
- Don't use mysql-connector. Use Flask-MySQL. This will provide a better output
for SQL queries instead or array in arrays.
- While you're at it, you can study how does flask templates work. It allows you
to create HTML applications instead of our usual CLI app :D
https://pythonbasics.org/flask-tutorial-templates/
- When deploying, deploy flask using uWSGI. Here is how to do it in nginx and in
a VPS:
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04
For apache, search google for it 😎 (Basically, there are two major web servers
available: nginx and apache. I personally like nginx more)
- Lastly, notice how if we update our app through git, we have to
`git fetch; git pull` and restart our server each time. Look up CI/CD in the
internet, with it, it can automatically deploy your web application after
each `git push`. In GitHub, we use "GitHub Actions". I used it for Game Your Fit
for automatic testing and deployment after each push :D
- Learn Node.JS instead, it's better ;)
