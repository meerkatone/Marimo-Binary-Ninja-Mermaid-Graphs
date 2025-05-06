import marimo

__generated_with = "0.13.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from typing import Dict
    import binaryninja
    return binaryninja, mo


@app.cell
def _(mo):
    mo.md(r"""<h2>post_dominance_frontier</h2>""")
    return


@app.cell(hide_code=True)
def _(binaryninja, mo):
    def _():
        bv = binaryninja.load(r"./Tenda/BNDB/trivision_webs.bndb")
        function_address = 0xB7E8
        func = bv.get_function_at(function_address)
        post_dominance_frontier = "graph TD;\n"
        if func is not None:
            for bb in func.basic_blocks:
                post_dominance_frontier += f"BB{hex(bb.start)}(({hex(bb.start)}))\n"
                for frontier in bb.post_dominance_frontier:
                    post_dominance_frontier += f"BB{hex(bb.start)} --> BB{hex(frontier.start)}\n"
        else:
            post_dominance_frontier += f'NoteNoFunction["No function found at address {hex(function_address)}"]\n'
        return mo.mermaid(post_dominance_frontier)


    _()
    return


@app.cell
def _(mo):
    mo.md(r"""<h2>post_dominator_tree_children</h2>""")
    return


@app.cell
def _(binaryninja, mo):
    def _():
        bv = binaryninja.load(r"./Tenda/BNDB/trivision_webs.bndb")
        function_address = 0xB7E8
        func = bv.get_function_at(function_address)
        post_dominator_tree_children = "graph TD;\n"
        if func is not None:
            for bb in func.basic_blocks:
                post_dominator_tree_children += f"BB{hex(bb.start)}(({hex(bb.start)}))\n"
                for frontier in bb.post_dominator_tree_children:
                    post_dominator_tree_children += f"BB{hex(bb.start)} --> BB{hex(frontier.start)}\n"
        else:
            post_dominator_tree_children += f'NoteNoFunction["No function found at address {hex(function_address)}"]\n'
        return mo.mermaid(post_dominator_tree_children)


    _()
    return


@app.cell
def _(mo):
    mo.md(r"""<h2>post_dominators</h2>""")
    return


@app.cell
def _(binaryninja, mo):
    def _():
        bv = binaryninja.load(r"./Tenda/BNDB/trivision_webs.bndb")
        function_address = 0xB7E8
        func = bv.get_function_at(function_address)
        post_dominators = "graph TD;\n"
        if func is not None:
            for bb in func.basic_blocks:
                post_dominators += f"BB{hex(bb.start)}(({hex(bb.start)}))\n"
                for frontier in bb.post_dominators:
                    post_dominators += f"BB{hex(bb.start)} --> BB{hex(frontier.start)}\n"
        else:
            post_dominators += f'NoteNoFunction["No function found at address {hex(function_address)}"]\n'
        return mo.mermaid(post_dominators)


    _()
    return


@app.cell
def _(mo):
    mo.md(r"""<h2>dominators</h2>""")
    return


@app.cell
def _(binaryninja, mo):
    def _():
        bv = binaryninja.load(r"./Tenda/BNDB/trivision_webs.bndb")
        function_address = 0xB7E8
        func = bv.get_function_at(function_address)
        dominators = "graph TD;\n"
        if func is not None:
            for bb in func.basic_blocks:
                dominators += f"BB{hex(bb.start)}(({hex(bb.start)}))\n"
                for frontier in bb.dominators:
                    dominators += f"BB{hex(bb.start)} --> BB{hex(frontier.start)}\n"
        else:
            dominators += f'NoteNoFunction["No function found at address {hex(function_address)}"]\n'
        return mo.mermaid(dominators)


    _()
    return


@app.cell
def _(mo):
    mo.md(r"""<h2>dominance_frontier</h2>""")
    return


@app.cell
def _(binaryninja, mo):
    def _():
        bv = binaryninja.load(r"./Tenda/BNDB/trivision_webs.bndb")
        function_address = 0xB7E8
        func = bv.get_function_at(function_address)
        dominance_frontier = "graph TD;\n"
        if func is not None:
            for bb in func.basic_blocks:
                dominance_frontier += f"BB{hex(bb.start)}(({hex(bb.start)}))\n"
                for frontier in bb.dominance_frontier:
                    dominance_frontier += f"BB{hex(bb.start)} --> BB{hex(frontier.start)}\n"
        else:
            dominance_frontier += f'NoteNoFunction["No function found at address {hex(function_address)}"]\n'
        return mo.mermaid(dominance_frontier)


    _()
    return


@app.cell
def _(mo):
    mo.md(r"""<h2>dominator_tree_children</h2>""")
    return


@app.cell
def _(binaryninja, mo):
    def _():
        bv = binaryninja.load(r"./Tenda/BNDB/trivision_webs.bndb")
        function_address = 0xB7E8
        func = bv.get_function_at(function_address)
        dominator_tree_children = "graph TD;\n"
        if func is not None:
            for bb in func.basic_blocks:
                dominator_tree_children += f"BB{hex(bb.start)}(({hex(bb.start)}))\n"
                for frontier in bb.dominator_tree_children:
                    dominator_tree_children += f"BB{hex(bb.start)} --> BB{hex(frontier.start)}\n"
        else:
            dominator_tree_children += f'NoteNoFunction["No function found at address {hex(function_address)}"]\n'
        return mo.mermaid(dominator_tree_children)


    _()
    return


@app.cell
def _(mo):
    mo.md(r"""<h2>strict_dominators</h2>""")
    return


@app.cell
def _(binaryninja, mo):
    def _():
        bv = binaryninja.load(r"./Tenda/BNDB/trivision_webs.bndb")
        function_address = 0xB7E8
        func = bv.get_function_at(function_address)
        strict_dominators = "graph TD;\n"
        if func is not None:
            for bb in func.basic_blocks:
                strict_dominators += f"BB{hex(bb.start)}(({hex(bb.start)}))\n"
                for frontier in bb.strict_dominators:
                    strict_dominators += f"BB{hex(bb.start)} --> BB{hex(frontier.start)}\n"
        else:
            strict_dominators += f'NoteNoFunction["No function found at address {hex(function_address)}"]\n'
        return mo.mermaid(strict_dominators)


    _()
    return


if __name__ == "__main__":
    app.run()
