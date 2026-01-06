# sklearnk

Collection of AI & ML lab programs.

## Installation

```bash
pip install sklearnk
```

## Usage

This package provides 12 AI/ML programs. Each program can be used in two ways:

### 1. Get Source Code as Text

```python
import sklearnk

# Returns the full source code as a string
code = sklearnk.program1()
print(code)
```

### 2. Execute the Program

```python
import sklearnk

# Executes the program directly
sklearnk.program1_run()
```

## Program List

- **program1** / **program1_run**: Tic Tac Toe
- **program2** / **program2_run**: Alpha Beta Pruning
- **program3** / **program3_run**: 8 Puzzle (A* Algorithm)
- **program4** / **program4_run**: Hill Climbing
- **program5** / **program5_run**: Logistic Regression
- **program6** / **program6_run**: Naive Bayes
- **program7** / **program7_run**: K-Nearest Neighbors
- **program8** / **program8_run**: K-Means Clustering
- **program9** / **program9_run**: Logistic Regression (sklearn)
- **program10** / **program10_run**: Naive Bayes (sklearn)
- **program11** / **program11_run**: KNN (sklearn)
- **program12** / **program12_run**: K-Means (sklearn)

## Examples

```python
import sklearnk

# Example 1: View source code
source = sklearnk.program3()
print(source)

# Example 2: Run the A* algorithm
sklearnk.program3_run()

# Example 3: Get KNN source and save to file
with open('knn.py', 'w') as f:
    f.write(sklearnk.program7())
```
