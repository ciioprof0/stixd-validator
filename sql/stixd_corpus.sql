-- Create the database (stix_corpus_01.sql)
DROP DATABASE IF EXISTS stixd_corpus;
CREATE DATABASE stixd_corpus;
-- SHOW databases;

-- Create the genders table in the specified database  (stix_corpus_02.sql)
-- DROP TABLE IF EXISTS stixd_corpus.genders;
CREATE TABLE stixd_corpus.genders (
    gender VARCHAR(7) PRIMARY KEY
);
-- SHOW CREATE TABLE stixd_corpus.genders;

-- Populate the genders table from ACE 6.7 Lexicon Specification
INSERT INTO stixd_corpus.genders (gender) VALUES
('undef'), ('neutr'), ('human'), ('masc'), ('fem');

-- SELECT * FROM stixd_corpus.genders;

-- Create the special_characters table in the specified database  (stix_corpus_03.sql)
-- DROP TABLE IF EXISTS stixd_corpus.special_characters;
CREATE TABLE stixd_corpus.special_characters (
    char_id INT AUTO_INCREMENT PRIMARY KEY,
    spec_char CHAR(1) UNIQUE,
    esc_seq VARCHAR(10)
);
-- SHOW CREATE TABLE stixd_corpus.special_characters;

-- Insert the special characters and their escape sequences
INSERT INTO stixd_corpus.special_characters (spec_char, esc_seq) VALUES
('\\', '\\\\'), ('\'', '\'\''), ('"', '\\"'), (',', '\\,'), ('.', '\\.'), 
(';', '\\;'), (':', '\\:'), ('!', '\\!'), ('(', '\\('), (')', '\\)'),
('[', '\\['), (']', '\\]'), ('{', '\\{'), ('}', '\\}'), ('|', '\\|'), ('@', '\\@'), 
('#', '\\#'), ('&', '\\&'), ('^', '\\^'), ('*', '\\*'), ('?', '\\?'), ('/', '\\/');

-- SELECT * FROM stixd_corpus.special_characters;


-- Create the prohibited_words table in the specified database (stix_corpus_04.sql)
-- DROP TABLE IF EXISTS stixd_corpus.prohibited_words;
CREATE TABLE stixd_corpus.prohibited_words (
    word VARCHAR(20) PRIMARY KEY
);
-- SHOW CREATE TABLE stixd_corpus.prohibited_words;

-- Insert the prohibited words from ACE 6.7 Lexicon Specification
INSERT INTO stixd_corpus.prohibited_words (word) VALUES
('null'), ('zero'), ('one'), ('two'), ('three'), ('four'), ('five'), ('six'), 
('seven'), ('eight'), ('nine'), ('ten'), ('eleven'), ('twelve'), ('dozen'), ('there'), 
('and'), ('or'), ('not'), ('that'), ('than'), ('of'), ('if'), ('then'), ('such'), 
('be'), ('provably'), ('more'), ('most'), ('are'), ('is'), ('the'), ('a'), ('an'), 
('some'), ('no'), ('every'), ('all'), ('each'), ('which'), ('its'), ('his'), ('her'),
('their'), ('whose'), ('it'), ('he'), ('she'), ('they'), ('him'), ('them'), 
('itself'), ('himself'), ('herself'), ('themselves'), ('someone'), ('somebody'), 
('something'), ('nobody'), ('nothing'), ('everyone'), ('everybody'), ('everything'), 
('what'), ('who'), ('how'), ('where'), ('when');

-- SELECT * FROM stixd_corpus.prohibited_words;

-- Create the prohibited_intersections table in the specified database (stix_corpus_05.sql)
-- DROP TABLE IF EXISTS stixd_corpus.prohibited_intersections;
CREATE TABLE stixd_corpus.prohibited_intersections (
    class1 VARCHAR(31),
    class2 VARCHAR(31),
    PRIMARY KEY (class1, class2)
);
-- SHOW CREATE TABLE stixd_corpus.prohibited_intersections;

-- Insert the prohibited intersections
INSERT INTO stixd_corpus.prohibited_intersections (class1, class2) VALUES
('adv', 'noun_sg'), ('adv', 'noun_pl'), ('adv', 'noun_mass'), ('adv', 'iv_finsg'), 
('adv', 'iv_infpl'), ('adj_itr', 'adj_tr'), ('pndef_sg', 'noun_sg'), 
('pndef_sg', 'noun_pl'), ('pndef_sg', 'noun_mass'), ('pndef_pl', 'noun_sg'),
('pndef_pl', 'noun_pl'), ('pndef_pl', 'noun_mass'), ('prep', 'adj_itr'), 
('prep', 'adj_itr_comp'), ('prep', 'adj_itr_sup'), ('prep', 'tv_finsg'),
('prep', 'tv_infpl'), ('prep', 'tv_pp');

