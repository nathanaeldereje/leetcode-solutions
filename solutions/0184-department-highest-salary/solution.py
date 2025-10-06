import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId', right_on='id')
    df=df.rename(columns={'name_x': 'Employee', 'name_y': 'Department','id_x':'id'}).drop(columns=['id_y','departmentId'])
    max_salary = df.groupby('Department')['salary'].max().reset_index()

# Step 2: Merge to get employee(s) who have that salary
    result = df.merge(max_salary, on=['Department', 'salary'])[['Department', 'Employee', 'salary']]


    return result
