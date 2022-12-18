statements  : NEWLINE* statement (NEWLINE+ statement)* NEWLINE*

statement		: KEYWORD:lotaDo expr?
						: KEYWORD:chaltayRaho
						: KEYWORD:rukoZaraSabarKaro
						: expr

expr        : KEYWORD:yeHaiJani IDENTIFIER EQ expr
            : comp-expr ((KEYWORD:aur|KEYWORD:ya) comp-expr)*

comp-expr   : nahi comp-expr
            : arith-expr ((EE|LT|GT|LTE|GTE) arith-expr)*

arith-expr  :	term ((PLUS|MINUS) term)*

term        : factor ((MUL|DIV) factor)*

factor      : (PLUS|MINUS) factor
            : power

power       : call (POW factor)*

call        : atom (LPAREN (expr (COMMA expr)*)? RPAREN)?

atom        : INT|FLOAT|STRING|IDENTIFIER
            : LPAREN expr RPAREN
            : list-expr
            : if-expr
            : for-expr
            : while-expr
            : func-def

list-expr   : LSQUARE (expr (COMMA expr)*)? RSQUARE

if-expr     : KEYWORD:agarJani expr KEYWORD:phir
              (statement if-expr-b|if-expr-c?)
            | (NEWLINE statements KEYWORD:khatamJani|if-expr-b|if-expr-c)

if-expr-b   : KEYWORD:nahiTohJani expr KEYWORD:phir
              (statement if-expr-b|if-expr-c?)
            | (NEWLINE statements KEYWORD:khatamJani|if-expr-b|if-expr-c)

if-expr-c   : KEYWORD:toh
              statement
            | (NEWLINE statements KEYWORD:khatamJani)

for-expr    : KEYWORD:janiKaLia IDENTIFIER EQ expr KEYWORD:jabTak expr 
              (KEYWORD:qadam expr)? KEYWORD:phir
              statement
            | (NEWLINE statements KEYWORD:khatamJani)

while-expr  : KEYWORD:jabTakJani expr KEYWORD:phir
              statement
            | (NEWLINE statements KEYWORD:khatamJani)

func-def    : KEYWORD:samjhoJani IDENTIFIER?
              LPAREN (IDENTIFIER (COMMA IDENTIFIER)*)? RPAREN
              (ARROW expr)
            | (NEWLINE statements KEYWORD:khatamJani)
