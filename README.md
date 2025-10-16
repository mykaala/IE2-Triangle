# IE2-Triangle
Template code for the In-Class Exercise 2 on Unit Testing, an exercise that focuses on unit testing and
test effectiveness, using code coverage and mutation analysis.

NOTE: In the following, we will be using the python 3 commands.

# Installation
We advise you to create a virtual enviroment (python venv, conda) to install the packages.
Preferred version of python - **python3.8**. 

1. Run ```pip3 install -r requirements.txt.```
2. Test the setup by running 
  ```
   cd test_suit
   python3 -m test_triangle
   ```
3. Test the initial test suite by running the script: ```test.sh```



# Control Flow Graph

![Control Flow Graph](isTriangle_cfg_numbered.png)

The **Control Flow Graph (CFG)** of `isTriangle.py` shows all potential execution paths.
For example, the path for a *scalene triangle* follows the sequence where all sides are distinct and valid.

You’ll use this CFG to answer analysis questions about variable definitions, references, and execution paths.



# Testing & Analysis

You will create **two test suites** inside the `test_suit/` folder and use the provided shell scripts for code coverage analysis.

## Statement Coverage

**Goal:** Achieve ≥ 95 % statement (line) coverage.

* Create: `test_statementCoverage.py`
* Run:

  ```bash
  ./statement_coverage.sh
  ```
* The report will be generated in:
  `test_suit/statement_html/index.html`


## Decision Coverage

**Goal:** Achieve ≥ 95 % branch (decision) coverage.

* Create: `test_decisionCoverage.py`
* Run:

  ```bash
  ./decision_coverage.sh
  ```
* The report will be generated in:
  `test_suit/decision_html/index.html`



### Coverage Tool

- We will be using the ```Coverage``` tool to analyze statement
coverage and condition coverage. 
- Run the Coverage code analysis scripts (statement_coverage.sh),
  (decision_coverage.sh) and inspect the report it produces. 
- You will find the ```index.html``` inside the generated folders ```statement_html``` and ```decision_html``` respectively in ```'./test_suit``` directory. 
- Useful resources:

  * [Coverage.py documentation](https://coverage.readthedocs.io/en/7.2.7/)
  * [pytest](https://pypi.org/project/pytest/)
  * [unittest](https://docs.python.org/3/library/unittest.html)

##  Mutation Testing (Part 3)

Mutation testing assesses whether your test suite can “kill” code mutants—small program changes that simulate common errors.

###  Provided Mutants

Two mutant versions of the triangle program are included for your analysis:

* [`mutant 1`](./mutants/mutant1/isTriangle.py)
* [`mutant 2`](./mutants/mutant2/isTriangle.py)

Each mutants subfolder contains a modified version of `isTriangle.py`.

###  Your Tasks

1. **Compare** each mutant to the original program:

   * Identify what code was changed.
   * Determine whether the mutant is *detectable* or *undetectable*.

2. **Explain**:

   * Why the mutant behaves differently or identically.
   * Common reasons some mutants remain undetectable.

*(Mutation analysis tools and detailed evaluation are optional for this exercise, but you should manually reason about detectability.)*


<!-- ## Mutation Testing
1. You need to create a test suite namely ```test_mutationAdequate.py ```
2. When you run the command './mutation.sh', you will find a log file ```mutation_output.log``` generated in the directory ```./test_suit```. Check the log file for generated mutants or error messages. 
3. The mutant detection ratio should be approximately **75%** and above. 

NB: python.exe command works for windows system. Use only python if you are working on a UNIX system.

### Mutation Tool

- Run the mutation analysis (mutation.sh) and inspect the set of killed mutants it reports
(mutation report.html/index.html). The generated files will be in the directory ```./test_suit/mutation_report.html```. 
- Check the output log for identifying generated mutants. This will help to create test cases. 
- USEFUL TIP: If a mutant is labeled survived in the mutation report.html/index.html file, your test suite did not catch (a.k.a. did not kill) that mutant. If a mutant is labeled killed, your test suite did
catch (kill) that mutant.

# Troubleshooting
If you encounter an error with ```if self.isAlive():``` from mutpy, do the following:
1. Open ```utils.py``` shown in the error message from the "mutpy" scripts in the installed directory. 
2. Go to the line ```if self.isAlive():```, shown in the error message
3. Make the following change: if self.isAlive(): becomes ```if self.is_alive():```



# Generating Control flow graph (OPTIONAL Reading)
If you are interested to generate the control flow graph we have used in this exercise yourself, you can follow these instructions. We have used the ```py2cfg``` package (https://pypi.org/project/py2cfg/) to generate control flow graph from the file ```isTriangle.py```. Note: Windows users may find that py2cfg has a specific dependency that only works in Unix system. In that case, please execute it in a UNIX virtual machine.

1. Use the following command to install the py2cfg library: ```pip3 install py2cfg --user```
2. Install graphviz for visualizing the generated CFG. In Ubuntu, you can use the following command:
```sudo apt install graphviz```. 
Link to the Graphviz download: https://graphviz.org/download/
3. If you have installed it, then the default command is:
```py2cfg isTriangle.py```. You should find a generated SVG file in the same directory.
4. In a web brower, open the generated SVG file to visualize the CFG. -->


## Submission Instructions

**Due:** Tuesday, **October 21 @ 11:59 PM** (via Gradescope)
This is a **group submission** — only one group member needs to submit.

**Your submission archive should be named:**
`<groupname>-inclass2.zip` (or `.tar.gz`)

It must include:

1. `answers.pdf` or `answers.txt` – Written responses to assignment questions
2. `test_statementCoverage.py` – Statement coverage test suite (≥ 95 %)
3. `test_decisionCoverage.py` – Decision coverage test suite (≥ 95 %)
4. `git-log.txt` – Your project’s commit history (e.g., via `git log > git-log.txt`)
5. *(Optional)* Any additional notes or reports you wish to include

After submission, **add all group members** in Gradescope using the *Group* functionality.

© 2025 CS520 — Software Testing & Analysis
Department of Computer Science, University of Massachusetts Amherst