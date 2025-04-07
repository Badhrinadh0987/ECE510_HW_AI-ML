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
      "source": "import numpy as np\nimport cProfile\n\ndef matrix_multiplication():\n    A = np.array([[1, 2], [3, 4]])\n    B = np.array([[5, 6], [7, 8]])\n    result = np.dot(A, B)\n    print(\"Matrix Multiplication Result:\\n\", result)\n\ncProfile.runctx(\"matrix_multiplication()\", globals(), locals(), sort='cumulative')\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Matrix Multiplication Result:\n [[19 22]\n [43 50]]\n         118 function calls (112 primitive calls) in 0.004 seconds\n\n   Ordered by: cumulative time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}\n        1    0.000    0.000    0.004    0.004 <string>:1(<module>)\n        1    0.000    0.000    0.004    0.004 <ipython-input-1-a654e34e4c80>:4(matrix_multiplication)\n        1    0.000    0.000    0.004    0.004 {built-in method builtins.print}\n        1    0.000    0.000    0.002    0.002 arrayprint.py:582(array2string)\n        1    0.000    0.000    0.002    0.002 arrayprint.py:1652(_array_str_implementation)\n        1    0.000    0.000    0.002    0.002 arrayprint.py:544(_array2string)\n        1    0.000    0.000    0.002    0.002 arrayprint.py:527(wrapper)\n        4    0.001    0.000    0.001    0.000 display.py:19(write)\n        1    0.000    0.000    0.001    0.001 arrayprint.py:473(_get_format_function)\n        1    0.000    0.000    0.001    0.001 arrayprint.py:431(<lambda>)\n        1    0.000    0.000    0.001    0.001 arrayprint.py:1258(__init__)\n        2    0.000    0.000    0.001    0.000 fromnumeric.py:69(_wrapreduction)\n        2    0.001    0.000    0.001    0.000 {method 'reduce' of 'numpy.ufunc' objects}\n        1    0.000    0.000    0.001    0.001 arrayprint.py:806(_formatArray)\n      7/1    0.000    0.000    0.001    0.001 arrayprint.py:815(recurser)\n        1    0.000    0.000    0.001    0.001 fromnumeric.py:2781(max)\n        4    0.000    0.000    0.000    0.000 arrayprint.py:1273(__call__)\n        1    0.000    0.000    0.000    0.000 fromnumeric.py:2925(min)\n        4    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n        4    0.000    0.000    0.000    0.000 arrayprint.py:779(_extendLine_pretty)\n        3    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}\n        1    0.000    0.000    0.000    0.000 arrayprint.py:64(_make_options_dict)\n        1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}\n        1    0.000    0.000    0.000    0.000 {method 'copy' of 'dict' objects}\n        1    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}\n        1    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}\n        3    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}\n        4    0.000    0.000    0.000    0.000 {method 'splitlines' of 'str' objects}\n        1    0.000    0.000    0.000    0.000 {built-in method builtins.id}\n        3    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}\n       41    0.000    0.000    0.000    0.000 {built-in method builtins.len}\n        1    0.000    0.000    0.000    0.000 {built-in method builtins.locals}\n        3    0.000    0.000    0.000    0.000 {built-in method builtins.max}\n        1    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}\n        1    0.000    0.000    0.000    0.000 multiarray.py:750(dot)\n        4    0.000    0.000    0.000    0.000 arrayprint.py:765(_extendLine)\n        2    0.000    0.000    0.000    0.000 {built-in method numpy.array}\n        1    0.000    0.000    0.000    0.000 {built-in method numpy.asarray}\n        1    0.000    0.000    0.000    0.000 arrayprint.py:423(_get_formatdict)\n        1    0.000    0.000    0.000    0.000 fromnumeric.py:2920(_min_dispatcher)\n        1    0.000    0.000    0.000    0.000 fromnumeric.py:2776(_max_dispatcher)\n\n\n"
        }
      ],
      "execution_count": 1
    },
    {
      "id": "fcb82e1c-8d89-48c0-849c-513978410792",
      "cell_type": "code",
      "source": "import dis\nimport ast\nimport inspect\n\ndef matrix_multiplication():\n    import numpy as np\n    A = np.array([[1, 2], [3, 4]])\n    B = np.array([[5, 6], [7, 8]])\n    result = np.dot(A, B)\n    print(\"Matrix Multiplication Result:\\n\", result)\n\ndef analyze_matrix_multiplication():\n    source = inspect.getsource(matrix_multiplication)\n    tree = ast.parse(source)\n\n    print(\"📌 AST Structure:\")\n    print(ast.dump(tree, indent=4))\n\n    print(\"\\n📌 Bytecode Instructions:\")\n    dis.dis(matrix_multiplication)\n\n    print(\"\\n🧠 Potential Parallelism:\")\n    print(\"- Matrix dot product is internally parallelized by NumPy using optimized BLAS libraries.\")\n    print(\"- At a higher level, individual element calculations can be assigned to separate threads or processes.\")\n\nanalyze_matrix_multiplication()\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "📌 AST Structure:\nModule(\n    body=[\n        FunctionDef(\n            name='matrix_multiplication',\n            args=arguments(\n                posonlyargs=[],\n                args=[],\n                kwonlyargs=[],\n                kw_defaults=[],\n                defaults=[]),\n            body=[\n                Import(\n                    names=[\n                        alias(name='numpy', asname='np')]),\n                Assign(\n                    targets=[\n                        Name(id='A', ctx=Store())],\n                    value=Call(\n                        func=Attribute(\n                            value=Name(id='np', ctx=Load()),\n                            attr='array',\n                            ctx=Load()),\n                        args=[\n                            List(\n                                elts=[\n                                    List(\n                                        elts=[\n                                            Constant(value=1),\n                                            Constant(value=2)],\n                                        ctx=Load()),\n                                    List(\n                                        elts=[\n                                            Constant(value=3),\n                                            Constant(value=4)],\n                                        ctx=Load())],\n                                ctx=Load())],\n                        keywords=[])),\n                Assign(\n                    targets=[\n                        Name(id='B', ctx=Store())],\n                    value=Call(\n                        func=Attribute(\n                            value=Name(id='np', ctx=Load()),\n                            attr='array',\n                            ctx=Load()),\n                        args=[\n                            List(\n                                elts=[\n                                    List(\n                                        elts=[\n                                            Constant(value=5),\n                                            Constant(value=6)],\n                                        ctx=Load()),\n                                    List(\n                                        elts=[\n                                            Constant(value=7),\n                                            Constant(value=8)],\n                                        ctx=Load())],\n                                ctx=Load())],\n                        keywords=[])),\n                Assign(\n                    targets=[\n                        Name(id='result', ctx=Store())],\n                    value=Call(\n                        func=Attribute(\n                            value=Name(id='np', ctx=Load()),\n                            attr='dot',\n                            ctx=Load()),\n                        args=[\n                            Name(id='A', ctx=Load()),\n                            Name(id='B', ctx=Load())],\n                        keywords=[])),\n                Expr(\n                    value=Call(\n                        func=Name(id='print', ctx=Load()),\n                        args=[\n                            Constant(value='Matrix Multiplication Result:\\n'),\n                            Name(id='result', ctx=Load())],\n                        keywords=[]))],\n            decorator_list=[],\n            type_params=[])],\n    type_ignores=[])\n\n📌 Bytecode Instructions:\n  5           0 RESUME                   0\n\n  6           2 LOAD_CONST               1 (0)\n              4 LOAD_CONST               0 (None)\n              6 IMPORT_NAME              0 (numpy)\n              8 STORE_FAST               0 (np)\n\n  7          10 LOAD_FAST                0 (np)\n             12 LOAD_ATTR                3 (NULL|self + array)\n             32 LOAD_CONST               2 (1)\n             34 LOAD_CONST               3 (2)\n             36 BUILD_LIST               2\n             38 LOAD_CONST               4 (3)\n             40 LOAD_CONST               5 (4)\n             42 BUILD_LIST               2\n             44 BUILD_LIST               2\n             46 CALL                     1\n             54 STORE_FAST               1 (A)\n\n  8          56 LOAD_FAST                0 (np)\n             58 LOAD_ATTR                3 (NULL|self + array)\n             78 LOAD_CONST               6 (5)\n             80 LOAD_CONST               7 (6)\n             82 BUILD_LIST               2\n             84 LOAD_CONST               8 (7)\n             86 LOAD_CONST               9 (8)\n             88 BUILD_LIST               2\n             90 BUILD_LIST               2\n             92 CALL                     1\n            100 STORE_FAST               2 (B)\n\n  9         102 LOAD_FAST                0 (np)\n            104 LOAD_ATTR                5 (NULL|self + dot)\n            124 LOAD_FAST                1 (A)\n            126 LOAD_FAST                2 (B)\n            128 CALL                     2\n            136 STORE_FAST               3 (result)\n\n 10         138 LOAD_GLOBAL              7 (NULL + print)\n            148 LOAD_CONST              10 ('Matrix Multiplication Result:\\n')\n            150 LOAD_FAST                3 (result)\n            152 CALL                     2\n            160 POP_TOP\n            162 RETURN_CONST             0 (None)\n\n🧠 Potential Parallelism:\n- Matrix dot product is internally parallelized by NumPy using optimized BLAS libraries.\n- At a higher level, individual element calculations can be assigned to separate threads or processes.\n"
        }
      ],
      "execution_count": 2
    },
    {
      "id": "635fe847-ff84-4a99-a982-2079ba5376fe",
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