-- SELECT * FROM stixd_corpus.prohibited_intersections;


-- Create the prolog_constraints table in the specified database (stix_corpus_06.sql)
-- DROP TABLE IF EXISTS stixd_corpus.prolog_constraints;
CREATE TABLE stixd_corpus.prolog_constraints (constraint_id INT AUTO_INCREMENT PRIMARY KEY, description VARCHAR(511), pattern VARCHAR(255), message VARCHAR(255),  auto_correct BOOLEAN);
-- SHOW CREATE TABLE stixd_corpus.prolog_constraints;

-- Insert the constraints with auto_correct flag
INSERT INTO stixd_corpus.prolog_constraints (description, pattern, message, auto_correct) VALUES
('The word form must contain only lower and upper case letters (a-z, A-Z), digits (0-9), hyphens (-), underscores (_), dollar signs ($), and degree signs (°).', '^[a-zA-Z_$°][a-zA-Z0-9_$°-]*$', 'Invalid characters in word_form. Allowed characters are: a-z, A-Z, 0-9, -, _, $, °.', TRUE),
('The first character must not be a digit or a hyphen.', '^[^0-9-]', 'The first character must not be a digit or a hyphen.', TRUE),
('Blank spaces are not allowed. Use hyphens instead of blank spaces.', '^.*[^ ].*$', 'Blank spaces are not allowed in word_form. Use hyphens instead.', TRUE),
('Symbols special for Prolog (e.g., apostrophe) must be escaped.', '', 'Symbols special for Prolog (e.g., apostrophe) must be escaped.', TRUE),
('Capitalized words (e.g., proper names) must be in quotes, otherwise they would be considered variables by Prolog.', '', 'Capitalized words (e.g., proper names) must be in quotes.', TRUE);

-- SELECT * FROM stixd_corpus.prolog_constraints;

-- Create the stix_objects table in the specified database (stix_corpus_07.sql)
-- DROP TABLE IF EXISTS stixd_corpus.stix_objects;
CREATE TABLE stixd_corpus.stix_objects (
    obj_id VARCHAR(292) PRIMARY KEY,
    type VARCHAR(255),
    created_by_ref VARCHAR(255),
    description TEXT, -- Optional raw text description
    spec_version VARCHAR(8) DEFAULT '2.1',
    created TIMESTAMP,
    modified TIMESTAMP,
    revoked BOOLEAN,
    labels JSON,
    confidence INT CHECK (confidence BETWEEN 0 AND 100),
    lang VARCHAR(20) DEFAULT 'en',
    external_references JSON,
    object_marking_refs JSON,
    granular_markings JSON,
    extensions JSON,
    derived_from JSON,
    duplicate_of JSON,
    related_to JSON
);
-- SHOW CREATE TABLE stixd_corpus.stix_objects;

-- Create the documents table in the specified database (stix_corpus_08.sql)
-- DROP TABLE IF EXISTS stixd_corpus.documents;
CREATE TABLE stixd_corpus.documents (
    doc_id INT AUTO_INCREMENT PRIMARY KEY,
    raw_text LONGTEXT,
    proc_text JSON,
    metadata JSON
);
-- SHOW CREATE TABLE stixd_corpus.documents;

-- Populating table done from Python script.

-- Create the sentences table in the specified database (stix_corpus_09.sql)
-- DROP TABLE IF EXISTS stixd_corpus.sentences;
CREATE TABLE stixd_corpus.sentences (
    sent_id INT AUTO_INCREMENT PRIMARY KEY,
    raw_sent TEXT,
    proc_sent JSON
);
-- SHOW CREATE TABLE stixd_corpus.sentences;

-- Populating table done from Python script.

-- Create the validation_results table in the specified database (stix_corpus_10.sql)
-- DROP TABLE IF EXISTS stixd_corpus.validation_results;
CREATE TABLE stixd_corpus.validation_results (
    val_id INT AUTO_INCREMENT PRIMARY KEY,
    obj_id VARCHAR(292),
    is_valid BOOLEAN,
    val_errors JSON,
    FOREIGN KEY (obj_id) REFERENCES stixd_corpus.stix_objects(obj_id)
);
-- SHOW CREATE TABLE stixd_corpus.validation_results;

-- Populating table done from Python script.

-- Create the lexicon table in the specified database (stix_corpus_11.sql)
-- DROP TABLE IF EXISTS stixd_corpus.lexicon;
CREATE TABLE stixd_corpus.lexicon (
    lex_id INT AUTO_INCREMENT PRIMARY KEY,
    word_class VARCHAR(31),
    base_form VARCHAR(255),
    logical_symbol VARCHAR(255),
    preposition INT,
    gender VARCHAR(7),
    definition TEXT,
    synsets JSON,
    tagsets JSON,
    UNIQUE (word_class, base_form),
    FOREIGN KEY (preposition) REFERENCES stixd_corpus.lexicon(lex_id),
    FOREIGN KEY (gender) REFERENCES stixd_corpus.genders(gender)
);
-- SHOW CREATE TABLE stixd_corpus.lexicon;

