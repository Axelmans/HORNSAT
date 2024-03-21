grammar HORNSAT;

formula
    : clause ('&&' clause)* #AllClauses
    ;

clause
    : '(' NEGATION? VAR (DISJUNCTION NEGATION? VAR)* ')' #SingleClause
    ;

VAR: [a-zA-Z];

NEGATION: '~';
DISJUNCTION: '||';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines