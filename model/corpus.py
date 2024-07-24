from typing import Any, Dict, List, Optional, Set


class Corpus:
    """
    A class to represent a corpus entry.

    Attributes:
        url (str): The URL from which the data was scraped.
        page_hash (str): The hash of the page content.
        text (str): The raw scraped text.
        metadata (Optional[Dict[str, Any]]): Additional metadata.
        date_scraped (str): The date when the data was scraped.
        tokens (Optional[List[str]]): Tokenized text.
        pos_tags (Optional[Dict[str, str]]): POS tags for the tokens.
        named_entities (Optional[Dict[str, str]]): Named entities.
        processed_text (Optional[str]): Cleaned and preprocessed text.
        lemmas (Optional[List[str]]): Lemmatized text.
        vocabulary (Optional[Set[str]]): Unique set of words.
        sentiment (Optional[Dict[str, Any]]): Sentiment analysis results.
        keywords (Optional[List[str]]): Extracted keywords or key phrases.
    """

    def __init__(
        self,
        url: str,
        page_hash: str,
        text: str,
        metadata: Optional[Dict[str, Any]] = None,
        date_scraped: Optional[str] = None,
        tokens: Optional[List[str]] = None,
        pos_tags: Optional[Dict[str, str]] = None,
        named_entities: Optional[Dict[str, str]] = None,
        processed_text: Optional[str] = None,
        lemmas: Optional[List[str]] = None,
        vocabulary: Optional[Set[str]] = None,
        sentiment: Optional[Dict[str, Any]] = None,
        keywords: Optional[List[str]] = None
    ) -> None:
        """
        Constructs all the necessary attributes for the corpus object.

        Args:
            url (str): The URL from which the data was scraped.
            page_hash (str): The hash of the page content.
            text (str): The raw scraped text.
            metadata (Optional[Dict[str, Any]]): Additional metadata.
            date_scraped (Optional[str]): The date when the data was scraped.
            tokens (Optional[List[str]]): Tokenized text.
            pos_tags (Optional[Dict[str, str]]): POS tags for the tokens.
            named_entities (Optional[Dict[str, str]]): Named entities.
            processed_text (Optional[str]): Cleaned and preprocessed text.
            lemmas (Optional[List[str]]): Lemmatized text.
            vocabulary (Optional[Set[str]]): Unique set of words.
            sentiment (Optional[Dict[str, Any]]): Sentiment analysis results.
            keywords (Optional[List[str]]): Extracted keywords or key phrases.
        """
        self.url = url
        self.page_hash = page_hash
        self.text = text
        self.metadata = metadata
        self.date_scraped = date_scraped
        self.tokens = tokens
        self.pos_tags = pos_tags
        self.named_entities = named_entities
        self.processed_text = processed_text
        self.lemmas = lemmas
        self.vocabulary = vocabulary
        self.sentiment = sentiment
        self.keywords = keywords