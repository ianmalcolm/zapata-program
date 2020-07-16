import json

def create_dataset():
    mu = [0.7313, 0.9893, 0.2725, 0.8750, 0.7667, 0.3622]
    sigma = [
             [0.7312, -0.6233, 0.4689, -0.5452, -0.0082, -0.3809],
             [-0.6233, 2.4732, -0.7538, 2.4659, -0.0733, 0.8945],
             [0.4689, -0.7538, 1.1543, -1.4095, 0.0007, -0.4301],
             [-0.5452, 2.4659, -1.4095, 3.5067, 0.2012, 1.0922],
             [-0.0082, -0.0733, 0.0007, 0.2012, 0.6231, 0.1509],
             [-0.3809, 0.8945, -0.4301, 1.0922, 0.1509, 0.8992],
            ]
    
    return mu, sigma

def create_ising(mu: 'expected returns', sigma: 'covariances', q: 'risk factor', B: 'budget', L: 'lagrange multiplier') -> 'ising model':
    
    n = len(mu)

    output = QubitOperator()

    for i in range(n):
        output += QubitOperator(f'X{i}', mu[i])

    for i in range(n):
        for j in range(n):
            output += QubitOperator(f'X{i} X{j}', -sigma[i][j]*q)
            
    for i in range(n):
        for j in range(n):
            output += QubitOperator(f'X{i} X{j}', -L)

    for i in range(n):
        output += QubitOperator(f'X{i}', 2*L*B)
        
    return output