-- Populating table done from Python script.


-- Create a trigger to enforce the mutual exclusivity of preposition and gender (stix_corpus_12.sql)
-- DROP TRIGGER IF EXISTS stixd_corpus.trg_lexicon_preposition_gender
DELIMITER //
CREATE TRIGGER stixd_corpus.trg_lexicon_preposition_gender
BEFORE INSERT ON stixd_corpus.lexicon
FOR EACH ROW
BEGIN
    IF (NEW.preposition IS NOT NULL AND NEW.gender IS NOT NULL) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'preposition and gender cannot both be NOT NULL';
    END IF;
END;
//
DELIMITER ;

-- Create the trigger to enforce preposition must be from an entry with word_class = prep  (stix_corpus_13.sql)
-- DROP TRIGGER IF EXISTS stixd_corpus.trg_lexicon_preposition_check;
DELIMITER //
CREATE TRIGGER stixd_corpus.trg_lexicon_preposition_check
BEFORE INSERT ON stixd_corpus.lexicon
FOR EACH ROW
BEGIN
    DECLARE word_class_check VARCHAR(31);
    IF (NEW.preposition IS NOT NULL) THEN
        SELECT word_class INTO word_class_check
        FROM stixd_corpus.lexicon
        WHERE lex_id = NEW.preposition;
        
        IF (word_class_check NOT LIKE 'prep%') THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'preposition must reference an entry with word_class starting with "prep"';
        END IF;
    END IF;
END;
//
DELIMITER ;


-- Create trigger to ensure preposition is not null if word_class starts with adj_tr or dv_ (stix_corpus_14.sql)
-- DROP TRIGGER IF EXISTS stixd_corpus.trg_lexicon_word_class_preposition
DELIMITER //
CREATE TRIGGER stixd_corpus.trg_lexicon_word_class_preposition
BEFORE INSERT ON stixd_corpus.lexicon
FOR EACH ROW
BEGIN
    IF (NEW.word_class LIKE 'adj_tr%' OR NEW.word_class LIKE 'dv_%') THEN
        IF (NEW.preposition IS NULL) THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'preposition must be NOT NULL if word_class starts with "adj_tr" or "dv_"';
        END IF;
    END IF;
END;
//
DELIMITER ;

-- Create trigger to ensure gender is not null if word_class starts with noun_ or pn  (stix_corpus_15.sql)
-- DROP TRIGGER IF EXISTS stixd_corpus.trg_lexicon_word_class_gender
DELIMITER //
CREATE TRIGGER stixd_corpus.trg_lexicon_word_class_gender
BEFORE INSERT ON stixd_corpus.lexicon
FOR EACH ROW
BEGIN
    IF (NEW.word_class LIKE 'noun_%' OR NEW.word_class LIKE 'pn%') THEN
        IF (NEW.gender IS NULL) THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'gender must be NOT NULL if word_class starts with "noun_" or "pn"';
        END IF;
    END IF;
END;
//
DELIMITER ;

-- Create the trigger to check for prohibited words in the base_form (stix_corpus_16.sql)
-- DROP TRIGGER IF EXISTS stixd_corpus.trg_lexicon_prohibited_words;
DELIMITER //
CREATE TRIGGER stixd_corpus.trg_lexicon_prohibited_words
BEFORE INSERT ON stixd_corpus.lexicon
FOR EACH ROW
BEGIN
    DECLARE prohibited_word_found INT DEFAULT 0;
    SELECT COUNT(*)
    INTO prohibited_word_found
    FROM stixd_corpus.prohibited_words
    WHERE word = NEW.base_form;

    IF prohibited_word_found > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'base_form contains a prohibited word';
    END IF;
END;
//
DELIMITER ;

-- Create the trigger to check for prohibited intersections (stix_corpus_17.sql)
-- DROP TRIGGER IF EXISTS stixd_corpus.trg_lexicon_prohibited_intersections;
DELIMITER //
CREATE TRIGGER stixd_corpus.trg_lexicon_prohibited_intersections
BEFORE INSERT ON stixd_corpus.lexicon
FOR EACH ROW
BEGIN
    DECLARE class_check INT DEFAULT 0;

    -- Check first condition
    SELECT COUNT(*)
    INTO class_check
    FROM stixd_corpus.prohibited_intersections
    WHERE class1 = NEW.word_class
      AND class2 IN (SELECT word_class
                     FROM stixd_corpus.lexicon
                     WHERE lex_id = NEW.preposition);

    IF class_check > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'This combination of word_class and preposition is prohibited';
    END IF;

    -- Reset the variable
    SET class_check = 0;

    -- Check second condition
    SELECT COUNT(*)
    INTO class_check
    FROM stixd_corpus.prohibited_intersections
    WHERE class2 = NEW.word_class
      AND class1 IN (SELECT word_class
                     FROM stixd_corpus.lexicon
                     WHERE lex_id = NEW.preposition);

    IF class_check > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'This combination of word_class and preposition is prohibited';
    END IF;
