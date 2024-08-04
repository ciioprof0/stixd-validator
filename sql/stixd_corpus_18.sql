-- Create trigger to check for prolog constraints
DROP TRIGGER IF EXISTS stixd_corpus.trg_lexicon_prolog_constraints
DELIMITER //
CREATE TRIGGER stixd_corpus.trg_lexicon_prolog_constraints
BEFORE INSERT ON stixd_corpus.lexicon
FOR EACH ROW
BEGIN
    DECLARE constraint_violation VARCHAR(255);
    DECLARE constraint_message VARCHAR(255);

    -- Check for each prolog constraint
    DECLARE cur CURSOR FOR 
    SELECT description, pattern, message 
    FROM stixd_corpus.prolog_constraints;
    
    OPEN cur;
    prolog_loop: LOOP
        FETCH cur INTO constraint_violation, constraint_message;
        IF constraint_violation IS NULL THEN
            LEAVE prolog_loop;
        END IF;
        -- Evaluate each constraint
        IF NOT (NEW.base_form REGEXP constraint_violation) THEN
            SET constraint_message = constraint_message;
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = constraint_message;
        END IF;
    END LOOP prolog_loop;
    CLOSE cur;
END;
//
DELIMITER ;
