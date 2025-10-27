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
        [
    {
        "input": [2, 10, ["melhor", "que", "machado", "de", "assis"]],
        "answer": "OK"
    },
    {
        "input": [6, 6, ["b", "c", "d", "e", "f", "g"]],
        "answer": "OK"
    },
    {
        "input": [6, 8, ["aa", "bb", "aa", "bb", "aa", "bb"]],
        "answer": "Inválido"
    },
    {
        "input": [3, 10, ["vida", "2vida", "real"]],
        "answer": "Inválido"
    },
    {
        "input": [3, 10, ["vida", "real_mente", "ok"]],
        "answer": "Inválido"
    },
    {
        "input": [3, 10, ["vida", "Real", "ok"]],
        "answer": "Inválido"
    },
    {
        "input": [3, 10, ["aaaaaaaaaaa", "b", "c"]],
        "answer": "Inválido"
    },
    {
        "input": [3, 10, ["", "vida", "real"]],
        "answer": "Inválido"
    },
    {
        "input": [4, 10, ["vida", "real", "boa"]],
        "answer": "Inválido"
    },
    {
        "input": [5, 10, ["palavra", "palavra", "palavra", "palavra", "palavra"]],
        "answer": "Inválido"
    },
    {
        "input": [4, 10, ["abc", "def", "ghi", "jkl"]],
        "answer": "Inválido"
    },
    {
        "input": [4, 10, ["abc", "def", "ghi", "jkl", "mno", "pqr"]],
        "answer": "OK"
    }
]
    ]
}