END;
//
DELIMITER ;


-- Create procedure to check for prolog constraints (stix_corpus_18.sql)
DELIMITER //
CREATE PROCEDURE stixd_corpus.check_prolog_constraints (IN base_form VARCHAR(255))
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE constraint_violation VARCHAR(255);
    DECLARE constraint_message VARCHAR(255);

    DECLARE cur CURSOR FOR SELECT pattern, message FROM stixd_corpus.prolog_constraints;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO constraint_violation, constraint_message;
        IF done THEN
            LEAVE read_loop;
        END IF;
        IF NOT (base_form REGEXP constraint_violation) THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = constraint_message;
        END IF;
    END LOOP;

    CLOSE cur;
END;
//
DELIMITER ;


-- Create the trigger to check for prolog constraints  (stix_corpus_18.sql)
-- DROP TRIGGER IF EXISTS stixd_corpus.trg_lexicon_prolog_constraints;
DELIMITER //
CREATE TRIGGER stixd_corpus.trg_lexicon_prolog_constraints
BEFORE INSERT ON stixd_corpus.lexicon
FOR EACH ROW
BEGIN
    CALL stixd_corpus.check_prolog_constraints(NEW.base_form);
END;
//
DELIMITER ;


-- Create the obj_doc_jt table in the specified database (stix_corpus_19.sql)
-- DROP TABLE IF EXISTS stixd_corpus.obj_doc_jt;
CREATE TABLE stixd_corpus.obj_doc_jt (
    obj_id VARCHAR(292),
    doc_id INT,
    PRIMARY KEY (obj_id, doc_id),
    FOREIGN KEY (obj_id) REFERENCES stixd_corpus.stix_objects(obj_id),
    FOREIGN KEY (doc_id) REFERENCES stixd_corpus.documents(doc_id)
);
-- SHOW CREATE TABLE stixd_corpus.obj_doc_jt;

-- Create the doc_sent_jt table in the specified database (stix_corpus_20.sql)
-- DROP TABLE IF EXISTS stixd_corpus.doc_sent_jt;
CREATE TABLE stixd_corpus.doc_sent_jt (
    doc_id INT,
    sent_id INT,
    PRIMARY KEY (doc_id, sent_id),
    FOREIGN KEY (doc_id) REFERENCES stixd_corpus.documents(doc_id),
    FOREIGN KEY (sent_id) REFERENCES stixd_corpus.sentences(sent_id)
);
-- SHOW CREATE TABLE stixd_corpus.doc_sent_jt;

-- Create the doc_lex_jt table in the specified database (stix_corpus_21.sql)
-- DROP TABLE IF EXISTS stixd_corpus.doc_lex_jt;
CREATE TABLE stixd_corpus.doc_lex_jt (
    doc_id INT,
    lex_id INT,
    PRIMARY KEY (doc_id, lex_id),
    FOREIGN KEY (doc_id) REFERENCES stixd_corpus.documents(doc_id),
    FOREIGN KEY (lex_id) REFERENCES stixd_corpus.lexicon(lex_id)
);
-- SHOW CREATE TABLE stixd_corpus.doc_lex_jt;

-- Create the sent_lex_jt table in the specified database (stix_corpus_22.sql)
-- DROP TABLE IF EXISTS stixd_corpus.sent_lex_jt;
CREATE TABLE stixd_corpus.sent_lex_jt (
    sent_id INT,
    lex_id INT,
    PRIMARY KEY (sent_id, lex_id),
    FOREIGN KEY (sent_id) REFERENCES stixd_corpus.sentences(sent_id),
    FOREIGN KEY (lex_id) REFERENCES stixd_corpus.lexicon(lex_id)
);
-- SHOW CREATE TABLE stixd_corpus.sent_lex_jt;

-- Create the obj_lex_jt table in the specified database (stix_corpus_23.sql)
-- DROP TABLE IF EXISTS stixd_corpus.obj_lex_jt;
CREATE TABLE stixd_corpus.obj_lex_jt (
    obj_id VARCHAR(292),
    lex_id INT,
    PRIMARY KEY (obj_id, lex_id),
    FOREIGN KEY (obj_id) REFERENCES stixd_corpus.stix_objects(obj_id),
    FOREIGN KEY (lex_id) REFERENCES stixd_corpus.lexicon(lex_id)
);
-- SHOW CREATE TABLE stixd_corpus.obj_lex_jt;