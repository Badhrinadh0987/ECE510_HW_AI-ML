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
      "id": "cd991d4c-2853-497c-bed4-56dd3ced3cfc",
      "cell_type": "code",
      "source": "def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quicksort(left) + middle + quicksort(right)\n\ndef run_quicksort():\n    arr = [3, 6, 8, 10, 1, 2, 1]\n    print(\"Quicksort Result:\", quicksort(arr))\n\nif __name__ == \"__main__\":\n    run_quicksort()\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "6b2afbd5-33d1-494f-a2cf-c6748cfcf5b4",
      "cell_type": "code",
      "source": "import py_compile\n\n# Compile the script\npy_compile.compile(\"Quick_sort.py\")\n\nprint(\"Bytecode compiled successfully!\")",
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
      "id": "4e0d87b8-a8f5-47a0-a0ed-d1039bc4c963",
      "cell_type": "code",
      "source": "import dis\n\nwith open(\"Quick_sort.py\") as f:\n    code = f.read()\n\ndis.dis(code)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "  0           0 RESUME                   0\n\n  1           2 LOAD_CONST               0 ('python')\n              4 LOAD_CONST               1 ('Python (Pyodide)')\n              6 LOAD_CONST               0 ('python')\n              8 LOAD_CONST               2 (('name', 'display_name', 'language'))\n             10 BUILD_CONST_KEY_MAP      3\n             12 LOAD_CONST               0 ('python')\n             14 LOAD_CONST               3 (3)\n             16 LOAD_CONST               4 (('name', 'version'))\n             18 BUILD_CONST_KEY_MAP      2\n             20 LOAD_CONST               5 ('.py')\n             22 LOAD_CONST               6 ('text/x-python')\n             24 LOAD_CONST               0 ('python')\n             26 LOAD_CONST               0 ('python')\n             28 LOAD_CONST               7 ('ipython3')\n             30 LOAD_CONST               8 ('3.8')\n             32 LOAD_CONST               9 (('codemirror_mode', 'file_extension', 'mimetype', 'name', 'nbconvert_exporter', 'pygments_lexer', 'version'))\n             34 BUILD_CONST_KEY_MAP      7\n             36 LOAD_CONST              10 (('kernelspec', 'language_info'))\n             38 BUILD_CONST_KEY_MAP      2\n             40 LOAD_CONST              11 (5)\n             42 LOAD_CONST              12 (4)\n             44 LOAD_CONST              13 ('cd991d4c-2853-497c-bed4-56dd3ced3cfc')\n             46 LOAD_CONST              14 ('code')\n             48 LOAD_CONST              15 ('def quicksort(arr):\\n    if len(arr) <= 1:\\n        return arr\\n    pivot = arr[len(arr) // 2]\\n    left = [x for x in arr if x < pivot]\\n    middle = [x for x in arr if x == pivot]\\n    right = [x for x in arr if x > pivot]\\n    return quicksort(left) + middle + quicksort(right)\\n\\ndef run_quicksort():\\n    arr = [3, 6, 8, 10, 1, 2, 1]\\n    print(\"Quicksort Result:\", quicksort(arr))\\n\\nif __name__ == \"__main__\":\\n    run_quicksort()\\n')\n             50 LOAD_CONST              16 ('trusted')\n             52 LOAD_NAME                0 (true)\n             54 BUILD_MAP                1\n             56 BUILD_LIST               0\n             58 LOAD_NAME                1 (null)\n             60 LOAD_CONST              17 (('id', 'cell_type', 'source', 'metadata', 'outputs', 'execution_count'))\n             62 BUILD_CONST_KEY_MAP      6\n             64 LOAD_CONST              18 ('6b2afbd5-33d1-494f-a2cf-c6748cfcf5b4')\n             66 LOAD_CONST              14 ('code')\n             68 LOAD_CONST              19 ('')\n             70 LOAD_CONST              16 ('trusted')\n             72 LOAD_NAME                0 (true)\n             74 BUILD_MAP                1\n             76 BUILD_LIST               0\n             78 LOAD_NAME                1 (null)\n             80 LOAD_CONST              17 (('id', 'cell_type', 'source', 'metadata', 'outputs', 'execution_count'))\n             82 BUILD_CONST_KEY_MAP      6\n             84 BUILD_LIST               2\n             86 LOAD_CONST              20 (('metadata', 'nbformat_minor', 'nbformat', 'cells'))\n             88 BUILD_CONST_KEY_MAP      4\n             90 RETURN_VALUE\n"
        }
      ],
      "execution_count": 2
    },
    {
      "id": "04cd7bc7-6c4e-44a5-87df-576206d8e532",
      "cell_type": "code",
      "source": "import dis\nimport collections\n\n# Read the workload.py file as a string\nwith open(\"Quick_sort.py\", \"r\", encoding=\"utf-8\") as f:\n    code = f.read()\n\n# Compile the code into bytecode\ncompiled_code = compile(code, \"Quick_sort.py\", \"exec\")\n\n# Disassemble and count bytecode instructions\ninstruction_counts = collections.Counter(instr.opname for instr in dis.Bytecode(compiled_code))\n\n# Print the instruction frequency\nprint(\"Instruction Counts:\")\nfor instr, count in instruction_counts.items():\n    print(f\"{instr}: {count}\")\n\n# Total number of instructions\nprint(\"\\nTotal Instructions:\", sum(instruction_counts.values()))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Instruction Counts:\nRESUME: 1\nLOAD_CONST: 28\nBUILD_CONST_KEY_MAP: 7\nLOAD_NAME: 4\nBUILD_MAP: 2\nBUILD_LIST: 3\nPOP_TOP: 1\nRETURN_CONST: 1\n\n 47al Instructions:\n"
        }
      ],
      "execution_count": 3
    },
    {
      "id": "397f4242-62fb-483e-b2d5-43b01f65b13f",
      "cell_type": "code",
      "source": "# Define arithmetic operators to count\narithmetic_operators = ['+', '-', '*', '/', '%']\n\n# Read the workload.py file\nwith open(\"Quick_sort.py\", \"r\", encoding=\"utf-8\") as f:\n    code = f.read()\n\n# Count occurrences of each arithmetic operator\narithmetic_counts = {op: code.count(op) for op in arithmetic_operators}\ntotal_arithmetic_instructions = sum(arithmetic_counts.values())\n\n# Print results\nprint(\"Arithmetic Operation Counts:\", arithmetic_counts)\nprint(\"Total Arithmetic Instructions:\", total_arithmetic_instructions)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Arithmetic Operation Counts: {'+': 2, '-': 9, '*': 0, '/': 3, '%': 0}\nTotal Arithmetic Instructions: 14\n"
        }
      ],
      "execution_count": 4
    },
    {
      "id": "f9f35a5a-510f-4822-815f-fb34f19c4b0c",
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