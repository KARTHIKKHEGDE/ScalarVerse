# sklearnk - AI & ML Lab Programs Library
# Each program is stored as a source string and can be returned or executed

import os

# Load all program sources as constants
def _load_program_source(filename):
    """Load program source from file"""
    path = os.path.join(os.path.dirname(__file__), filename)
    if not os.path.exists(path):
        return f"# Error: {filename} not found"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Remove the if __name__ == '__main__': guard for execution
        # but keep it in the returned source code
        return content

def _get_executable_code(source):
    """Convert source code to executable form by removing __name__ guard"""
    lines = source.split('\n')
    result = []
    skip_next = False
    
    for i, line in enumerate(lines):
        # Skip the if __name__ == '__main__': line and unindent its contents
        if "if __name__ == '__main__':" in line or 'if __name__ == "__main__":' in line:
            skip_next = True
            continue
        
        if skip_next and line.strip():
            # Unindent the code that was inside the if block
            result.append(line[4:] if line.startswith('    ') else line)
        elif not skip_next:
            result.append(line)
    
    return '\n'.join(result)

# Store all programs as string constants
PROGRAM1_SOURCE = _load_program_source('program1.py')
PROGRAM2_SOURCE = _load_program_source('program2.py')
PROGRAM3_SOURCE = _load_program_source('program3.py')
PROGRAM4_SOURCE = _load_program_source('program4.py')
PROGRAM5_SOURCE = _load_program_source('program5.py')
PROGRAM6_SOURCE = _load_program_source('program6.py')
PROGRAM7_SOURCE = _load_program_source('program7.py')
PROGRAM8_SOURCE = _load_program_source('program8.py')
PROGRAM9_SOURCE = _load_program_source('program9.py')
PROGRAM10_SOURCE = _load_program_source('program10.py')
PROGRAM11_SOURCE = _load_program_source('program11.py')
PROGRAM12_SOURCE = _load_program_source('program12.py')

# Program 1: Tic Tac Toe
def program1():
    """Returns the source code for Program 1 (Tic Tac Toe)"""
    return PROGRAM1_SOURCE

def program1_run():
    """Executes Program 1 (Tic Tac Toe)"""
    exec(_get_executable_code(PROGRAM1_SOURCE), {})

# Program 2: Alpha Beta Pruning
def program2():
    """Returns the source code for Program 2 (Alpha Beta Pruning)"""
    return PROGRAM2_SOURCE

def program2_run():
    """Executes Program 2 (Alpha Beta Pruning)"""
    exec(_get_executable_code(PROGRAM2_SOURCE), {})

# Program 3: 8 Puzzle (A* Algorithm)
def program3():
    """Returns the source code for Program 3 (8 Puzzle A*)"""
    return PROGRAM3_SOURCE

def program3_run():
    """Executes Program 3 (8 Puzzle A*)"""
    exec(_get_executable_code(PROGRAM3_SOURCE), {})

# Program 4: Hill Climbing
def program4():
    """Returns the source code for Program 4 (Hill Climbing)"""
    return PROGRAM4_SOURCE

def program4_run():
    """Executes Program 4 (Hill Climbing)"""
    exec(_get_executable_code(PROGRAM4_SOURCE), {})

# Program 5: Logistic Regression
def program5():
    """Returns the source code for Program 5 (Logistic Regression)"""
    return PROGRAM5_SOURCE

def program5_run():
    """Executes Program 5 (Logistic Regression)"""
    exec(_get_executable_code(PROGRAM5_SOURCE), {})

# Program 6: Naive Bayes
def program6():
    """Returns the source code for Program 6 (Naive Bayes)"""
    return PROGRAM6_SOURCE

def program6_run():
    """Executes Program 6 (Naive Bayes)"""
    exec(_get_executable_code(PROGRAM6_SOURCE), {})

# Program 7: K-Nearest Neighbors
def program7():
    """Returns the source code for Program 7 (KNN)"""
    return PROGRAM7_SOURCE

def program7_run():
    """Executes Program 7 (KNN)"""
    exec(_get_executable_code(PROGRAM7_SOURCE), {})

# Program 8: K-Means Clustering
def program8():
    """Returns the source code for Program 8 (K-Means)"""
    return PROGRAM8_SOURCE

def program8_run():
    """Executes Program 8 (K-Means)"""
    exec(_get_executable_code(PROGRAM8_SOURCE), {})

# Program 9: Logistic Regression (sklearn)
def program9():
    """Returns the source code for Program 9 (Logistic Regression Sklearn)"""
    return PROGRAM9_SOURCE

def program9_run():
    """Executes Program 9 (Logistic Regression Sklearn)"""
    exec(_get_executable_code(PROGRAM9_SOURCE), {})

# Program 10: Naive Bayes (sklearn)
def program10():
    """Returns the source code for Program 10 (Naive Bayes Sklearn)"""
    return PROGRAM10_SOURCE

def program10_run():
    """Executes Program 10 (Naive Bayes Sklearn)"""
    exec(_get_executable_code(PROGRAM10_SOURCE), {})

# Program 11: KNN (sklearn)
def program11():
    """Returns the source code for Program 11 (KNN Sklearn)"""
    return PROGRAM11_SOURCE

def program11_run():
    """Executes Program 11 (KNN Sklearn)"""
    exec(_get_executable_code(PROGRAM11_SOURCE), {})

# Program 12: K-Means (sklearn)
def program12():
    """Returns the source code for Program 12 (K-Means Sklearn)"""
    return PROGRAM12_SOURCE

def program12_run():
    """Executes Program 12 (K-Means Sklearn)"""
    exec(_get_executable_code(PROGRAM12_SOURCE), {})