# User guide
How to run, test and use the application

## How to run online
#### The app has been ported to Heroku: https://tira-rps.herokuapp.com/
You can simply start the game and play vs the AI. The game shows your current score.

## How to run locally
### 1. Clone the project or download & extract with ZIP

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Running the program:
```bash
flask run
```
The app will open locally and can be used in your browser at http://127.0.0.1:5000/

### 4. You can also test the code:
Run tests and coverage-reports using the following
```bash
invoke test
```
```bash
invoke coverage-report
```
Coverage-report can be found from htmlcov/index.html
### 4. Code quality can be checked by:
```bash
invoke lint
```
