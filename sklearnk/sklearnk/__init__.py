import os

def _get_program_code(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    if not os.path.exists(path):
        return f"Error: {filename} not found."
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def program1():
    """Returns the source code for Program 1 (Tic Tac Toe)"""
    return _get_program_code('program1.py')

def program2():
    """Returns the source code for Program 2 (Alpha Beta Pruning)"""
    return _get_program_code('program2.py')

def program3():
    """Returns the source code for Program 3 (8 Puzzle A*)"""
    return _get_program_code('program3.py')

def program4():
    """Returns the source code for Program 4 (Hill Climbing)"""
    return _get_program_code('program4.py')

def program5():
    """Returns the source code for Program 5 (Logistic Regression)"""
    return _get_program_code('program5.py')

def program6():
    """Returns the source code for Program 6 (Naive Bayes)"""
    return _get_program_code('program6.py')

def program7():
    """Returns the source code for Program 7 (KNN)"""
    return _get_program_code('program7.py')

def program8():
    """Returns the source code for Program 8 (K-Means)"""
    return _get_program_code('program8.py')

def program9():
    """Returns the source code for Program 9 (Logistic Regression Sklearn)"""
    return _get_program_code('program9.py')

def program10():
    """Returns the source code for Program 10 (Naive Bayes Sklearn)"""
    return _get_program_code('program10.py')

def program11():
    """Returns the source code for Program 11 (KNN Sklearn)"""
    return _get_program_code('program11.py')

def program12():
    """Returns the source code for Program 12 (K-Means Sklearn)"""
    return _get_program_code('program12.py')