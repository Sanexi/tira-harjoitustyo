# Testing

## How to test the code
#### 1. Clone the project or download and extract as ZIP
#### 2. Install dependencies:
```bash
pip install requirements.txt
```
#### 3. Run tests and coverage-reports using the following
```bash
invoke test
```
```bash
invoke coverage-report
```
Coverage-report can be found from htmlcov/index.html

## Performance Testing
In classes_test.py TestRPS.test_random_picks tests how the AI handles random picks. No AI can predict random picks and this AI is no different and returns almost same values for player_wins and ai_wins.

## Coverage report
![week4coverage](https://github.com/Sanexi/tira-harjoitustyo/blob/main/documentation/images/week4coverage.JPG)
