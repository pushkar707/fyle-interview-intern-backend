-- Write query to find the number of grade A's given by the teacher who has graded the most assignments

SELECT COUNT(grade)
from assignments
WHERE grade="A" AND teacher_id = (SELECT teacher_id
FROM assignments
WHERE state = 'GRADED'
GROUP BY teacher_id
ORDER BY count(grade) DESC
LIMIT 1);