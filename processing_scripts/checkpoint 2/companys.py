import pandas as pd

# Datos de estructura organizacional de empresa tech
org_structure = pd.DataFrame({
    'labels': ['Company',
               'Engineering', 'Product', 'Sales', 'Operations',
               'Backend', 'Frontend', 'Mobile', 'DevOps',
               'Design', 'Product Management', 'Analytics',
               'Enterprise', 'SMB', 'Partnerships',
               'HR', 'Finance', 'Legal', 'IT',
               'Backend-Team1', 'Backend-Team2', 'Frontend-Team1', 'Frontend-Team2',
               'Mobile-iOS', 'Mobile-Android', 'DevOps-Cloud', 'DevOps-Security',
               'UI/UX', 'Research', 'PM-Core', 'PM-Growth',
               'Data-Science', 'BI'],
    'parents': ['',
                'Company', 'Company', 'Company', 'Company',
                'Engineering', 'Engineering', 'Engineering', 'Engineering',
                'Product', 'Product', 'Product',
                'Sales', 'Sales', 'Sales',
                'Operations', 'Operations', 'Operations', 'Operations',
                'Backend', 'Backend', 'Frontend', 'Frontend',
                'Mobile', 'Mobile', 'DevOps', 'DevOps',
                'Design', 'Design', 'Product Management', 'Product Management',
                'Analytics', 'Analytics'],
    'values': [500,
               180, 80, 120, 120,
               60, 50, 40, 30,
               30, 25, 25,
               50, 40, 30,
               40, 35, 25, 20,
               30, 30, 25, 25,
               20, 20, 15, 15,
               15, 15, 12, 13,
               13, 12]
})

# Guardar en CSV
org_structure.to_csv("empresas_tech.csv", index=False)