# Lab 5: Static Code Analysis — To-Do List & Task Manager

LAB5 REPOSITORY : https://github.com/bmeghana-14/L5_37_todo_manager

**Your file:** `todo_manager.py`

Follow the lab handout for the full instructions.

## About the program

A task manager. It adds tasks with a priority, marks them complete, lists pending tasks in priority order, searches by keyword, suggests a task to do next, and saves tasks to tasks.pkl and tasks.json.

The code works, but only just. It has quality, style and security problems of the kind Pylint, Flake8 and Bandit are built to find.

## What to do

1. **Run it first** and read the output carefully:

   ```
   python todo_manager.py
   ```

   It runs a short demonstration and needs no input. Note what it prints, so you can check that it still behaves the same after your fixes.

2. **Install the tools:**

   ```
   python -m pip install pylint bandit flake8
   ```

3. **Run the analysis and save the reports:**

   ```
   python -m pylint todo_manager.py > pylint_report.txt
   python -m bandit -r todo_manager.py > bandit_report.txt
   python -m flake8 todo_manager.py > flake8_report.txt
   ```

4. **Document the issues in `issues.md`.**

   Read all three initial reports and identify at least **4 distinct issues** reported for `todo_manager.py`. Record the actual findings from your reports; do not invent issues or copy generic examples. If more than one tool reports the same underlying problem, record it once and mention both tools in the Tool column.

   For each issue, include:
   - **Issue:** a short name for the problem.
   - **Severity:** High, Medium, or Low. Put High issues first, then Medium, then Low. Consider the security or functional impact when assigning severity; do not treat every style warning as High.
   - **Tool:** Pylint, Bandit, Flake8, or more than one if applicable.
   - **Type:** for example, security, error handling, correctness, maintainability, or style.
   - **Line(s):** the exact line number(s) shown in the report.
   - **Description:** what the tool flagged and why it matters.
   - **Fix Approach:** the specific change you plan to make.

   Use this table format and add one row for each distinct issue:

   | Issue | Severity | Tool | Type | Line(s) | Description | Fix Approach |
   |-------|----------|------|------|---------|-------------|--------------|
   | Actual finding from your report | High/Medium/Low | Tool name | Issue category | Line number(s) | Explain the reported problem and its impact | State the planned correction |
   | ... | ... | ... | ... | ... | ... | ... |

   Make sure the line numbers match the initial reports. Keep the original reports so you can compare them after fixing the code.

5. **Fix the code and verify your changes.**

   - Review the issues in `issues.md` and fix at least **4 of the issues you documented** in `todo_manager.py`.
   - Preserve the program's existing functionality. Do not remove or change the demonstrated task-manager behaviour just to improve the tool scores.
   - After making the fixes, run all three analysis tools again and save the final reports (overwrite the earlier reports or use clearly named final-report files):

     ```
     python -m pylint todo_manager.py > pylint_report.txt
     python -m bandit -r todo_manager.py > bandit_report.txt
     python -m flake8 todo_manager.py > flake8_report.txt
     ```

   - Compare the final reports with your initial reports. Confirm that the issues you fixed no longer appear, and review any warnings that remain.
   - Run `python todo_manager.py` again and compare its output with the initial demonstration to check that the program still works.
   - Update `issues.md` to identify which issues were fixed and note any remaining issues. Do not claim an issue is fixed unless the final reports support it.

   Repeat the fix-and-check cycle if necessary until the results are satisfactory.

6. **Reflect.** Answer the four reflection questions from the handout in `reflection.md`.

## Deliverables

- `todo_manager.py`: your cleaned version, with at least 4 issues fixed.
- `issues.md`: the completed issue table, including severity, tool, issue type, line numbers, fix approach, and the final status of each issue.
- `reflection.md`: your answers to the reflection questions.
- `pylint_report.txt`, `bandit_report.txt`, and `flake8_report.txt`: the final analysis reports.

**Target:** aim for a Pylint score above 9.5 on your final file. A perfect 10.00/10 is very good.

Be ready to explain the bugs you found and how you fixed them. You may be called on to present.
