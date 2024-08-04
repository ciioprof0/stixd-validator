-- Create the genders table in the specified database
DROP TABLE IF EXISTS stixd_corpus.genders;
CREATE TABLE stixd_corpus.genders (
    gender VARCHAR(7) PRIMARY KEY
);
SHOW CREATE TABLE stixd_corpus.genders;

-- Populate the genders table from ACE 6.7 Lexicon Specification
INSERT INTO stixd_corpus.genders (gender) VALUES
('undef'), ('neutr'), ('human'), ('masc'), ('fem');

SELECT * FROM stixd_corpus.genders;