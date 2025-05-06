# Marimo-Binary-Ninja-Mermaid-Graphs
Marimo Binary Ninja Mermaid Graphs

Marimo notebook for Binary Ninja Commercial to create headless Mermaid dominator graphs.

## Clone the repo
git clone https://github.com/meerkatone/Marimo-Binary-Ninja-Mermaid-Graphs.git

## Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

## Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

## Setup venv and Marimo
uv venv venv_marimo --python 3.12

source /venv_marimo/headless/bin/activate

cd Binary-Diffing-and-Marimo

uv pip install marimo

## Launch the notebook
marimo edit ./binary_ninja_mermaid.py

The notebook will ask you to install the required dependencies via uv.

## References
- Binary Ninja Python API Reference: https://api.binary.ninja/
- Dominator (graph theory): https://en.wikipedia.org/wiki/Dominator_(graph_theory)
- Compiling Techniques Lecture 14: Building SSA Form: https://opencourse.inf.ed.ac.uk/sites/default/files/2024-02/ct_lecture_14_-_building_ssa_form_0.pdf
- Static Single Assignment 15-411 Compiler Design: https://www.cs.cmu.edu/~fp/courses/15411-f08/lectures/09-ssa.pdf
- GCC Compiler Optimization Course: https://www.youtube.com/watch?v=c6csK4Z_U98&list=PL2saaWTUEfabOcP1xKb64KHNn9vKKPfef
