# Reproduction
Reproduction of various experiments can be conducted by first installing the requirements via (provided by author)
```
conda create -n "fedxgb" python=3.9 
conda activate fedxgb
pip install -r ./requirements.txt
```
Then going to the branch within this repository which applies to the experiment you are interested in re-running, and finally running `main.py`.

Experiments are listed below:
Fig 2
reproduce all base: `eval_split_methods_base` (vary t, vary e, vary d)

reproduce low eps budget: `eval_split_methods_low_eps` (vary t)

reproduce linear axis: `eval_split_methods_vary_t_axis` (vary t)

reproduce low eps budge + linear axis: `eval_split_methods_combined` (vary t)


Fig 3

reproduce all base: `eval_split_candidate_base` (vary s, vary t, vary q)

reproduce low epsilon: `eval_split_candidate_vary_t_low_eps` (vary t)

reproduce low epsilon: `eval_split_candidate_vary_q_low_eps` (vary q)


Fig 4

reproduce batch updates: `eval_batch_budget_base`


Fig 5

reproduce base: `compare_methods_c1`

reproduce low eps (0.1): `compare_methods_c1_low_eps`

reproduce med eps (0.5): `compare_methods_c1_med_eps`


Plot all tables

Instead of running `main.py`, run `paper_plotter.py` on branch `plot_tables`

# federated-boosted-dp-trees
Code for the reproduction challenge of the CCS'22 paper "Federated Boosted Decision Trees with Differential Privacy" 

Original work conducted by Samuel Maddock et al: https://github.com/Samuel-Maddock/federated-boosted-dp-trees
