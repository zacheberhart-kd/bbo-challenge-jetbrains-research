# JetBrains Research's Solution for Black-Box Optimization Challenge

*Forked version of JetBrains' Space Partitioning Optimizer that includes a local installation and a run file.*

From the original authors:

This is the code for our solution to the [NeurIPS 2020 Black-Box Optimization Challenge](https://bbochallenge.com/).

Our solution is described in the "Solving Black-Box Optimization Challenge via Learning Search Space Partition for Local Bayesian Optimization" paper.

## Results

Our approach scored 92.509 in the finals and ranked 3rd overall!

## Paper & License

The paper is available at: https://arxiv.org/pdf/2012.10335.pdf.

Our implementation is released under [Apache License 2.0](./LICENSE) license except for the code derived from TuRBO.

## Run locally

Installation:

```
python setup.py develop
```

## Setting the Search Space

To optimize an objective, you'll need to pass a config dict which uses AutoML's `ConfigSpace` API.

Example Configuration:

```
config = {
    'x': {'type': 'int', 'space': 'linear', 'range': (0, 10)},
    'y': {'type': 'int', 'space': 'linear', 'range': (0, 10)},
    'z': {'type': 'real', 'space': 'bilog', 'range': (-1, 1)},
    'a': {'type': 'real', 'space': 'logit', 'range': (1e-9, 1e-6)},
    'b': {'type': 'bool'},
    'c': {'type': 'cat', 'values': ['aa', 'bb', 'cc']},
}
```

## Run Locally

Use the example file:

```
python run.py
```

Use custom objective/config:

```
import jetbrains_bbo.optimizer as jo

def objective(a, b):
    return a + b

optimizer = jo.SpacePartitioningOptimizer(config)

for _ in range(N_OPTIM_ITER):
    suggestions = optimizer.suggest(n_suggestions=N_SUGGESTIONS)
    optimizer.observe(suggestions, [objective(**suggestion) for suggestion in suggestions])

```
