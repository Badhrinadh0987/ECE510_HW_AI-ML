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
      "source": "import numpy as np\nfrom scipy.integrate import solve_ivp\nimport cProfile\n\ndef ode_solver():\n    def dydt(t, y): return -2 * y\n    sol = solve_ivp(dydt, [0, 5], [1], method='RK45')\n    print(\"ODE Solution:\", sol.y)\n\ncProfile.runctx(\"ode_solver()\", globals(), locals(), sort='cumulative')",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "ODE Solution: [[1.00000000e+00 8.59330265e-01 3.39954077e-01 1.41634832e-01\n  5.88020563e-02 2.44004625e-02 1.01080684e-02 4.17064112e-03\n  1.70480502e-03 6.82283272e-04 2.61139397e-04 9.18493878e-05\n  4.57237894e-05]]\n         1082 function calls (1068 primitive calls) in 0.016 seconds\n\n   Ordered by: cumulative time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}\n        1    0.000    0.000    0.016    0.016 <ipython-input-1-580d0032e5c1>:5(ode_solver)\n        1    0.000    0.000    0.016    0.016 <string>:1(<module>)\n        1    0.000    0.000    0.012    0.012 ivp.py:159(solve_ivp)\n       12    0.000    0.000    0.008    0.001 base.py:175(step)\n       12    0.001    0.000    0.008    0.001 rk.py:111(_step_impl)\n       12    0.003    0.000    0.005    0.000 rk.py:14(rk_step)\n        1    0.000    0.000    0.004    0.004 {built-in method builtins.print}\n        1    0.000    0.000    0.004    0.004 rk.py:85(__init__)\n        1    0.000    0.000    0.003    0.003 arrayprint.py:1652(_array_str_implementation)\n        1    0.000    0.000    0.003    0.003 arrayprint.py:582(array2string)\n        1    0.000    0.000    0.003    0.003 base.py:131(__init__)\n        1    0.000    0.000    0.003    0.003 base.py:4(check_arguments)\n        5    0.002    0.000    0.002    0.000 {method 'reduce' of 'numpy.ufunc' objects}\n        1    0.000    0.000    0.002    0.002 arrayprint.py:544(_array2string)\n        1    0.000    0.000    0.002    0.002 arrayprint.py:527(wrapper)\n        1    0.000    0.000    0.002    0.002 {method 'all' of 'numpy.ndarray' objects}\n        1    0.000    0.000    0.002    0.002 _methods.py:67(_all)\n        1    0.000    0.000    0.002    0.002 arrayprint.py:473(_get_format_function)\n        1    0.000    0.000    0.002    0.002 arrayprint.py:939(__init__)\n        1    0.000    0.000    0.002    0.002 arrayprint.py:432(<lambda>)\n        1    0.001    0.001    0.002    0.002 arrayprint.py:966(fillFormat)\n       12    0.000    0.000    0.002    0.000 rk.py:108(_estimate_error_norm)\n       74    0.000    0.000    0.002    0.000 base.py:152(fun)\n       74    0.000    0.000    0.001    0.000 base.py:22(fun_wrapped)\n        4    0.001    0.000    0.001    0.000 display.py:19(write)\n       15    0.000    0.000    0.001    0.000 _linalg.py:2566(norm)\n       15    0.000    0.000    0.001    0.000 common.py:63(norm)\n       74    0.001    0.000    0.001    0.000 <ipython-input-1-580d0032e5c1>:6(dydt)\n       12    0.001    0.000    0.001    0.000 rk.py:105(_estimate_error)\n        1    0.000    0.000    0.001    0.001 arrayprint.py:806(_formatArray)\n     15/1    0.000    0.000    0.001    0.001 arrayprint.py:815(recurser)\n        1    0.000    0.000    0.001    0.001 common.py:68(select_initial_step)\n       37    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}\n        1    0.000    0.000    0.000    0.000 common.py:44(validate_tol)\n       92    0.000    0.000    0.000    0.000 {built-in method numpy.asarray}\n        1    0.000    0.000    0.000    0.000 shape_base.py:219(vstack)\n        1    0.000    0.000    0.000    0.000 shape_base.py:81(atleast_2d)\n        2    0.000    0.000    0.000    0.000 fromnumeric.py:89(_wrapreduction_any_all)\n        2    0.000    0.000    0.000    0.000 fromnumeric.py:2400(any)\n       13    0.000    0.000    0.000    0.000 arrayprint.py:1052(__call__)\n       84    0.000    0.000    0.000    0.000 multiarray.py:750(dot)\n       37    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}\n        2    0.000    0.000    0.000    0.000 fromnumeric.py:69(_wrapreduction)\n        5    0.000    0.000    0.000    0.000 {built-in method builtins.max}\n       15    0.000    0.000    0.000    0.000 {method 'ravel' of 'numpy.ndarray' objects}\n       26    0.000    0.000    0.000    0.000 {built-in method numpy._core._multiarray_umath.dragon4_scientific}\n       14    0.000    0.000    0.000    0.000 arrayprint.py:995(<genexpr>)\n       14    0.000    0.000    0.000    0.000 arrayprint.py:992(<genexpr>)\n        1    0.000    0.000    0.000    0.000 fromnumeric.py:2925(min)\n       14    0.000    0.000    0.000    0.000 arrayprint.py:996(<genexpr>)\n       13    0.000    0.000    0.000    0.000 {method 'splitlines' of 'str' objects}\n        1    0.000    0.000    0.000    0.000 {method 'astype' of 'numpy.ndarray' objects}\n       15    0.000    0.000    0.000    0.000 {method 'dot' of 'numpy.ndarray' objects}\n        1    0.000    0.000    0.000    0.000 numerictypes.py:470(issubdtype)\n        1    0.000    0.000    0.000    0.000 fromnumeric.py:2781(max)\n       13    0.000    0.000    0.000    0.000 arrayprint.py:779(_extendLine_pretty)\n        1    0.000    0.000    0.000    0.000 arrayprint.py:423(_get_formatdict)\n        1    0.000    0.000    0.000    0.000 _ufunc_config.py:410(__enter__)\n       14    0.000    0.000    0.000    0.000 arrayprint.py:997(<genexpr>)\n       14    0.000    0.000    0.000    0.000 arrayprint.py:1009(<genexpr>)\n        1    0.000    0.000    0.000    0.000 _util.py:864(__getattr__)\n       14    0.000    0.000    0.000    0.000 {built-in method builtins.min}\n        2    0.000    0.000    0.000    0.000 {method 'any' of 'numpy.generic' objects}\n       13    0.000    0.000    0.000    0.000 {built-in method numpy.asanyarray}\n        2    0.000    0.000    0.000    0.000 _methods.py:58(_any)\n        1    0.000    0.000    0.000    0.000 arrayprint.py:64(_make_options_dict)\n        1    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}\n        5    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}\n        1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}\n        1    0.000    0.000    0.000    0.000 {method 'copy' of 'dict' objects}\n        1    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}\n        1    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}\n       13    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}\n       13    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}\n        5    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}\n        1    0.000    0.000    0.000    0.000 {built-in method builtins.abs}\n        2    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}\n        1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}\n        1    0.000    0.000    0.000    0.000 {built-in method builtins.id}\n        2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}\n      130    0.000    0.000    0.000    0.000 {built-in method builtins.len}\n        1    0.000    0.000    0.000    0.000 {built-in method builtins.locals}\n        1    0.000    0.000    0.000    0.000 {method 'set' of '_contextvars.ContextVar' objects}\n        1    0.000    0.000    0.000    0.000 {method 'reset' of '_contextvars.ContextVar' objects}\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n        1    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}\n        1    0.000    0.000    0.000    0.000 multiarray.py:161(concatenate)\n        1    0.000    0.000    0.000    0.000 {built-in method numpy.array}\n        1    0.000    0.000    0.000    0.000 {built-in method numpy.empty}\n        1    0.000    0.000    0.000    0.000 {built-in method numpy._core._multiarray_umath._make_extobj}\n        1    0.000    0.000    0.000    0.000 arrayprint.py:930(_none_or_positive_arg)\n       13    0.000    0.000    0.000    0.000 arrayprint.py:765(_extendLine)\n        1    0.000    0.000    0.000    0.000 shape_base.py:207(_arrays_for_stack_dispatcher)\n        1    0.000    0.000    0.000    0.000 fromnumeric.py:2920(_min_dispatcher)\n        1    0.000    0.000    0.000    0.000 fromnumeric.py:2776(_max_dispatcher)\n        2    0.000    0.000    0.000    0.000 numerictypes.py:288(issubclass_)\n        2    0.000    0.000    0.000    0.000 fromnumeric.py:2395(_any_dispatcher)\n        1    0.000    0.000    0.000    0.000 _ufunc_config.py:426(__exit__)\n        1    0.000    0.000    0.000    0.000 shape_base.py:215(_vhstack_dispatcher)\n        1    0.000    0.000    0.000    0.000 shape_base.py:77(_atleast_2d_dispatcher)\n       15    0.000    0.000    0.000    0.000 _linalg.py:128(isComplexType)\n       14    0.000    0.000    0.000    0.000 arrayprint.py:1000(<genexpr>)\n        1    0.000    0.000    0.000    0.000 _ufunc_config.py:400(__init__)\n       15    0.000    0.000    0.000    0.000 _linalg.py:2562(_norm_dispatcher)\n        1    0.000    0.000    0.000    0.000 common.py:26(warn_extraneous)\n        1    0.000    0.000    0.000    0.000 common.py:19(validate_max_step)\n\n\n"
        }
      ],
      "execution_count": 1
    },
    {
      "id": "359848d2-dd08-4738-8333-933a1a6eb0fc",
      "cell_type": "code",
      "source": "import dis\nimport ast\nimport inspect\n\ndef ode_solver():\n    def dydt(t, y): return -2 * y\n    from scipy.integrate import solve_ivp\n    sol = solve_ivp(dydt, [0, 5], [1], method='RK45')\n    print(\"ODE Solution:\", sol.y)\n\ndef analyze_ode_solver():\n    source = inspect.getsource(ode_solver)\n    tree = ast.parse(source)\n\n    print(\"📌 AST Structure:\")\n    print(ast.dump(tree, indent=4))\n\n    print(\"\\n📌 Bytecode Instructions:\")\n    dis.dis(ode_solver)\n\n    print(\"\\n🧠 Potential Parallelism:\")\n    print(\"- Not much parallelism here; ODE integration is sequential (RK45).\")\n    print(\"- You could solve multiple independent ODEs in parallel, if applicable.\")\n\nanalyze_ode_solver()\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "📌 AST Structure:\nModule(\n    body=[\n        FunctionDef(\n            name='ode_solver',\n            args=arguments(\n                posonlyargs=[],\n                args=[],\n                kwonlyargs=[],\n                kw_defaults=[],\n                defaults=[]),\n            body=[\n                FunctionDef(\n                    name='dydt',\n                    args=arguments(\n                        posonlyargs=[],\n                        args=[\n                            arg(arg='t'),\n                            arg(arg='y')],\n                        kwonlyargs=[],\n                        kw_defaults=[],\n                        defaults=[]),\n                    body=[\n                        Return(\n                            value=BinOp(\n                                left=UnaryOp(\n                                    op=USub(),\n                                    operand=Constant(value=2)),\n                                op=Mult(),\n                                right=Name(id='y', ctx=Load())))],\n                    decorator_list=[],\n                    type_params=[]),\n                ImportFrom(\n                    module='scipy.integrate',\n                    names=[\n                        alias(name='solve_ivp')],\n                    level=0),\n                Assign(\n                    targets=[\n                        Name(id='sol', ctx=Store())],\n                    value=Call(\n                        func=Name(id='solve_ivp', ctx=Load()),\n                        args=[\n                            Name(id='dydt', ctx=Load()),\n                            List(\n                                elts=[\n                                    Constant(value=0),\n                                    Constant(value=5)],\n                                ctx=Load()),\n                            List(\n                                elts=[\n                                    Constant(value=1)],\n                                ctx=Load())],\n                        keywords=[\n                            keyword(\n                                arg='method',\n                                value=Constant(value='RK45'))])),\n                Expr(\n                    value=Call(\n                        func=Name(id='print', ctx=Load()),\n                        args=[\n                            Constant(value='ODE Solution:'),\n                            Attribute(\n                                value=Name(id='sol', ctx=Load()),\n                                attr='y',\n                                ctx=Load())],\n                        keywords=[]))],\n            decorator_list=[],\n            type_params=[])],\n    type_ignores=[])\n\n📌 Bytecode Instructions:\n  5           0 RESUME                   0\n\n  6           2 LOAD_CONST               1 (<code object dydt at 0x5616020, file \"<ipython-input-2-e1fe9366127b>\", line 6>)\n              4 MAKE_FUNCTION            0\n              6 STORE_FAST               0 (dydt)\n\n  7           8 LOAD_CONST               2 (0)\n             10 LOAD_CONST               3 (('solve_ivp',))\n             12 IMPORT_NAME              0 (scipy.integrate)\n             14 IMPORT_FROM              1 (solve_ivp)\n             16 STORE_FAST               1 (solve_ivp)\n             18 POP_TOP\n\n  8          20 PUSH_NULL\n             22 LOAD_FAST                1 (solve_ivp)\n             24 LOAD_FAST                0 (dydt)\n             26 LOAD_CONST               2 (0)\n             28 LOAD_CONST               4 (5)\n             30 BUILD_LIST               2\n             32 LOAD_CONST               5 (1)\n             34 BUILD_LIST               1\n             36 LOAD_CONST               6 ('RK45')\n             38 KW_NAMES                 7 (('method',))\n             40 CALL                     4\n             48 STORE_FAST               2 (sol)\n\n  9          50 LOAD_GLOBAL              5 (NULL + print)\n             60 LOAD_CONST               8 ('ODE Solution:')\n             62 LOAD_FAST                2 (sol)\n             64 LOAD_ATTR                6 (y)\n             84 CALL                     2\n             92 POP_TOP\n             94 RETURN_CONST             0 (None)\n\nDisassembly of <code object dydt at 0x5616020, file \"<ipython-input-2-e1fe9366127b>\", line 6>:\n  6           0 RESUME                   0\n              2 LOAD_CONST               1 (-2)\n              4 LOAD_FAST                1 (y)\n              6 BINARY_OP                5 (*)\n             10 RETURN_VALUE\n\n🧠 Potential Parallelism:\n- Not much parallelism here; ODE integration is sequential (RK45).\n- You could solve multiple independent ODEs in parallel, if applicable.\n"
        }
      ],
      "execution_count": 2
    },
    {
      "id": "f874f8da-b2eb-4c51-abec-17d3221907bf",
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