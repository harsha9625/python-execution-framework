# Python Execution & Automated Test Framework

## Overview

This project implements a dynamic Python execution and automated testing framework designed to simulate how coding platforms evaluate user-submitted programs. The system allows Python scripts to be executed with injected runtime variables, captures program output, and validates results against structured test cases.

The project demonstrates core concepts in runtime execution, controlled environments, output handling, and automated verification — essential ideas behind scalable code evaluation systems.

---

## Problem Statement

Modern coding platforms require safe and repeatable ways to execute user code, validate correctness, and provide feedback. This project explores how such systems can be built using Python by:

- Executing scripts dynamically
- Injecting test inputs
- Capturing output streams
- Validating expected behavior

---

## Key Features

- Dynamic Python script execution using controlled runtime environments
- Runtime variable injection for flexible testing
- Output capture via redirected standard streams
- Structured error handling
- Automated validation using JSON-defined test cases
- Pass/fail reporting for scalable evaluation

---

## System Architecture

The framework consists of modular components:

### Execution Engine
Responsible for running Python scripts dynamically while isolating execution context and capturing output.

### Test Runner
Loads structured test cases, executes scripts with inputs, and compares outputs for validation.

### Evaluation Pipeline
Simulates automated assessment workflows similar to online coding platforms.

---

## Project Structure

pyexecutor/
  executor.py       → Core execution engine

runner.py           → Automated test runner  
sample_script.py    → Example script under evaluation  
test_cases.json     → Structured input/output test cases  

---

## How It Works

1. Test cases are defined in JSON format.
2. The runner loads each case sequentially.
3. Runtime variables are injected into the script.
4. Script output is captured and analyzed.
5. Expected vs actual outputs are compared.
6. Pass/fail summary is generated.

---

## How to Run

python runner.py

---

## Learning Outcomes

This project explores:

- Dynamic code execution
- Runtime environment management
- Automated test pipelines
- Output capture and validation
- Software verification workflows
- System-level thinking for scalable evaluation tools

---

## Applications

The framework models ideas used in:

- Online coding platforms
- Automated grading systems
- Debugging tools
- Code evaluation pipelines
- Educational programming environments

---

## Purpose

The goal of this project is to understand how automated execution and validation systems operate internally and to build a lightweight prototype demonstrating these principles using Python.

---

## Author

Harsha Vardhan  
Python Systems & Automation Exploration
