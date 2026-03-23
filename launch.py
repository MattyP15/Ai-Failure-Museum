#!/usr/bin/env python3
import subprocess, sys, os, shutil, platform

ROOT = os.path.dirname(os.path.abspath(__file__))
VENV = os.path.join(ROOT, ".venv")
CODE = os.path.join(ROOT, "4_code", "djangoCode")
REQUIREMENTS = os.path.join(ROOT, "requirements.txt")
DB_PATH = os.path.join(CODE, "db.sqlite3")

FIXTURES = [
    "museum/fixtures/Accounts.json",
    "museum/fixtures/categories.json",
    "museum/fixtures/exhibits.json",
    "museum/fixtures/quizzes.json",
]

if platform.system() == "Windows":
    PIP = os.path.join(VENV, "Scripts", "pip")
    PYTHON = os.path.join(VENV, "Scripts", "python")
else:
    PIP = os.path.join(VENV, "bin", "pip")
    PYTHON = os.path.join(VENV, "bin", "python")

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def log(colour, label, msg):
    print(f"{colour}{BOLD}[{label}]{RESET} {msg}")

def run(cmd, cwd=None, check=True):
    log(CYAN, "RUN", " ".join(cmd) if isinstance(cmd, list) else cmd)
    result = subprocess.run(cmd, cwd=cwd, shell=isinstance(cmd, str))
    if check and result.returncode != 0:
        log(RED, "FAIL", f"cmd exited with code {result.returncode}")
        sys.exit(result.returncode)
    return result

def main():
    skip_seed = "--skip-seed" in sys.argv
    reset = "--reset" in sys.argv

    log(GREEN, "START", "AI Failure Museum launcher")
    log(YELLOW, "INFO", f"Project root : {ROOT}")
    log(YELLOW, "INFO", f"Django code  : {CODE}")
    log(YELLOW, "INFO", f"Venv path    : {VENV}")
    log(YELLOW, "INFO", f"Python       : {sys.executable} ({platform.python_version()})")
    print()

    if not os.path.isdir(CODE):
        log(RED, "ERROR", f"django project not found  {CODE}")
        sys.exit(1)

    if not os.path.isfile(REQUIREMENTS):
        log(RED, "ERROR", f"requirements.txt not found  {REQUIREMENTS}")
        sys.exit(1)

    #activating venev
    if os.path.isdir(VENV):
        log(GREEN, "VENV", "venv already exists")
    else:
        log(YELLOW, "VENV", "creating virtual environment...")
        run([sys.executable, "-m", "venv", VENV])
        log(GREEN, "VENV", "success")

    log(YELLOW, "CHECK", f"pip location: {PIP}")
    if not os.path.isfile(PIP):
        log(RED, "ERROR", "pip not found inside venv - try deleting .venv and running again")
        sys.exit(1)
    print()

    ##inteall dependencies DEPS
    log(YELLOW, "DEPS", "installing requirements")
    run([PIP, "install", "-r", REQUIREMENTS])
    log(GREEN, "DEPS", " installed")
    print()

    #reset if required 
    if reset and os.path.isfile(DB_PATH):
        log(YELLOW, "RESET", "deleting existing database")
        os.remove(DB_PATH)
        log(GREEN, "RESET", " deleted")
        skip_seed = False
    print()

    #migreate
    log(YELLOW, "DB", "running migrations")
    run([PYTHON, "manage.py", "migrate"], cwd=CODE)
    log(GREEN, "DB", " complete")
    print()

    #seeding data if not skippped
    if skip_seed:
        log(YELLOW, "SEED", "skipping loaddata (--skip-seed)")
    else:
        log(YELLOW, "SEED", "loading fixture data")
        for fixture in FIXTURES:
            fixture_path = os.path.join(CODE, fixture)
            if os.path.isfile(fixture_path):
                run([PYTHON, "manage.py", "loaddata", fixture], cwd=CODE)
                log(GREEN, "SEED", f"loaded  {fixture}")
            else:
                log(RED, "SEED", f"fixture not found: {fixture_path}")
    print()

    #launching
    log(GREEN, "SERVER", "starting development server on http://127.0.0.1:8000")
    log(YELLOW, "TIP", " Ctrl+C to stop the server")
    print()

    try:
        run([PYTHON, "manage.py", "runserver"], cwd=CODE, check=False)
    except KeyboardInterrupt:
        print()
        log(GREEN, "STOP", "server stopped by user")

if __name__ == "__main__":
    main()
