import subprocess, os

subprocess.Popen("flask run", env={
  "FLASK_APP": "src/backend",
  "FLASK_ENV": "development",
  **os.environ.copy()
})
