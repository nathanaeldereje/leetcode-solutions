# Write your MySQL query statement below
with Managers as(
    select e.*, m.salary as managerSalary
    from Employee e
    Left Join Employee m on e.managerId=m.id
)
select name as Employee from Managers
where salary>managerSalary
