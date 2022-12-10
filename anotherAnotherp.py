# A testing file for probability testing
# We test the probabilities of a specific case in the Secretary problem:
# (described here)
# https://en.wikipedia.org/wiki/Secretary_problem
# given n candidates, while hiring the top k available, we count and thus estimate
# the probability of a candidate to be hired (functions end with "single_hire")
# and we also look for the Expected value for the number of hires per group of
# n candidates (functions with suffix "expected_hired_count").

from math import log
from random import shuffle

# import tqdm as tqdm

# we have n people
# we accept k people to work for us (the best out of n)
# given a person on level between 1 and n - k
# what is the expected value of the number of people accepted?
# let's say (for example) - do k people get accepted to work on average?
# our guess was k/n
# assume:
N = 2000
K = 2
print(f"n = {N}, k = {K}")
# set number of experiments
NUM_OF_EXP = 10_000

# create an array of n people sorted by their level:
my_candidates = [i for i in range(1, N + 1)]
# we are only interested in the first N candidates (as the last K are sure to get in):
experiment_relevant_candidates = set(my_candidates[0:N-K])


# helper function to decide if candidate is good enough for hire
def my_better_than_min(arr, element, k):
    if len(arr) < k:
        return True
    return element > min(arr)


# hiring algorithm
def hire_k_candidates_out_of_n_expected_hired_count(candidates, k):
    # this function receives a permutation of the sorted candidates
    # traverses the array and decides who to hire based on skill (number of candidate)
    number_of_hired_candidates = 0
    hired_candidates = []
    for candidate in candidates:
        if my_better_than_min(hired_candidates, candidate, k):
            # print(f"Candidate {candidate} is better than "
            #       f"{min(hired_candidates) if len(hired_candidates) else float('-inf')}"
            #       f", and hence is added")
            number_of_hired_candidates += 1
            # if necessary, remove the lowest hire from the list
            if len(hired_candidates) == k:
                hired_candidates.remove(min(hired_candidates))

            hired_candidates.append(candidate)

    # print(f"In the end we have hired this group {hired_candidates}")
    return number_of_hired_candidates


# hiring algorithm
def hire_k_candidates_out_of_n_single_hire(candidates, k, candidate_to_check):
    # this function receives a permutation of the sorted candidates
    # traverses the array and decides who to hire based on skill (number of candidate)
    hired_candidates = []
    for candidate in candidates:
        if my_better_than_min(hired_candidates, candidate, k):
            # candidate "i" was chosen
            if candidate == candidate_to_check:
                return True
            # if necessary, remove the lowest hire from the list
            if len(hired_candidates) == k:
                hired_candidates.remove(min(hired_candidates))
            hired_candidates.append(candidate)
    return False


# hiring algorithm
def hire_k_candidates_out_of_n_single_hire_using_set(candidates, k, candidate_to_check):
    # this function receives a permutation of the sorted candidates
    # traverses the array and decides who to hire based on skill (number of candidate)
    hired_candidates = set()
    for candidate in candidates:
        if my_better_than_min(hired_candidates, candidate, k):
            # candidate "i" was chosen
            if candidate == candidate_to_check:
                return True
            # if necessary, remove the lowest hire from the list
            if len(hired_candidates) == k:
                hired_candidates.remove(min(hired_candidates))
            hired_candidates.add(candidate)
    return False


def main_test_for_hiring_probability_of_each_candidate():
    for c in range(1,N + 1):
        successful_experiments = 0
        for _ in range(NUM_OF_EXP):
            # create a permutation of candidates array:
            shuffled_candidates = my_candidates.copy()
            shuffle(shuffled_candidates)

            if hire_k_candidates_out_of_n_single_hire_using_set(shuffled_candidates, K, c):
                successful_experiments += 1
        print(f"\nDone {NUM_OF_EXP} experiments!")
        print(f"Candidate {c} probability to be hired is {successful_experiments / NUM_OF_EXP}")
        print(f"Maxim-Rotem-Dima (k / (n - i + 1),"
              f" for values of k <= n - k) formula gave us {(K / (N - c + 1)) if N - c + 1 != 0 else 1}")


def main_test_for_expected_hired_count():
    total_candidates_hired = 0
    for _ in range(NUM_OF_EXP):
        # create a permutation of candidates array:
        shuffled_candidates = my_candidates.copy()
        shuffle(shuffled_candidates)
        total_candidates_hired += hire_k_candidates_out_of_n_expected_hired_count(shuffled_candidates, K)
    print(f"\nDone {NUM_OF_EXP} experiments!")
    print(f"On average, hired {total_candidates_hired / NUM_OF_EXP} "
          f"candidates each experiment (estimated Expected value)!")
    print(f"{K * log(N / K)=}")


main_test_for_expected_hired_count()
