# build a graph with n nodes and m edges.
# split the nodes randomly into two groups (uniformly)
# check the number of edges that form a
# connection between the two groups.
# We look for:
# expected value = ?
# in our test n (# of nodes) is given to be an even integer
# IMPORTANT: I assume graph is undirected

from random import randint, shuffle
from math import factorial

# TODO: remove this if you don't have the external module "tqdm"
# used to show the amount of time left for the running experiment (in console)
from tqdm import tqdm


# some ideas about expected value
def maxim_formula(n, m):
    return f"Maxim({n}, {m}) = {(m / 2)=}"


def dima_formula(n, m):
    return f"Dima({n}, {m}) = {((factorial(n // 2) ** 2) * m) / (2 * factorial(n))=}"


# TODO: write this down, check and compare values
# Theoretically, the expected value should be calculated as such:
# use indicators defined for each edge: is edge connecting the 2 groups? (1 / 0) (set = Ai for edge i)
# find probability for an edge to be connecting,
# and sum P(Ai) for i = 1, 2, .. m
# Explanation: set A to be the random variable for the amount of connecting edges
# A = A1 + A2 + ... (because each Ai is an indicator)
# E[A] = E[sum(Ai)]



N = 10
M = 3
NUM_OF_EXPERIMENTS = 100_000
# the one list of nodes to be used in the tests
NODES = [i for i in range(1, N + 1)]


# create m edges for a graph with nodes 1, 2, ... n
def make_edges_for_graph(n, m):
    if n < 1:
        raise Exception(f"Invalid value for n ({n})")
    if m < 0 or m > ((n * (n - 1)) / 2):
        raise Exception(f"Invalid value for m ({m})")
    edges = set()
    # split nodes based on random value:
    for _ in range(m):
        # create m random edges between the nodes
        edge = (randint(1, n), randint(1, n))
        # do not allow self-edges or edges that already exist
        while edge[0] == edge[1] or edge in edges \
                or (edge[1], edge[0]) in edges:
            edge = (randint(1, n), randint(1, n))
        edges.add(edge)
    return edges


# create an n/2, n/2 random split for the given nodes list
def split_graph_randomly(original_nodes, n):
    nodes = original_nodes.copy()
    shuffle(nodes)
    return nodes[:(n // 2)], nodes[(n // 2):]


# the test - count how many edges connect group1 and group2
def test_count_edges_that_connect_2_groups(edges, group1, group2):
    # prep
    connecting_edges = 0
    s1, s2 = set(group1), set(group2)
    # check each edge
    for edge in edges:
        u, v = edge
        # if edge is connecting,
        # increment count of connecting edges
        if u in s1 and v in s2:
            connecting_edges += 1
        elif u in s2 and v in s1:
            connecting_edges += 1
    return connecting_edges


# check a wide range of m values to get a better picture of
# the expected value
while M < 10:
    print(f"Performing experiments for case {N=}, {M=}")
    total_connecting_edges = 0
    for _ in range(NUM_OF_EXPERIMENTS):
        E = make_edges_for_graph(N, M)
        v1, v2 = split_graph_randomly(NODES, N)
        total_connecting_edges += \
            test_count_edges_that_connect_2_groups(E, v1, v2)

    print(f"Done {NUM_OF_EXPERIMENTS} experiments successfully!")
    print(f"On average, we got {total_connecting_edges / NUM_OF_EXPERIMENTS}"
          f" edges connecting the two groups of each graph")
    print(f"{maxim_formula(N,M)}\n{dima_formula(N,M)}\n"
          f"\"The answer\": {(M/2) * (1 + (1/(N-1)))=} (lol), my answer={(M*N)/(2*(N-1))=}\n")
    M += 1
