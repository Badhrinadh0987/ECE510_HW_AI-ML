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
      "id": "ea949278-449c-4c6a-a913-71ba14bec105",
      "cell_type": "code",
      "source": "import numpy as np\nfrom scipy.integrate import solve_ivp\n\ndef ode_solver():\n    def dydt(t, y): return -2 * y\n    sol = solve_ivp(dydt, [0, 5], [1], method='RK45')\n    print(\"ODE Solution:\", sol.y)\n\nif __name__ == \"__main__\":\n    ode_solver()\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "04a04831-cf41-4196-8e32-826d7c27f317",
      "cell_type": "code",
      "source": "import py_compile\n\n# Compile the script\npy_compile.compile(\"diff_sol.py\")\n\nprint(\"Bytecode compiled successfully!\")",
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
      "id": "1c8be29f-584a-400e-b465-a3823ce8a016",
      "cell_type": "code",
      "source": "import dis\n\nwith open(\"diff_sol.py\") as f:\n    code = f.read()\n\ndis.dis(code)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "  0           0 RESUME                   0\n\n  1           2 LOAD_CONST               0 ('python')\n              4 LOAD_CONST               1 ('Python (Pyodide)')\n              6 LOAD_CONST               0 ('python')\n              8 LOAD_CONST               2 (('name', 'display_name', 'language'))\n             10 BUILD_CONST_KEY_MAP      3\n             12 LOAD_CONST               0 ('python')\n             14 LOAD_CONST               3 (3)\n             16 LOAD_CONST               4 (('name', 'version'))\n             18 BUILD_CONST_KEY_MAP      2\n             20 LOAD_CONST               5 ('.py')\n             22 LOAD_CONST               6 ('text/x-python')\n             24 LOAD_CONST               0 ('python')\n             26 LOAD_CONST               0 ('python')\n             28 LOAD_CONST               7 ('ipython3')\n             30 LOAD_CONST               8 ('3.8')\n             32 LOAD_CONST               9 (('codemirror_mode', 'file_extension', 'mimetype', 'name', 'nbconvert_exporter', 'pygments_lexer', 'version'))\n             34 BUILD_CONST_KEY_MAP      7\n             36 LOAD_CONST              10 (('kernelspec', 'language_info'))\n             38 BUILD_CONST_KEY_MAP      2\n             40 LOAD_CONST              11 (5)\n             42 LOAD_CONST              12 (4)\n             44 LOAD_CONST              13 ('ea949278-449c-4c6a-a913-71ba14bec105')\n             46 LOAD_CONST              14 ('code')\n             48 LOAD_CONST              15 ('import numpy as np\\nfrom scipy.integrate import solve_ivp\\n\\ndef ode_solver():\\n    def dydt(t, y): return -2 * y\\n    sol = solve_ivp(dydt, [0, 5], [1], method=\\'RK45\\')\\n    print(\"ODE Solution:\", sol.y)\\n\\nif __name__ == \"__main__\":\\n    ode_solver()\\n')\n             50 LOAD_CONST              16 ('trusted')\n             52 LOAD_NAME                0 (true)\n             54 BUILD_MAP                1\n             56 BUILD_LIST               0\n             58 LOAD_NAME                1 (null)\n             60 LOAD_CONST              17 (('id', 'cell_type', 'source', 'metadata', 'outputs', 'execution_count'))\n             62 BUILD_CONST_KEY_MAP      6\n             64 BUILD_LIST               1\n             66 LOAD_CONST              18 (('metadata', 'nbformat_minor', 'nbformat', 'cells'))\n             68 BUILD_CONST_KEY_MAP      4\n             70 RETURN_VALUE\n"
        }
      ],
      "execution_count": 2
    },
    {
      "id": "ecc25f3b-b863-4ff6-b963-ed1671848abd",
      "cell_type": "code",
      "source": "import dis\nimport collections\n\n# Read the workload.py file as a string\nwith open(\"diff_sol.py\", \"r\", encoding=\"utf-8\") as f:\n    code = f.read()\n\n# Compile the code into bytecode\ncompiled_code = compile(code, \"diff_sol.py\", \"exec\")\n\n# Disassemble and count bytecode instructions\ninstruction_counts = collections.Counter(instr.opname for instr in dis.Bytecode(compiled_code))\n\n# Print the instruction frequency\nprint(\"Instruction Counts:\")\nfor instr, count in instruction_counts.items():\n    print(f\"{instr}: {count}\")\n\n# Total number of instructions\nprint(\"\\nTotal Instructions:\", sum(instruction_counts.values()))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Instruction Counts:\nRESUME: 1\nLOAD_CONST: 48\nBUILD_CONST_KEY_MAP: 11\nLOAD_NAME: 6\nBUILD_MAP: 4\nBUILD_LIST: 5\nPOP_TOP: 1\nRETURN_CONST: 1\n\n 77al Instructions:\n"
        }
      ],
      "execution_count": 3
    },
    {
      "id": "efbe5f46-8a7b-4dc7-b47f-a154ae3e28f4",
      "cell_type": "code",
      "source": "# Define arithmetic operators to count\narithmetic_operators = ['+', '-', '*', '/', '%']\n\n# Read the workload.py file\nwith open(\"diff_sol.py\", \"r\", encoding=\"utf-8\") as f:\n    code = f.read()\n\n# Count occurrences of each arithmetic operator\narithmetic_counts = {op: code.count(op) for op in arithmetic_operators}\ntotal_arithmetic_instructions = sum(arithmetic_counts.values())\n\n# Print results\nprint(\"Arithmetic Operation Counts:\", arithmetic_counts)\nprint(\"Total Arithmetic Instructions:\", total_arithmetic_instructions)\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Arithmetic Operation Counts: {'+': 0, '-': 25, '*': 2, '/': 2, '%': 0}\nTotal Arithmetic Instructions: 29\n"
        }
      ],
      "execution_count": 4
    },
    {
      "id": "7cb9f530-ad7f-4abd-b3ed-937cdfaa6364",
      "cell_type": "code",
      "source": "import cProfile\ncProfile.run('exec(open(\"diff_sol.py\").read())', sort='cumulative')",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "         11 function calls (10 primitive calls) in 0.022 seconds\n\n   Ordered by: cumulative time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n      2/1    0.002    0.001    0.022    0.022 {built-in method builtins.exec}\n        1    0.000    0.000    0.022    0.022 <string>:1(<module>)\n        1    0.016    0.016    0.016    0.016 {built-in method _io.open}\n        1    0.000    0.000    0.016    0.016 interactiveshell.py:315(_modified_open)\n        1    0.004    0.004    0.004    0.004 {method 'read' of '_io.TextIOWrapper' objects}\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}\n        1    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)\n        1    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)\n        1    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)\n\n\n"
        },
        {
          "ename": "<class 'NameError'>",
          "evalue": "name 'true' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "Cell \u001b[0;32mIn[17], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mcProfile\u001b[39;00m\n\u001b[0;32m----> 2\u001b[0m \u001b[43mcProfile\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mexec(open(\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mdiff_sol.py\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43m).read())\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43msort\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mcumulative\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n",
            "File \u001b[0;32m/lib/python312.zip/cProfile.py:18\u001b[0m, in \u001b[0;36mrun\u001b[0;34m(statement, filename, sort)\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mrun\u001b[39m(statement, filename\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m, sort\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m1\u001b[39m):\n\u001b[0;32m---> 18\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43m_pyprofile\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_Utils\u001b[49m\u001b[43m(\u001b[49m\u001b[43mProfile\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mstatement\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mfilename\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43msort\u001b[49m\u001b[43m)\u001b[49m\n",
            "File \u001b[0;32m/lib/python312.zip/profile.py:55\u001b[0m, in \u001b[0;36m_Utils.run\u001b[0;34m(self, statement, filename, sort)\u001b[0m\n\u001b[1;32m     53\u001b[0m prof \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprofiler()\n\u001b[1;32m     54\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m---> 55\u001b[0m     \u001b[43mprof\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mstatement\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m     56\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mSystemExit\u001b[39;00m:\n\u001b[1;32m     57\u001b[0m     \u001b[38;5;28;01mpass\u001b[39;00m\n",
            "File \u001b[0;32m/lib/python312.zip/cProfile.py:97\u001b[0m, in \u001b[0;36mProfile.run\u001b[0;34m(self, cmd)\u001b[0m\n\u001b[1;32m     95\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01m__main__\u001b[39;00m\n\u001b[1;32m     96\u001b[0m \u001b[38;5;28mdict\u001b[39m \u001b[38;5;241m=\u001b[39m __main__\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__dict__\u001b[39m\n\u001b[0;32m---> 97\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrunctx\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcmd\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mdict\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mdict\u001b[39;49m\u001b[43m)\u001b[49m\n",
            "File \u001b[0;32m/lib/python312.zip/cProfile.py:102\u001b[0m, in \u001b[0;36mProfile.runctx\u001b[0;34m(self, cmd, globals, locals)\u001b[0m\n\u001b[1;32m    100\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39menable()\n\u001b[1;32m    101\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 102\u001b[0m     \u001b[43mexec\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcmd\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mglobals\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mlocals\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[1;32m    103\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[1;32m    104\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdisable()\n",
            "File \u001b[0;32m<string>:1\u001b[0m\n",
            "File \u001b[0;32m<string>:1\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'true' is not defined"
          ],
          "output_type": "error"
        }
      ],
      "execution_count": 17
    },
    {
      "id": "715511d3-4a64-4da3-af32-faaf0dde7310",
      "cell_type": "code",
      "source": "import cProfile\n\ndef main():\n    # Call your main function here\n    pass  # Replace with actual function call\n\nif __name__ == \"__main__\":\n    cProfile.run(\"main()\", \"diff_sol.prof\")",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 16
    },
    {
      "id": "def41979-a259-41e4-926e-63ddddb1ac2d",
      "cell_type": "code",
      "source": "import cProfile\n\ncProfile.run(\"exec(open('diff_sol.py').read())\")",
      "metadata": {
        "trusted": true,
        "scrolled": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "         11 function calls (10 primitive calls) in 0.020 seconds\n\n   Ordered by: standard name\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)\n        1    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)\n        1    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)\n        1    0.000    0.000    0.000    0.000 <string>:1(<module>)\n        1    0.000    0.000    0.013    0.013 interactiveshell.py:315(_modified_open)\n        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}\n        1    0.013    0.013    0.013    0.013 {built-in method _io.open}\n      2/1    0.002    0.001    0.020    0.020 {built-in method builtins.exec}\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n        1    0.005    0.005    0.005    0.005 {method 'read' of '_io.TextIOWrapper' objects}\n\n\n"
        },
        {
          "ename": "<class 'NameError'>",
          "evalue": "name 'true' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "Cell \u001b[0;32mIn[12], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mcProfile\u001b[39;00m\n\u001b[0;32m----> 3\u001b[0m \u001b[43mcProfile\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mexec(open(\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mdiff_sol.py\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m).read())\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n",
            "File \u001b[0;32m/lib/python312.zip/cProfile.py:18\u001b[0m, in \u001b[0;36mrun\u001b[0;34m(statement, filename, sort)\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mrun\u001b[39m(statement, filename\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m, sort\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m1\u001b[39m):\n\u001b[0;32m---> 18\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43m_pyprofile\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_Utils\u001b[49m\u001b[43m(\u001b[49m\u001b[43mProfile\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mstatement\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mfilename\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43msort\u001b[49m\u001b[43m)\u001b[49m\n",
            "File \u001b[0;32m/lib/python312.zip/profile.py:55\u001b[0m, in \u001b[0;36m_Utils.run\u001b[0;34m(self, statement, filename, sort)\u001b[0m\n\u001b[1;32m     53\u001b[0m prof \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprofiler()\n\u001b[1;32m     54\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m---> 55\u001b[0m     \u001b[43mprof\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mstatement\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m     56\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mSystemExit\u001b[39;00m:\n\u001b[1;32m     57\u001b[0m     \u001b[38;5;28;01mpass\u001b[39;00m\n",
            "File \u001b[0;32m/lib/python312.zip/cProfile.py:97\u001b[0m, in \u001b[0;36mProfile.run\u001b[0;34m(self, cmd)\u001b[0m\n\u001b[1;32m     95\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01m__main__\u001b[39;00m\n\u001b[1;32m     96\u001b[0m \u001b[38;5;28mdict\u001b[39m \u001b[38;5;241m=\u001b[39m __main__\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__dict__\u001b[39m\n\u001b[0;32m---> 97\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrunctx\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcmd\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mdict\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mdict\u001b[39;49m\u001b[43m)\u001b[49m\n",
            "File \u001b[0;32m/lib/python312.zip/cProfile.py:102\u001b[0m, in \u001b[0;36mProfile.runctx\u001b[0;34m(self, cmd, globals, locals)\u001b[0m\n\u001b[1;32m    100\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39menable()\n\u001b[1;32m    101\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 102\u001b[0m     \u001b[43mexec\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcmd\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mglobals\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mlocals\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[1;32m    103\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[1;32m    104\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdisable()\n",
            "File \u001b[0;32m<string>:1\u001b[0m\n",
            "File \u001b[0;32m<string>:1\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'true' is not defined"
          ],
          "output_type": "error"
        }
      ],
      "execution_count": 12
    },
    {
      "id": "28b78fe8-9558-4273-95b8-df5f1294318b",
      "cell_type": "code",
      "source": "import cProfile\nimport pstats\n\n# Define a function to execute the script\ndef run_script():\n    with open(\"diff_sol.py\") as f:\n        exec(f.read(), globals())\n\n# Profile the script\nprofile_file = \"diff_sol.prof\"\ncProfile.run(\"run_script()\", profile_file)\n\n# Analyze and print results\nstats = pstats.Stats(profile_file)\nstats.strip_dirs().sort_stats(\"cumulative\").print_stats(10)  # Show top 10 slowest functions\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "ename": "<class 'NameError'>",
          "evalue": "name 'true' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "Cell \u001b[0;32mIn[15], line 11\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[38;5;66;03m# Profile the script\u001b[39;00m\n\u001b[1;32m     10\u001b[0m profile_file \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdiff_sol.prof\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m---> 11\u001b[0m \u001b[43mcProfile\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mrun_script()\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mprofile_file\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m     13\u001b[0m \u001b[38;5;66;03m# Analyze and print results\u001b[39;00m\n\u001b[1;32m     14\u001b[0m stats \u001b[38;5;241m=\u001b[39m pstats\u001b[38;5;241m.\u001b[39mStats(profile_file)\n",
            "File \u001b[0;32m/lib/python312.zip/cProfile.py:18\u001b[0m, in \u001b[0;36mrun\u001b[0;34m(statement, filename, sort)\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mrun\u001b[39m(statement, filename\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m, sort\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m1\u001b[39m):\n\u001b[0;32m---> 18\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43m_pyprofile\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_Utils\u001b[49m\u001b[43m(\u001b[49m\u001b[43mProfile\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mstatement\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mfilename\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43msort\u001b[49m\u001b[43m)\u001b[49m\n",
            "File \u001b[0;32m/lib/python312.zip/profile.py:55\u001b[0m, in \u001b[0;36m_Utils.run\u001b[0;34m(self, statement, filename, sort)\u001b[0m\n\u001b[1;32m     53\u001b[0m prof \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprofiler()\n\u001b[1;32m     54\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m---> 55\u001b[0m     \u001b[43mprof\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mstatement\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m     56\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mSystemExit\u001b[39;00m:\n\u001b[1;32m     57\u001b[0m     \u001b[38;5;28;01mpass\u001b[39;00m\n",
            "File \u001b[0;32m/lib/python312.zip/cProfile.py:97\u001b[0m, in \u001b[0;36mProfile.run\u001b[0;34m(self, cmd)\u001b[0m\n\u001b[1;32m     95\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01m__main__\u001b[39;00m\n\u001b[1;32m     96\u001b[0m \u001b[38;5;28mdict\u001b[39m \u001b[38;5;241m=\u001b[39m __main__\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__dict__\u001b[39m\n\u001b[0;32m---> 97\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrunctx\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcmd\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mdict\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mdict\u001b[39;49m\u001b[43m)\u001b[49m\n",
            "File \u001b[0;32m/lib/python312.zip/cProfile.py:102\u001b[0m, in \u001b[0;36mProfile.runctx\u001b[0;34m(self, cmd, globals, locals)\u001b[0m\n\u001b[1;32m    100\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39menable()\n\u001b[1;32m    101\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 102\u001b[0m     \u001b[43mexec\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcmd\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mglobals\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mlocals\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[1;32m    103\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[1;32m    104\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdisable()\n",
            "File \u001b[0;32m<string>:1\u001b[0m\n",
            "Cell \u001b[0;32mIn[15], line 7\u001b[0m, in \u001b[0;36mrun_script\u001b[0;34m()\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mrun_script\u001b[39m():\n\u001b[1;32m      6\u001b[0m     \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdiff_sol.py\u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[0;32m----> 7\u001b[0m         \u001b[43mexec\u001b[49m\u001b[43m(\u001b[49m\u001b[43mf\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mread\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mglobals\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n",
            "File \u001b[0;32m<string>:1\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'true' is not defined"
          ],
          "output_type": "error"
        }
      ],
      "execution_count": 15
    },
    {
      "id": "359848d2-dd08-4738-8333-933a1a6eb0fc",
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