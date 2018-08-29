# Pronomial Coreferencing
This is an NLP project for the English language which aims to resolve the pronouns present in a piece of text to reflect the noun that they refer to.

> **Example:**
> *Aaron telephoned Jake to tell him that he lost the laptop.*
> *Aaron telephoned Jake to tell **Jake** that **Aaron** lost the laptop.*

## Prerequisites
1. Python 3.3+ interpreter
2. Python packages that need to be installed are mentioned in `requirements.txt`

## Getting Started
Here is a quick guide to the various files to help you navigate and use the repository.

### `gender_classify.py`
A Machine Learning script that trains a model to classify people names into male or female.

### `main.py`
Core computation is done in this script. Each function in the script does the following:
* **preprocess()** - Contructs a dependency parse and extracts sentence features
* **resolution()** - Maps each pronoun to its noun
* **build_output()** - Constructs the output string that is to be returned
* **main()** - Accepts an input string and returns the resolved string

### `run.py`
The script that must be run to access `main.py`.
It provides two alternative functions to take input from the user:
* **file()** - Provide input as a text file, `input.txt`
* **keyboard()** - Manually type text as input

Call one of the above functions that you need to use in `run.py` as shown:
```
if __name__ == '__main__':
    keyboard()
```

### `data` folder
* `names.csv` - Dataset of people names and the corresponding gender of the person. Used to train the classifier in `gender_classify.py`
* `input.txt` - The text file where you can save your input text which needs to be resolved for pronouns