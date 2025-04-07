{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "b141f167-edf7-4569-973e-676cdec9fcbf",
      "cell_type": "code",
      "source": "import numpy as np\n\ndef matrix_multiplication():\n    A = np.array([[1, 2], [3, 4]])\n    B = np.array([[5, 6], [7, 8]])\n    result = np.dot(A, B)\n    print(\"Matrix Multiplication Result:\\n\", result)\n\nif __name__ == \"__main__\":\n    matrix_multiplication()\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "11712595-eace-4ec3-b33a-07338c936699",
      "cell_type": "code",
      "source": "import py_compile\n\n# Compile the script\npy_compile.compile(\"Mat_mul.py\")\n\nprint(\"Bytecode compiled successfully!\")",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Bytecode compiled successfully!\n"
        }
      ],
      "execution_count": 1
    },
    {
      "id": "092f318d-6468-4422-9048-50fbe7e746df",
      "cell_type": "code",
      "source": "import dis\n\nwith open(\"Mat_mul.py\") as f:\n    code = f.read()\n\ndis.dis(code)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "  0           0 RESUME                   0\n\n  1           2 LOAD_CONST               0 ('python')\n              4 LOAD_CONST               1 ('Python (Pyodide)')\n              6 LOAD_CONST               0 ('python')\n              8 LOAD_CONST               2 (('name', 'display_name', 'language'))\n             10 BUILD_CONST_KEY_MAP      3\n             12 LOAD_CONST               0 ('python')\n             14 LOAD_CONST               3 (3)\n             16 LOAD_CONST               4 (('name', 'version'))\n             18 BUILD_CONST_KEY_MAP      2\n             20 LOAD_CONST               5 ('.py')\n             22 LOAD_CONST               6 ('text/x-python')\n             24 LOAD_CONST               0 ('python')\n             26 LOAD_CONST               0 ('python')\n             28 LOAD_CONST               7 ('ipython3')\n             30 LOAD_CONST               8 ('3.8')\n             32 LOAD_CONST               9 (('codemirror_mode', 'file_extension', 'mimetype', 'name', 'nbconvert_exporter', 'pygments_lexer', 'version'))\n             34 BUILD_CONST_KEY_MAP      7\n             36 LOAD_CONST              10 (('kernelspec', 'language_info'))\n             38 BUILD_CONST_KEY_MAP      2\n             40 LOAD_CONST              11 (5)\n             42 LOAD_CONST              12 (4)\n             44 LOAD_CONST              13 ('b141f167-edf7-4569-973e-676cdec9fcbf')\n             46 LOAD_CONST              14 ('code')\n             48 LOAD_CONST              15 ('import numpy as np\\n\\ndef matrix_multiplication():\\n    A = np.array([[1, 2], [3, 4]])\\n    B = np.array([[5, 6], [7, 8]])\\n    result = np.dot(A, B)\\n    print(\"Matrix Multiplication Result:\\\\n\", result)\\n\\nif __name__ == \"__main__\":\\n    matrix_multiplication()\\n')\n             50 LOAD_CONST              16 ('trusted')\n             52 LOAD_NAME                0 (true)\n             54 BUILD_MAP                1\n             56 BUILD_LIST               0\n             58 LOAD_NAME                1 (null)\n             60 LOAD_CONST              17 (('id', 'cell_type', 'source', 'metadata', 'outputs', 'execution_count'))\n             62 BUILD_CONST_KEY_MAP      6\n             64 BUILD_LIST               1\n             66 LOAD_CONST              18 (('metadata', 'nbformat_minor', 'nbformat', 'cells'))\n             68 BUILD_CONST_KEY_MAP      4\n             70 RETURN_VALUE\n"
        }
      ],
      "execution_count": 2
    },
    {
      "id": "babbf0bf-a025-4cab-8142-06e0043f6def",
      "cell_type": "code",
      "source": "import dis\nimport collections\n\n# Read the workload.py file as a string\nwith open(\"Mat_mul.py\", \"r\", encoding=\"utf-8\") as f:\n    code = f.read()\n\n# Compile the code into bytecode\ncompiled_code = compile(code, \"Mat_mul.py\", \"exec\")\n\n# Disassemble and count bytecode instructions\ninstruction_counts = collections.Counter(instr.opname for instr in dis.Bytecode(compiled_code))\n\n# Print the instruction frequency\nprint(\"Instruction Counts:\")\nfor instr, count in instruction_counts.items():\n    print(f\"{instr}: {count}\")\n\n# Total number of instructions\nprint(\"\\nTotal Instructions:\", sum(instruction_counts.values()))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Instruction Counts:\nRESUME: 1\nLOAD_CONST: 23\nBUILD_CONST_KEY_MAP: 6\nLOAD_NAME: 2\nBUILD_MAP: 1\nBUILD_LIST: 2\nPOP_TOP: 1\nRETURN_CONST: 1\n\n 37al Instructions:\n"
        }
      ],
      "execution_count": 3
    },
    {
      "id": "2868e33c-e9c5-4cbb-8545-b568e1135fce",
      "cell_type": "code",
      "source": "# Define arithmetic operators to count\narithmetic_operators = ['+', '-', '*', '/', '%']\n\n# Read the workload.py file\nwith open(\"Mat_mul.py\", \"r\", encoding=\"utf-8\") as f:\n    code = f.read()\n\n# Count occurrences of each arithmetic operator\narithmetic_counts = {op: code.count(op) for op in arithmetic_operators}\ntotal_arithmetic_instructions = sum(arithmetic_counts.values())\n\n# Print results\nprint(\"Arithmetic Operation Counts:\", arithmetic_counts)\nprint(\"Total Arithmetic Instructions:\", total_arithmetic_instructions)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Arithmetic Operation Counts: {'+': 1, '-': 29, '*': 1, '/': 3, '%': 1}\nTotal Arithmetic Instructions: 35\n"
        }
      ],
      "execution_count": 4
    },
    {
      "id": "69a474a5-c067-40f5-8ab6-5a546a959c37",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}