# Implementation

## Directory structure
* README includes brief summary of the project and links to all documentation
* `src`directory has all of project's source code
* Source code is split into modules `app`, `classes`, `constructor` and `routes`
* `src/tests` has automatic unittests for the project
* `documentation` includes all documentation for the project
* User guide can be found in the `documentation` directory

## Project structure
Project's main part is the Markov chain-algortihm that dictates the AI's picks on different rounds (Can be found in `classes.py`). Project has 6 different models trained to defeat most common player strategies. These different models play every round and the best scoring model in the last 6 rounds will be picked against the player. Tied rounds wont be scored and first round is always random. Memory was chosen to be 6 rounds due to a study (source 1) that proved 5-7 rounds being the optimal memory for a RPS AI.

Different models used in the project:
* Model 0: Chooses what would've lost to player's previous choice.
* Model 1: Chooses what would've won player's previous choice.
* Model 2: Chooses what would've tied with player's previous choice.
* Model 3: A Vector model. Player plays in certain pattern (uses a vector) ie. rock>paper>scissors or rock>scissors>paper.
* Model 4: Frequency model. Player tends to pick the same pick most of the time.
* Model 5: Least frequent model. Player tends to picks the least frequent pick.

These models have proven to be fairly effective against players using strategies. However players who are trying to win a machine and thinks about defeating it more deeply might be able to find a strategy to defeat this algorithm.

## Time implementation
Application should be running at O(n) time complexity

## Current flaws in the application
* AI isn't perfect and can be defeated by studying it's techniques. Naive players can be defeated however.

## Sources
* https://arxiv.org/ftp/arxiv/papers/2003/2003.06769.pdf
* https://towardsdatascience.com/how-to-win-over-70-matches-in-rock-paper-scissors-3e17e67e0dab
* https://towardsdatascience.com/building-a-rock-paper-scissors-ai-948ec424132f
* https://towardsai.net/p/artificial-intelligence/towards-an-ai-for-rock-paper-scissors-3fb05780271f
