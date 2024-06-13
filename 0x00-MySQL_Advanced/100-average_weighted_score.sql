--
--
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score_w FLOAT;
    SET avg_score_w = (SELECT SUM(score * weight) / SUM(weight) 
                        FROM users AS U
                        JOIN corrections as C ON U.id=C.user_id 
                        JOIN projects AS P ON C.project_id=P.id 
                        WHERE U.id=user_id);
    UPDATE users SET average_score = avg_score_w WHERE id=user_id;
END;
$$