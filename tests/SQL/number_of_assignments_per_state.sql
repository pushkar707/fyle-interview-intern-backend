-- Write query to get number of assignments for each state

select state,COUNT(state) from assignments GROUP BY state;
