# Fitness tracker module

This module perform the following functions: receive information about the completed training, determine the type of training, calculate training results and display an information message about the results of the training.

## Content

- [Requirements](#requirements)
- [How to start](#how-to-start)
- [Project command](#project-command)

## Requirements

- Python 3.11 or higher

## How to start

### 1. Cloning the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/VNCVTKV/hw_python_oop-master.git
cd hw_python_oop-master
```

### 2. Run homework.py

Add into list packages some tuples in format (workout_type, [data]).  
For example:

```python
if __name__ == '__main__':
packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180])
    ]
...
```

For swimming type workout('SWM'), [data] = [action = number of strokes, duration, weight, length_pool, count_pool]

## Project command

- [VNCVTKV](https://t.me/vncvtkv) — python developer
