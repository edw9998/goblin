import subprocess, os

subprocess.Popen("flask run", env={
  "FLASK_APP": "src/backend",
  "FLASK_ENV": os.getenv("ENVIRONMENT", "development"),
  **os.environ.copy()
})
