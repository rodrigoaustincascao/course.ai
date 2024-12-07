import pandas as pd
import numpy as np

# Configurações básicas
np.random.seed(42)  # Para reprodutibilidade
num_rows = 100000

# Gerar dados simulados
data = {
    'ID': np.arange(1, num_rows + 1),
    'Sexo': np.random.choice(['M', 'F'], size=num_rows),
    'Hand': np.random.choice(['Right', 'Left'], size=num_rows),
    'Age': np.random.randint(18, 90, size=num_rows),
    'Edu': np.random.choice(['None', 'Primary', 'Secondary', 'Tertiary'], size=num_rows),
    'SES': np.random.choice(['Low', 'Middle', 'High'], size=num_rows),
    'MMSE': np.random.uniform(0, 30, size=num_rows),
    'CDR': np.random.choice([0, 0.5, 1, 2, 3], size=num_rows),
    'eTIV': np.random.uniform(1200, 1600, size=num_rows),
    'nWBV': np.random.uniform(0.6, 0.9, size=num_rows),
    'ASF': np.random.uniform(0.5, 1.5, size=num_rows),
    'Delay': np.random.randint(0, 36, size=num_rows)  # Atraso em meses
}

# Criar DataFrame
df = pd.DataFrame(data)

# Salvar em um arquivo CSV
df.to_csv('dados_pacientes.csv', index=False)

print("Arquivo CSV com 100 mil linhas gerado com sucesso!")