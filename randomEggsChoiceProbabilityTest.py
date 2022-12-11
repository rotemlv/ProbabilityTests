# Experiment:
# We have a sack with 5 white, 3 black and 2 red eggs
# we randomly pull 2 eggs from the sack
# we want to know the probability of pulling eggs with a certain characteristics
# for example - at least one egg is red, no egg is white, etc.
# This code allows us to define a condition for the experiment,
# and to count the number of occurrences where said condition is met.
# Hence, we get an approximation for the probability of the condition to happen.

from collections.abc import Callable
from random import shuffle
# prepare for multi-processing
# from concurrent.futures import ProcessPoolExecutor

# TODO: remove this if you don't have the external module "tqdm"
# used to show the amount of time left for the running experiment (in console)
from tqdm import tqdm

# This import is used for readability - allows
# user to modify the function "experiment_condition()"
# and get the correct descriptive console output
# as in: change one thing instead of 2 every time
# you want to check a different case
import inspect

NUM_RED_EGGS = 2
NUM_BLACK_EGGS = 3
NUM_WHITE_EGGS = 5

RED, BLACK, WHITE = 0, 1, 2
NUM_OF_EXPERIMENTS = 1_000_000


experiment_array = [RED] * NUM_RED_EGGS + [BLACK] * NUM_BLACK_EGGS + [WHITE] * NUM_WHITE_EGGS


# post-run analysis for some cases
# 0 reds:  0.622186
# 1 reds: 0.3556489
# 2 reds: 0.0221224
# ------- -> total = 0.9999573 (kinda-sorta 1)


# This function is the important one
def experiment_condition(tpl: tuple):
    # we pull 2 eggs from the group, we want the probability of the eggs
    # belonging to a specific group (or not belonging to it)
    # change this function to change the test

    # old test - check for case: 1 black egg and 1 white egg
    # expected_result = {(WHITE, BLACK), (BLACK, WHITE)}
    # return tpl in expected_result

    # another example case: 2 of the eggs is red
    return (RED, RED) == tpl


# TODO: Experimental (test this)
# define a string for the condition of the experiment (for print statements)
# (in fact, converts the last line of the function contents to a string)
DESCRIPTION_OF_EXPERIMENT_CONDITION = inspect.getsource(experiment_condition). \
    split('\n')[-2].strip().replace("tpl", f"{('egg1', 'egg2')}").removeprefix("return ")


def get_shuffled_experiment_array():
    shuffle(experiment_array)
    return experiment_array


def pull_two(eggs_array):
    # even better, we already shuffled the ting
    # assert removed to try and speed this up
    # assert len(eggs_array) > 1
    return eggs_array[0], eggs_array[1]


# initialize experiment specific variables (total runs and successful experiments)
successful_experiments = 0
valid_experiments = NUM_OF_EXPERIMENTS

print(f"Running experiment {NUM_OF_EXPERIMENTS} times for condition {DESCRIPTION_OF_EXPERIMENT_CONDITION}:")

for _ in tqdm(range(NUM_OF_EXPERIMENTS)):
    if experiment_condition(pull_two(get_shuffled_experiment_array())):
        successful_experiments += 1

print(f"Probability for {DESCRIPTION_OF_EXPERIMENT_CONDITION}:"
      f" {successful_experiments / valid_experiments}")


