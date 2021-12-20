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

5a. For backend, run the program by executing the startdevserver.py file.

5b. For frontend, run the program by executing the src/frontend.main.py file.

## Better things that could be done:
- 