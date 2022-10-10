"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, 2, 3, 4, 5]],
            "answer": [1, 2, 3, 4, 5]
        },
        {
            "input": [[3, 4, 11, 13, 11, 4, 4, 7, 3]],
            "answer": [4, 4, 4, 3, 3, 11, 11, 7, 13]
        }
    ],
    "Extra": [
        {
            "input": [[99, 99, 55, 55, 21, 21, 10, 10]],
            "answer": [10, 10, 21, 21, 55, 55, 99, 99]
        },
        {
            "input": [[5, 6, 13, 99, 45, 34, 99, 6, 6, 45]],
            "answer": [6, 6, 6, 45, 45, 99, 99, 5, 13, 34]
        }
    ]
}
