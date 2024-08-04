-- Create the doc_sent_jt table in the specified database
DROP TABLE IF EXISTS stixd_corpus.doc_sent_jt;
CREATE TABLE stixd_corpus.doc_sent_jt (
    doc_id INT,
    sent_id INT,
    PRIMARY KEY (doc_id, sent_id),
    FOREIGN KEY (doc_id) REFERENCES stixd_corpus.documents(doc_id),
    FOREIGN KEY (sent_id) REFERENCES stixd_corpus.sentences(sent_id)
);
SHOW CREATE TABLE stixd_corpus.doc_sent_jt;