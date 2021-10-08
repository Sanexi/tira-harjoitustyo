# RPS AI using Markov Chains
Project is made for bachelor's in computer science at University of Helsinki.

## How 2 run
### 1. Clone the project or download & extract with ZIP
### 2. To run the program in console edit src/app.py: remove ''' from both ends at the end of the code.
On the console you will see:
* What model the AI has chosen to use
* How many total wins and losses you have
* What the current scoring is for the different models (inside [ ])
* What the different models would've picked (inside ( ))

![runonconsole](https://github.com/Sanexi/tira-harjoitustyo/blob/main/documentation/images/temporaryconsole.JPG)

### 3. To test the program you will have to install dependencies:
```bash
pip install requirements.txt
```
And run tests and coverage-reports using the following
```bash
invoke test
```
```bash
invoke coverage-report
```
Coverage-report can be found from htmlcov/index.html
### 4. To test the code quality use the following:
```bash
invoke pylint
```

## Project Documentation
### [Definition](https://github.com/Sanexi/tira-harjoitustyo/blob/main/documentation/definition.md)

### [Testing](https://github.com/Sanexi/tira-harjoitustyo/blob/main/documentation/testing.md)

### Weekly Reports
* [Weekly Report 1](https://github.com/Sanexi/tira-harjoitustyo/blob/main/documentation/weekly_report1.md)
* [Weekly Report 2](https://github.com/Sanexi/tira-harjoitustyo/blob/main/documentation/weekly_report2.md)
* [Weekly Report 3](https://github.com/Sanexi/tira-harjoitustyo/blob/main/documentation/weekly_report3.md)
* [Weekly Report 4](https://github.com/Sanexi/tira-harjoitustyo/blob/main/documentation/weekly_report4.md)
