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
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Quicksort Result: [1, 1, 2, 3, 6, 8, 10]\n"
        }
      ],
      "execution_count": 6
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
      "id": "81e69ea6-57ed-4a53-8bb4-99a48dfd9ec6",
      "cell_type": "code",
      "source": "import cProfile\n\ndef quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quicksort(left) + middle + quicksort(right)\n\ndef run_quicksort():\n    arr = [3, 6, 8, 10, 1, 2, 1]\n    print(\"Quicksort Result:\", quicksort(arr))\n\ncProfile.runctx(\"run_quicksort()\", globals(), locals(), sort='cumulative')\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Quicksort Result: [1, 1, 2, 3, 6, 8, 10]\n         36 function calls (26 primitive calls) in 0.001 seconds\n\n   Ordered by: cumulative time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}\n        1    0.000    0.000    0.001    0.001 {built-in method builtins.print}\n        1    0.000    0.000    0.001    0.001 <string>:1(<module>)\n        1    0.000    0.000    0.001    0.001 <ipython-input-7-9b6444e68e2d>:12(run_quicksort)\n        4    0.001    0.000    0.001    0.000 display.py:19(write)\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n       16    0.000    0.000    0.000    0.000 {built-in method builtins.len}\n     11/1    0.000    0.000    0.000    0.000 <ipython-input-7-9b6444e68e2d>:3(quicksort)\n\n\n"
        }
      ],
      "execution_count": 7
    },
    {
      "id": "721aaff3-6b51-4635-9d0b-137090470584",
      "cell_type": "code",
      "source": "import dis\nimport ast\nimport inspect\n\ndef quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quicksort(left) + middle + quicksort(right)\n\ndef analyze_quicksort():\n    source = inspect.getsource(quicksort)\n    tree = ast.parse(source)\n\n    print(\"📌 AST Structure:\")\n    print(ast.dump(tree, indent=4))\n\n    print(\"\\n📌 Bytecode Instructions:\")\n    dis.dis(quicksort)\n\n    print(\"\\n🧠 Potential Parallelism:\")\n    print(\"- Recursive calls to quicksort(left) and quicksort(right) are independent.\")\n    print(\"- They can be executed in parallel using multiprocessing or concurrent.futures.\")\n\nanalyze_quicksort()\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "📌 AST Structure:\nModule(\n    body=[\n        FunctionDef(\n            name='quicksort',\n            args=arguments(\n                posonlyargs=[],\n                args=[\n                    arg(arg='arr')],\n                kwonlyargs=[],\n                kw_defaults=[],\n                defaults=[]),\n            body=[\n                If(\n                    test=Compare(\n                        left=Call(\n                            func=Name(id='len', ctx=Load()),\n                            args=[\n                                Name(id='arr', ctx=Load())],\n                            keywords=[]),\n                        ops=[\n                            LtE()],\n                        comparators=[\n                            Constant(value=1)]),\n                    body=[\n                        Return(\n                            value=Name(id='arr', ctx=Load()))],\n                    orelse=[]),\n                Assign(\n                    targets=[\n                        Name(id='pivot', ctx=Store())],\n                    value=Subscript(\n                        value=Name(id='arr', ctx=Load()),\n                        slice=BinOp(\n                            left=Call(\n                                func=Name(id='len', ctx=Load()),\n                                args=[\n                                    Name(id='arr', ctx=Load())],\n                                keywords=[]),\n                            op=FloorDiv(),\n                            right=Constant(value=2)),\n                        ctx=Load())),\n                Assign(\n                    targets=[\n                        Name(id='left', ctx=Store())],\n                    value=ListComp(\n                        elt=Name(id='x', ctx=Load()),\n                        generators=[\n                            comprehension(\n                                target=Name(id='x', ctx=Store()),\n                                iter=Name(id='arr', ctx=Load()),\n                                ifs=[\n                                    Compare(\n                                        left=Name(id='x', ctx=Load()),\n                                        ops=[\n                                            Lt()],\n                                        comparators=[\n                                            Name(id='pivot', ctx=Load())])],\n                                is_async=0)])),\n                Assign(\n                    targets=[\n                        Name(id='middle', ctx=Store())],\n                    value=ListComp(\n                        elt=Name(id='x', ctx=Load()),\n                        generators=[\n                            comprehension(\n                                target=Name(id='x', ctx=Store()),\n                                iter=Name(id='arr', ctx=Load()),\n                                ifs=[\n                                    Compare(\n                                        left=Name(id='x', ctx=Load()),\n                                        ops=[\n                                            Eq()],\n                                        comparators=[\n                                            Name(id='pivot', ctx=Load())])],\n                                is_async=0)])),\n                Assign(\n                    targets=[\n                        Name(id='right', ctx=Store())],\n                    value=ListComp(\n                        elt=Name(id='x', ctx=Load()),\n                        generators=[\n                            comprehension(\n                                target=Name(id='x', ctx=Store()),\n                                iter=Name(id='arr', ctx=Load()),\n                                ifs=[\n                                    Compare(\n                                        left=Name(id='x', ctx=Load()),\n                                        ops=[\n                                            Gt()],\n                                        comparators=[\n                                            Name(id='pivot', ctx=Load())])],\n                                is_async=0)])),\n                Return(\n                    value=BinOp(\n                        left=BinOp(\n                            left=Call(\n                                func=Name(id='quicksort', ctx=Load()),\n                                args=[\n                                    Name(id='left', ctx=Load())],\n                                keywords=[]),\n                            op=Add(),\n                            right=Name(id='middle', ctx=Load())),\n                        op=Add(),\n                        right=Call(\n                            func=Name(id='quicksort', ctx=Load()),\n                            args=[\n                                Name(id='right', ctx=Load())],\n                            keywords=[])))],\n            decorator_list=[],\n            type_params=[])],\n    type_ignores=[])\n\n📌 Bytecode Instructions:\n  5           0 RESUME                   0\n\n  6           2 LOAD_GLOBAL              1 (NULL + len)\n             12 LOAD_FAST                0 (arr)\n             14 CALL                     1\n             22 LOAD_CONST               1 (1)\n             24 COMPARE_OP              26 (<=)\n             28 POP_JUMP_IF_FALSE        2 (to 34)\n\n  7          30 LOAD_FAST                0 (arr)\n             32 RETURN_VALUE\n\n  8     >>   34 LOAD_FAST                0 (arr)\n             36 LOAD_GLOBAL              1 (NULL + len)\n             46 LOAD_FAST                0 (arr)\n             48 CALL                     1\n             56 LOAD_CONST               2 (2)\n             58 BINARY_OP                2 (//)\n             62 BINARY_SUBSCR\n             66 STORE_FAST               1 (pivot)\n\n  9          68 LOAD_FAST                0 (arr)\n             70 GET_ITER\n             72 LOAD_FAST_AND_CLEAR      2 (x)\n             74 SWAP                     2\n             76 BUILD_LIST               0\n             78 SWAP                     2\n        >>   80 FOR_ITER                10 (to 104)\n             84 STORE_FAST               2 (x)\n             86 LOAD_FAST                2 (x)\n             88 LOAD_FAST                1 (pivot)\n             90 COMPARE_OP               2 (<)\n             94 POP_JUMP_IF_TRUE         1 (to 98)\n             96 JUMP_BACKWARD            9 (to 80)\n        >>   98 LOAD_FAST                2 (x)\n            100 LIST_APPEND              2\n            102 JUMP_BACKWARD           12 (to 80)\n        >>  104 END_FOR\n            106 STORE_FAST               3 (left)\n            108 STORE_FAST               2 (x)\n\n 10         110 LOAD_FAST                0 (arr)\n            112 GET_ITER\n            114 LOAD_FAST_AND_CLEAR      2 (x)\n            116 SWAP                     2\n            118 BUILD_LIST               0\n            120 SWAP                     2\n        >>  122 FOR_ITER                10 (to 146)\n            126 STORE_FAST               2 (x)\n            128 LOAD_FAST                2 (x)\n            130 LOAD_FAST                1 (pivot)\n            132 COMPARE_OP              40 (==)\n            136 POP_JUMP_IF_TRUE         1 (to 140)\n            138 JUMP_BACKWARD            9 (to 122)\n        >>  140 LOAD_FAST                2 (x)\n            142 LIST_APPEND              2\n            144 JUMP_BACKWARD           12 (to 122)\n        >>  146 END_FOR\n            148 STORE_FAST               4 (middle)\n            150 STORE_FAST               2 (x)\n\n 11         152 LOAD_FAST                0 (arr)\n            154 GET_ITER\n            156 LOAD_FAST_AND_CLEAR      2 (x)\n            158 SWAP                     2\n            160 BUILD_LIST               0\n            162 SWAP                     2\n        >>  164 FOR_ITER                10 (to 188)\n            168 STORE_FAST               2 (x)\n            170 LOAD_FAST                2 (x)\n            172 LOAD_FAST                1 (pivot)\n            174 COMPARE_OP              68 (>)\n            178 POP_JUMP_IF_TRUE         1 (to 182)\n            180 JUMP_BACKWARD            9 (to 164)\n        >>  182 LOAD_FAST                2 (x)\n            184 LIST_APPEND              2\n            186 JUMP_BACKWARD           12 (to 164)\n        >>  188 END_FOR\n            190 STORE_FAST               5 (right)\n            192 STORE_FAST               2 (x)\n\n 12         194 LOAD_GLOBAL              3 (NULL + quicksort)\n            204 LOAD_FAST                3 (left)\n            206 CALL                     1\n            214 LOAD_FAST                4 (middle)\n            216 BINARY_OP                0 (+)\n            220 LOAD_GLOBAL              3 (NULL + quicksort)\n            230 LOAD_FAST                5 (right)\n            232 CALL                     1\n            240 BINARY_OP                0 (+)\n            244 RETURN_VALUE\n        >>  246 SWAP                     2\n            248 POP_TOP\n\n  9         250 SWAP                     2\n            252 STORE_FAST               2 (x)\n            254 RERAISE                  0\n        >>  256 SWAP                     2\n            258 POP_TOP\n\n 10         260 SWAP                     2\n            262 STORE_FAST               2 (x)\n            264 RERAISE                  0\n        >>  266 SWAP                     2\n            268 POP_TOP\n\n 11         270 SWAP                     2\n            272 STORE_FAST               2 (x)\n            274 RERAISE                  0\nExceptionTable:\n  76 to 94 -> 246 [2]\n  98 to 104 -> 246 [2]\n  118 to 136 -> 256 [2]\n  140 to 146 -> 256 [2]\n  160 to 178 -> 266 [2]\n  182 to 188 -> 266 [2]\n\n🧠 Potential Parallelism:\n- Recursive calls to quicksort(left) and quicksort(right) are independent.\n- They can be executed in parallel using multiprocessing or concurrent.futures.\n"
        }
      ],
      "execution_count": 8
    },
    {
      "id": "818c2648-9bc1-4347-bd8c-ab452129877a",
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