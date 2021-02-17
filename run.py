from copy import deepcopy
from typing import Union, Dict

import jetbrains_bbo.optimizer as jo

# -------------------------------- #
# Example run for simple function. #
# -------------------------------- #

def objective(x, z, c, b):
    "squirrel can only minimize so negative is needed for a maximation objective"
    return -((((x ** 2) + z) * {'1': 1, '2': 2, '3': 3}[c]) * b)

def parse_results(optimizer: so.SwitchingOptimizer, init_score: Union[int, float]) -> Dict:
    
    best_score = float(init_score)
    
    for i, results in enumerate(optimizer.results):
        results = deepcopy(results)
        _, score = results
        if score < best_score:
            results.append(i)
            best_suggestion = results
            best_score = score
            
    return {k: v for k, v in zip(['params', 'score', 'iteration'], best_suggestion)}


if __name__ == '__main__':
    
    N_OPTIM_ITER = 100 # the number of optimization iterations
    N_SUGGESTIONS = 8  # number of parallel suggestions in one optimization iteration
    
    api_config = {
        'x': {'type': 'int', 'space': 'linear', 'range': (0, 10)},
        'z': {'type': 'int', 'space': 'linear', 'range': (0, 10)},
        'c': {'type': 'cat', 'values': ['1', '2', '3']},
        'b': {'type': 'bool'},
    }

    opt =  jo.SpacePartitioningOptimizer(api_config)

    for _ in range(N_OPTIM_ITER):
        suggestions = opt.suggest(n_suggestions=N_SUGGESTIONS)
        opt.observe(suggestions, [objective(**suggestion) for suggestion in suggestions])
    
    print(f'\n\n\n===== RESULTS =====\n\nBest Params:\n\n{parse_results(opt, init_score=0)}')
