import pandas as pd

# Datos de presupuesto por departamento y proyectos
budget_data = pd.DataFrame({
    'department': ['Engineering', 'Engineering', 'Engineering', 'Engineering',
                   'Marketing', 'Marketing', 'Marketing',
                   'Sales', 'Sales', 'Sales',
                   'Research', 'Research', 'Research'],
    'project': ['Cloud Infrastructure', 'Product Development', 'Security', 'Data Pipeline',
                'Digital Campaigns', 'Content Creation', 'Events',
                'CRM System', 'Sales Training', 'Partnerships',
                'AI Research', 'Market Analysis', 'User Studies'],
    'budget': [2500, 3500, 1800, 2200,
                1500, 800, 1200,
                1000, 600, 900,
                2000, 1200, 800]
})

# Guardar en CSV
budget_data.to_csv("budget_data.csv", index=False)