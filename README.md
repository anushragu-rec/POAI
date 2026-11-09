# POAI – Principles of Artificial Intelligence Lab

**Course code:** AI23231  
**Department:** Artificial Intelligence and Machine Learning  
**College:** Rajalakshmi Engineering College  
**Academic basis:** AI23231 Principles of Artificial Intelligence Lab Manual (Regulation 2023)

This repository contains runnable implementations for the 11 experiments listed in the lab manual. Python programs are used for search, game playing, reasoning, planning and fuzzy inference. Prolog is used for the two introductory logic-programming exercises.

## Experiments

| No. | Experiment | File |
|---|---|---|
| 01 | 8 Queens Problem (Backtracking) | `01_8_Queens/main.py` |
| 02 | Depth First Search | `02_Depth_First_Search/main.py` |
| 03 | MINIMAX Algorithm (Tic-Tac-Toe) | `03_MINIMAX/main.py` |
| 04 | A* Search Algorithm | `04_A_Star/main.py` |
| 05 | Minimum and Maximum of Two Numbers (Prolog) | `05_Min_Max/min_max.pl` |
| 06 | Simple Clauses – Likes Example (Prolog) | `06_Simple_Clauses/likes.pl` |
| 07 | Unification and Resolution | `07_Unification_Resolution/main.py` |
| 08 | Backward Chaining | `08_Backward_Chaining/main.py` |
| 09 | Forward Chaining | `09_Forward_Chaining/main.py` |
| 10 | Blocks World | `10_Blocks_World/main.py` |
| 11 | Fuzzy Inference System | `11_Fuzzy_Inference/main.py` |

## Requirements

- Python 3.9 or later for experiments 01–04 and 07–11.
- SWI-Prolog or another compatible Prolog interpreter for experiments 05–06.
- Experiment 11 uses `numpy` and `scikit-fuzzy`.

Install Python dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

Open a terminal in the experiment folder and run:

```bash
python main.py
```

For Prolog experiments, open the `.pl` file in SWI-Prolog and run the sample query shown in that file.

## Notes

- The experiment topics and scenarios follow the supplied AI23231 lab manual.
- Some formatting/logic issues in the printed manual code have been corrected so the examples execute consistently.
- The 8 Queens program prints the first solution by default. Set `PRINT_ALL_SOLUTIONS = True` to print every solution.
- Sample outputs are included in each experiment's `README.md`.
# POAI
# POAI
# POAI
