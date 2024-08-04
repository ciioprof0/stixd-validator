% Adjectives

    % Adverbs
        adv(PositiveForm, LogicalSymbol).   % base_form
        adv_comp(ComparativeForm, LogicalSymbol).
        adv_sup(SuperlativeForm, LogicalSymbol).

    % Intransitive Adjectives
        adj_itr(PositiveForm, LogicalSymbol).   % base_form
        adj_itr_comp(ComparativeForm, LogicalSymbol).
        adj_itr_sup(SuperlativeForm, LogicalSymbol).

    % Transitive Adjectives (adj_tr)
        adj_tr(PositiveForm, LogicalSymbol, Preposition).   % base_form
        adj_tr_comp(ComparativeForm, LogicalSymbol, Preposition).
        adj_tr_sup(SuperlativeForm, LogicalSymbol, Preposition).

% Nouns

    % Countable Nouns
        noun_sg(SingularForm, LogicalSymbol, Gender).   % base_form
        noun_pl(PluralForm, LogicalSymbol, Gender).

    % Mass Nouns
        noun_mass(WordForm, LogicalSymbol, Gender).   % base_form

    % Measurement Nouns
        mn_sg(SingularForm, LogicalSymbol).   % base_form
        mn_pl(PluralForm, LogicalSymbol).

    % Proper Names that do not take determiners
        pn_sg(WordForm, LogicalSymbol, Gender).   % base_form
        pn_pl(WordForm, LogicalSymbol, Gender).

    % Proper Names that take determiners
        pndef_sg(WordForm, LogicalSymbol, Gender).   % base_form
        pndef_pl(WordForm, LogicalSymbol, Gender).


% Verbs

    % Intransitive Verbs
        iv_finsg(ThirdSgForm, LogicalSymbol).
        iv_infpl(InfForm, LogicalSymbol).   % base_form

    % Transitive Verbs
        tv_finsg(ThirdSgForm, LogicalSymbol).
        tv_infpl(InfForm, LogicalSymbol).   % base_form
        tv_pp(PastPartForm, LogicalSymbol).

    % Ditransitive Verbs
        dv_finsg(ThirdSgForm, LogicalSymbol, Preposition).
        dv_infpl(InfForm, LogicalSymbol, Preposition).   % base_form
        dv_pp(PastPartForm, LogicalSymbol, Preposition).


% Prepositions
    prep(WordForm, LogicalSymbol).   % base_form