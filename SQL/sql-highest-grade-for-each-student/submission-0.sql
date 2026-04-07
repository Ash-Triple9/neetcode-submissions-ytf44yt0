-- Write your query below

-- Dealing with a composite key (student_id and exam_id)
-- score column is never NULL

-- show highest score along with its corresponding exam_id
 -- if there are numerous highest scores, return the one with the smallest exam id

-- ignoring the smallest id condition for now
-- it would look something like:
-- selecting max(score) along with other cols from the table group_by student id
SELECT DISTINCT ON (student_id)
    student_id,
    exam_id,
    score
FROM exam_results
ORDER BY student_id, score DESC, exam_id;

