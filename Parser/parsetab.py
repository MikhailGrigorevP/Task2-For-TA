
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftTOleftLESSGREATEREQNOTEQleftPLUSMINUSASSIGNMENT BACK BEGIN BOOL BRACKETS COMMA COMMENT CONCRETE CONTINUE DECIMAL DO DOUBLE_QUOTE DRILL ELSE END EQ EXIT FALSE FORWARD FRONT FUNCTION GLASS GREATER IF INTEGER LBRACKET LEFT LESS LMS L_QBRACKET MINUS NEWLINE NOTEQ OF PLASTIC PLUS POP PUSH QUOTE RBRACKET REFLECT RETURN RIGHT ROTATE_LEFT ROTATE_RIGHT R_QBRACKET STEEL STRING THEN TO TRUE UNDEFINED UNTIL VARIABLE VECTOR WOODprogram : statementsstatements_group : BEGIN statements END\n                            | inner_statementinner_statement : declaration\n                     | assignment\n                     | while\n                     | if\n                     | command\n                     | function\n                     | call\n                     | RETURN expression\n                     | emptystatements : statements statement\n                      | statementstatement : declaration NEWLINE\n                     | comment NEWLINE\n                     | assignment NEWLINE\n                     | while NEWLINE\n                     | if NEWLINE\n                     | command NEWLINE\n                     | function NEWLINE\n                     | call NEWLINE\n                     | RETURN expression NEWLINE\n                     | empty NEWLINEstatement : errors NEWLINEstatement : errorsdeclaration : type variablescomment : COMMENT anyany : any VARIABLE\n               | VARIABLEtype : INTEGER\n                | STRING\n                | BOOL\n                | VECTOR OF type\n        type : errorsvariables : variable COMMA variables\n                | assignment COMMA variables\n                | variable\n                | assignmentassignment : variable ASSIGNMENT expressionvariable : VARIABLE indexing\n                    | VARIABLEindexing : L_QBRACKET expression R_QBRACKET indexing\n                    | L_QBRACKET expression R_QBRACKETexpression : variable\n                      | const\n                      | qstring\n                      | math_expression\n                      | robot_command\n                      | converting_command\n                      | vector_pop\n                      | callqstring : DOUBLE_QUOTE string DOUBLE_QUOTE\n                   | QUOTE string QUOTEstring : VARIABLE string\n                   | DECIMAL string\n                   | FALSE string\n                   | TRUE string\n                   | FALSE\n                   | TRUE\n                   | DECIMAL\n                   | VARIABLEconst : TRUE\n                 | FALSE\n                 | UNDEFINED\n                 | DECIMAL\n                 | EXIT\n                 | WOOD\n                 | STEEL\n                 | GLASS\n                 | CONCRETE\n                 | PLASTICmath_expression : expression LESS expression\n                           | expression GREATER expression\n                           | expression EQ expression\n                           | expression NOTEQ expression\n                           | expression PLUS expression\n                           | expression MINUS expressionwhile : DO statements_group UNTIL expressionif : IF expression THEN statements_group\n              | IF expression THEN statements_group ELSE statements_groupfunction : FUNCTION OF type VARIABLE LBRACKET parameters RBRACKET statements_group\n                    | FUNCTION OF type VARIABLE BRACKETS statements_groupcommand : vector_command\n                   | robot_commandconverting_command : expression TO type\n                              | expression TO expression\n                              | expression TO vector_ofvector_of : VECTOR OF vector_of\n                    | VECTORvector_command : variable PUSH BACK expression\n                          | variable PUSH FRONT expressionvector_pop : variable POP BACK\n                      | variable POP FRONTrobot_command : LEFT\n                    | RIGHT\n                    | FORWARD\n                    | BACK\n                    | ROTATE_RIGHT\n                    | ROTATE_LEFT\n                    | LMS\n                    | REFLECT\n                    | DRILLcall : VARIABLE LBRACKET parameters RBRACKET\n                | VARIABLE BRACKETSempty : parameters : parameters COMMA parameter\n                      | parameter\n                      | CONTINUEparameter : expression\n                     | VARIABLE EQ expressionerrors : errors error\n                    | error'
    
_lr_action_items = {'RETURN':([0,2,3,14,18,24,38,39,40,41,42,43,44,45,46,69,70,71,81,100,122,124,164,166,174,],[12,12,-14,-26,90,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,12,-23,12,90,90,90,90,]),'COMMENT':([0,2,3,14,24,38,39,40,41,42,43,44,45,46,69,70,71,81,100,122,],[16,16,-14,-26,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,16,-23,16,]),'DO':([0,2,3,14,18,24,38,39,40,41,42,43,44,45,46,69,70,71,81,100,122,124,164,166,174,],[18,18,-14,-26,18,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,18,-23,18,18,18,18,18,]),'IF':([0,2,3,14,18,24,38,39,40,41,42,43,44,45,46,69,70,71,81,100,122,124,164,166,174,],[19,19,-14,-26,19,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,19,-23,19,19,19,19,19,]),'FUNCTION':([0,2,3,14,18,24,38,39,40,41,42,43,44,45,46,69,70,71,81,100,122,124,164,166,174,],[22,22,-14,-26,22,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,22,-23,22,22,22,22,22,]),'VARIABLE':([0,2,3,12,14,15,16,18,19,24,25,26,27,38,39,40,41,42,43,44,45,46,67,68,69,70,71,76,77,78,81,90,92,95,98,100,101,102,103,104,105,106,107,110,111,112,113,115,116,117,119,120,121,122,124,125,132,159,161,164,165,166,174,],[23,23,-14,56,-26,75,77,23,56,-113,-31,-32,-33,-13,-15,-16,-17,-18,-19,-20,-21,-22,110,110,-24,-25,-112,117,-30,56,23,56,-35,126,56,-23,56,56,56,56,56,56,56,110,110,110,110,75,75,-29,56,56,56,23,23,158,-34,56,126,23,126,23,23,]),'NEWLINE':([0,2,3,4,5,6,7,8,9,10,11,13,14,20,21,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,71,72,73,74,75,76,77,81,82,83,84,85,86,87,88,89,91,92,96,97,100,117,118,122,123,124,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,151,152,153,154,155,156,157,160,162,164,166,169,170,171,173,174,175,],[-106,-106,-14,39,40,41,42,43,44,45,46,69,70,-84,-85,-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,-13,-15,-16,-17,-18,-19,-20,-21,-22,100,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-24,-25,-112,-27,-38,-39,-42,-28,-30,-106,-3,-4,-5,-6,-7,-8,-9,-10,-12,-35,-105,-41,-23,-29,-40,-106,-11,-106,-34,-73,-74,-75,-76,-77,-78,-87,-86,-88,-90,-93,-94,-53,-54,-36,-37,-91,-92,-79,-2,-80,-104,-44,-106,-106,-43,-89,-81,-83,-106,-82,]),'error':([0,2,3,14,18,24,38,39,40,41,42,43,44,45,46,69,70,71,81,92,94,99,100,107,122,124,163,164,166,174,],[24,24,-14,71,24,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,24,71,24,24,-23,24,24,24,24,24,24,24,]),'INTEGER':([0,2,3,14,18,24,38,39,40,41,42,43,44,45,46,69,70,71,81,94,99,100,107,122,124,163,164,166,174,],[25,25,-14,-26,25,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,25,25,25,-23,25,25,25,25,25,25,25,]),'STRING':([0,2,3,14,18,24,38,39,40,41,42,43,44,45,46,69,70,71,81,94,99,100,107,122,124,163,164,166,174,],[26,26,-14,-26,26,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,26,26,26,-23,26,26,26,26,26,26,26,]),'BOOL':([0,2,3,14,18,24,38,39,40,41,42,43,44,45,46,69,70,71,81,94,99,100,107,122,124,163,164,166,174,],[27,27,-14,-26,27,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,27,27,27,-23,27,27,27,27,27,27,27,]),'VECTOR':([0,2,3,14,18,24,38,39,40,41,42,43,44,45,46,69,70,71,81,94,99,100,107,122,124,163,164,166,174,],[28,28,-14,-26,28,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,28,28,28,-23,142,28,28,142,28,28,28,]),'LEFT':([0,2,3,12,14,18,19,24,38,39,40,41,42,43,44,45,46,69,70,71,78,81,90,95,98,100,101,102,103,104,105,106,107,119,120,121,122,124,159,161,164,165,166,174,],[30,30,-14,30,-26,30,30,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,30,30,30,30,30,-23,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'RIGHT':([0,2,3,12,14,18,19,24,38,39,40,41,42,43,44,45,46,69,70,71,78,81,90,95,98,100,101,102,103,104,105,106,107,119,120,121,122,124,159,161,164,165,166,174,],[31,31,-14,31,-26,31,31,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,31,31,31,31,31,-23,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'FORWARD':([0,2,3,12,14,18,19,24,38,39,40,41,42,43,44,45,46,69,70,71,78,81,90,95,98,100,101,102,103,104,105,106,107,119,120,121,122,124,159,161,164,165,166,174,],[32,32,-14,32,-26,32,32,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,32,32,32,32,32,-23,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'BACK':([0,2,3,12,14,18,19,24,38,39,40,41,42,43,44,45,46,69,70,71,78,79,81,90,95,98,100,101,102,103,104,105,106,107,108,119,120,121,122,124,159,161,164,165,166,174,],[29,29,-14,29,-26,29,29,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,29,119,29,29,29,29,-23,29,29,29,29,29,29,29,143,29,29,29,29,29,29,29,29,29,29,29,]),'ROTATE_RIGHT':([0,2,3,12,14,18,19,24,38,39,40,41,42,43,44,45,46,69,70,71,78,81,90,95,98,100,101,102,103,104,105,106,107,119,120,121,122,124,159,161,164,165,166,174,],[33,33,-14,33,-26,33,33,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,33,33,33,33,33,-23,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'ROTATE_LEFT':([0,2,3,12,14,18,19,24,38,39,40,41,42,43,44,45,46,69,70,71,78,81,90,95,98,100,101,102,103,104,105,106,107,119,120,121,122,124,159,161,164,165,166,174,],[34,34,-14,34,-26,34,34,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,34,34,34,34,34,-23,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'LMS':([0,2,3,12,14,18,19,24,38,39,40,41,42,43,44,45,46,69,70,71,78,81,90,95,98,100,101,102,103,104,105,106,107,119,120,121,122,124,159,161,164,165,166,174,],[35,35,-14,35,-26,35,35,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,35,35,35,35,35,-23,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'REFLECT':([0,2,3,12,14,18,19,24,38,39,40,41,42,43,44,45,46,69,70,71,78,81,90,95,98,100,101,102,103,104,105,106,107,119,120,121,122,124,159,161,164,165,166,174,],[36,36,-14,36,-26,36,36,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,36,36,36,36,36,-23,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'DRILL':([0,2,3,12,14,18,19,24,38,39,40,41,42,43,44,45,46,69,70,71,78,81,90,95,98,100,101,102,103,104,105,106,107,119,120,121,122,124,159,161,164,165,166,174,],[37,37,-14,37,-26,37,37,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,37,37,37,37,37,-23,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'$end':([1,2,3,14,24,38,39,40,41,42,43,44,45,46,69,70,71,100,],[0,-1,-14,-26,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,-23,]),'END':([3,14,24,38,39,40,41,42,43,44,45,46,69,70,71,100,122,],[-14,-26,-113,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-25,-112,-23,156,]),'TRUE':([12,19,67,68,78,90,95,98,101,102,103,104,105,106,107,110,111,112,113,119,120,121,159,161,165,],[57,57,113,113,57,57,57,57,57,57,57,57,57,57,57,113,113,113,113,57,57,57,57,57,57,]),'FALSE':([12,19,67,68,78,90,95,98,101,102,103,104,105,106,107,110,111,112,113,119,120,121,159,161,165,],[58,58,112,112,58,58,58,58,58,58,58,58,58,58,58,112,112,112,112,58,58,58,58,58,58,]),'UNDEFINED':([12,19,78,90,95,98,101,102,103,104,105,106,107,119,120,121,159,161,165,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'DECIMAL':([12,19,67,68,78,90,95,98,101,102,103,104,105,106,107,110,111,112,113,119,120,121,159,161,165,],[60,60,111,111,60,60,60,60,60,60,60,60,60,60,60,111,111,111,111,60,60,60,60,60,60,]),'EXIT':([12,19,78,90,95,98,101,102,103,104,105,106,107,119,120,121,159,161,165,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'WOOD':([12,19,78,90,95,98,101,102,103,104,105,106,107,119,120,121,159,161,165,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'STEEL':([12,19,78,90,95,98,101,102,103,104,105,106,107,119,120,121,159,161,165,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'GLASS':([12,19,78,90,95,98,101,102,103,104,105,106,107,119,120,121,159,161,165,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'CONCRETE':([12,19,78,90,95,98,101,102,103,104,105,106,107,119,120,121,159,161,165,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'PLASTIC':([12,19,78,90,95,98,101,102,103,104,105,106,107,119,120,121,159,161,165,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'DOUBLE_QUOTE':([12,19,78,90,95,98,101,102,103,104,105,106,107,109,110,111,112,113,119,120,121,146,147,148,149,159,161,165,],[67,67,67,67,67,67,67,67,67,67,67,67,67,145,-62,-61,-59,-60,67,67,67,-55,-56,-57,-58,67,67,67,]),'QUOTE':([12,19,78,90,95,98,101,102,103,104,105,106,107,110,111,112,113,114,119,120,121,146,147,148,149,159,161,165,],[68,68,68,68,68,68,68,68,68,68,68,68,68,-62,-61,-59,-60,150,68,68,68,-55,-56,-57,-58,68,68,68,]),'ASSIGNMENT':([17,23,73,75,97,162,169,],[78,-42,78,-42,-41,-44,-43,]),'PUSH':([17,23,97,162,169,],[79,-42,-41,-44,-43,]),'BEGIN':([18,124,164,166,174,],[81,81,81,81,81,]),'UNTIL':([18,20,21,24,25,26,27,29,30,31,32,33,34,35,36,37,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,72,73,74,75,80,82,83,84,85,86,87,88,89,91,92,96,97,118,123,124,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,151,152,153,154,155,156,157,160,162,164,166,169,170,171,173,174,175,],[-106,-84,-85,-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-112,-27,-38,-39,-42,121,-3,-4,-5,-6,-7,-8,-9,-10,-12,-35,-105,-41,-40,-11,-106,-34,-73,-74,-75,-76,-77,-78,-87,-86,-88,-90,-93,-94,-53,-54,-36,-37,-91,-92,-79,-2,-80,-104,-44,-106,-106,-43,-89,-81,-83,-106,-82,]),'ELSE':([20,21,24,25,26,27,29,30,31,32,33,34,35,36,37,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,72,73,74,75,82,83,84,85,86,87,88,89,91,92,96,97,118,123,124,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,151,152,153,154,155,156,157,160,162,164,166,169,170,171,173,174,175,],[-84,-85,-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-112,-27,-38,-39,-42,-3,-4,-5,-6,-7,-8,-9,-10,-12,-35,-105,-41,-40,-11,-106,-34,-73,-74,-75,-76,-77,-78,-87,-86,-88,-90,-93,-94,-53,-54,-36,-37,-91,-92,-79,-2,164,-104,-44,-106,-106,-43,-89,-81,-83,-106,-82,]),'OF':([22,28,142,],[94,99,163,]),'LBRACKET':([23,56,126,158,],[95,95,95,165,]),'BRACKETS':([23,56,126,158,],[96,96,96,166,]),'L_QBRACKET':([23,56,75,126,162,],[98,98,98,98,98,]),'LESS':([24,25,26,27,29,30,31,32,33,34,35,36,37,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,92,93,96,97,118,123,126,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,153,154,155,160,162,167,169,170,],[-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,101,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-112,-35,101,-105,-41,101,101,-42,101,101,-34,-73,-74,-75,-76,-77,-78,101,-86,-88,-90,-93,-94,-53,-54,101,101,101,-104,-44,101,-43,-89,]),'GREATER':([24,25,26,27,29,30,31,32,33,34,35,36,37,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,92,93,96,97,118,123,126,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,153,154,155,160,162,167,169,170,],[-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,102,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-112,-35,102,-105,-41,102,102,-42,102,102,-34,-73,-74,-75,-76,-77,-78,102,-86,-88,-90,-93,-94,-53,-54,102,102,102,-104,-44,102,-43,-89,]),'EQ':([24,25,26,27,29,30,31,32,33,34,35,36,37,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,92,93,96,97,118,123,126,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,153,154,155,160,162,167,169,170,],[-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,103,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-112,-35,103,-105,-41,103,103,159,103,103,-34,-73,-74,-75,-76,-77,-78,103,-86,-88,-90,-93,-94,-53,-54,103,103,103,-104,-44,103,-43,-89,]),'NOTEQ':([24,25,26,27,29,30,31,32,33,34,35,36,37,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,92,93,96,97,118,123,126,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,153,154,155,160,162,167,169,170,],[-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,104,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-112,-35,104,-105,-41,104,104,-42,104,104,-34,-73,-74,-75,-76,-77,-78,104,-86,-88,-90,-93,-94,-53,-54,104,104,104,-104,-44,104,-43,-89,]),'PLUS':([24,25,26,27,29,30,31,32,33,34,35,36,37,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,92,93,96,97,118,123,126,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,153,154,155,160,162,167,169,170,],[-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,105,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-112,-35,105,-105,-41,105,105,-42,105,105,-34,105,105,105,105,-77,-78,105,-86,-88,-90,-93,-94,-53,-54,105,105,105,-104,-44,105,-43,-89,]),'MINUS':([24,25,26,27,29,30,31,32,33,34,35,36,37,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,92,93,96,97,118,123,126,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,153,154,155,160,162,167,169,170,],[-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,106,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-112,-35,106,-105,-41,106,106,-42,106,106,-34,106,106,106,106,-77,-78,106,-86,-88,-90,-93,-94,-53,-54,106,106,106,-104,-44,106,-43,-89,]),'TO':([24,25,26,27,29,30,31,32,33,34,35,36,37,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,92,93,96,97,118,123,126,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,153,154,155,160,162,167,169,170,],[-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,107,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-112,-35,107,-105,-41,107,107,-42,107,107,-34,-73,-74,-75,-76,-77,-78,-87,-86,-88,-90,-93,-94,-53,-54,107,107,107,-104,-44,107,-43,-89,]),'THEN':([24,25,26,27,29,30,31,32,33,34,35,36,37,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,92,93,96,97,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,160,162,169,170,],[-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-112,-35,124,-105,-41,-34,-73,-74,-75,-76,-77,-78,-87,-86,-88,-90,-93,-94,-53,-54,-104,-44,-43,-89,]),'COMMA':([24,25,26,27,29,30,31,32,33,34,35,36,37,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,73,74,75,92,96,97,118,126,127,128,129,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,160,162,167,168,169,170,172,],[-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-112,115,116,-42,-35,-105,-41,-40,-42,161,-108,-109,-110,-34,-73,-74,-75,-76,-77,-78,-87,-86,-88,-90,-93,-94,-53,-54,-104,-44,-111,-107,-43,-89,161,]),'RBRACKET':([24,25,26,27,29,30,31,32,33,34,35,36,37,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,92,96,97,126,127,128,129,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,160,162,167,168,169,170,172,],[-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-112,-35,-105,-41,-42,160,-108,-109,-110,-34,-73,-74,-75,-76,-77,-78,-87,-86,-88,-90,-93,-94,-53,-54,-104,-44,-111,-107,-43,-89,174,]),'R_QBRACKET':([24,25,26,27,29,30,31,32,33,34,35,36,37,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,92,96,97,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,160,162,169,170,],[-113,-31,-32,-33,-98,-95,-96,-97,-99,-100,-101,-102,-103,-45,-46,-47,-48,-49,-50,-51,-52,-42,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-112,-35,-105,-41,162,-34,-73,-74,-75,-76,-77,-78,-87,-86,-88,-90,-93,-94,-53,-54,-104,-44,-43,-89,]),'POP':([48,56,97,126,162,169,],[108,-42,-41,-42,-44,-43,]),'FRONT':([79,108,],[120,144,]),'CONTINUE':([95,165,],[129,129,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,81,],[2,122,]),'statement':([0,2,81,122,],[3,38,3,38,]),'declaration':([0,2,18,81,122,124,164,166,174,],[4,4,83,4,4,83,83,83,83,]),'comment':([0,2,81,122,],[5,5,5,5,]),'assignment':([0,2,15,18,81,115,116,122,124,164,166,174,],[6,6,74,84,6,74,74,6,84,84,84,84,]),'while':([0,2,18,81,122,124,164,166,174,],[7,7,85,7,7,85,85,85,85,]),'if':([0,2,18,81,122,124,164,166,174,],[8,8,86,8,8,86,86,86,86,]),'command':([0,2,18,81,122,124,164,166,174,],[9,9,87,9,9,87,87,87,87,]),'function':([0,2,18,81,122,124,164,166,174,],[10,10,88,10,10,88,88,88,88,]),'call':([0,2,12,18,19,78,81,90,95,98,101,102,103,104,105,106,107,119,120,121,122,124,159,161,164,165,166,174,],[11,11,55,89,55,55,11,55,55,55,55,55,55,55,55,55,55,55,55,55,11,89,55,55,89,55,89,89,]),'empty':([0,2,18,81,122,124,164,166,174,],[13,13,91,13,13,91,91,91,91,]),'errors':([0,2,18,81,94,99,107,122,124,163,164,166,174,],[14,14,92,14,92,92,92,14,92,92,92,92,92,]),'type':([0,2,18,81,94,99,107,122,124,163,164,166,174,],[15,15,15,15,125,132,140,15,15,132,15,15,15,]),'variable':([0,2,12,15,18,19,78,81,90,95,98,101,102,103,104,105,106,107,115,116,119,120,121,122,124,159,161,164,165,166,174,],[17,17,48,73,17,48,48,17,48,48,48,48,48,48,48,48,48,48,73,73,48,48,48,17,17,48,48,17,48,17,17,]),'vector_command':([0,2,18,81,122,124,164,166,174,],[20,20,20,20,20,20,20,20,20,]),'robot_command':([0,2,12,18,19,78,81,90,95,98,101,102,103,104,105,106,107,119,120,121,122,124,159,161,164,165,166,174,],[21,21,52,21,52,52,21,52,52,52,52,52,52,52,52,52,52,52,52,52,21,21,52,52,21,52,21,21,]),'expression':([12,19,78,90,95,98,101,102,103,104,105,106,107,119,120,121,159,161,165,],[47,93,118,123,130,131,133,134,135,136,137,138,139,153,154,155,167,130,130,]),'const':([12,19,78,90,95,98,101,102,103,104,105,106,107,119,120,121,159,161,165,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'qstring':([12,19,78,90,95,98,101,102,103,104,105,106,107,119,120,121,159,161,165,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'math_expression':([12,19,78,90,95,98,101,102,103,104,105,106,107,119,120,121,159,161,165,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'converting_command':([12,19,78,90,95,98,101,102,103,104,105,106,107,119,120,121,159,161,165,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'vector_pop':([12,19,78,90,95,98,101,102,103,104,105,106,107,119,120,121,159,161,165,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'variables':([15,115,116,],[72,151,152,]),'any':([16,],[76,]),'statements_group':([18,124,164,166,174,],[80,157,171,173,175,]),'inner_statement':([18,124,164,166,174,],[82,82,82,82,82,]),'indexing':([23,56,75,126,162,],[97,97,97,97,169,]),'string':([67,68,110,111,112,113,],[109,114,146,147,148,149,]),'parameters':([95,165,],[127,172,]),'parameter':([95,161,165,],[128,168,128,]),'vector_of':([107,163,],[141,170,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','parser.py',29),
  ('statements_group -> BEGIN statements END','statements_group',3,'p_statements_group','parser.py',34),
  ('statements_group -> inner_statement','statements_group',1,'p_statements_group','parser.py',35),
  ('inner_statement -> declaration','inner_statement',1,'p_inner_statement','parser.py',43),
  ('inner_statement -> assignment','inner_statement',1,'p_inner_statement','parser.py',44),
  ('inner_statement -> while','inner_statement',1,'p_inner_statement','parser.py',45),
  ('inner_statement -> if','inner_statement',1,'p_inner_statement','parser.py',46),
  ('inner_statement -> command','inner_statement',1,'p_inner_statement','parser.py',47),
  ('inner_statement -> function','inner_statement',1,'p_inner_statement','parser.py',48),
  ('inner_statement -> call','inner_statement',1,'p_inner_statement','parser.py',49),
  ('inner_statement -> RETURN expression','inner_statement',2,'p_inner_statement','parser.py',50),
  ('inner_statement -> empty','inner_statement',1,'p_inner_statement','parser.py',51),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',60),
  ('statements -> statement','statements',1,'p_statements','parser.py',61),
  ('statement -> declaration NEWLINE','statement',2,'p_statement','parser.py',69),
  ('statement -> comment NEWLINE','statement',2,'p_statement','parser.py',70),
  ('statement -> assignment NEWLINE','statement',2,'p_statement','parser.py',71),
  ('statement -> while NEWLINE','statement',2,'p_statement','parser.py',72),
  ('statement -> if NEWLINE','statement',2,'p_statement','parser.py',73),
  ('statement -> command NEWLINE','statement',2,'p_statement','parser.py',74),
  ('statement -> function NEWLINE','statement',2,'p_statement','parser.py',75),
  ('statement -> call NEWLINE','statement',2,'p_statement','parser.py',76),
  ('statement -> RETURN expression NEWLINE','statement',3,'p_statement','parser.py',77),
  ('statement -> empty NEWLINE','statement',2,'p_statement','parser.py',78),
  ('statement -> errors NEWLINE','statement',2,'p_statement_error','parser.py',87),
  ('statement -> errors','statement',1,'p_statement_error_no_nl','parser.py',93),
  ('declaration -> type variables','declaration',2,'p_declaration','parser.py',99),
  ('comment -> COMMENT any','comment',2,'p_comment','parser.py',104),
  ('any -> any VARIABLE','any',2,'p_any','parser.py',109),
  ('any -> VARIABLE','any',1,'p_any','parser.py',110),
  ('type -> INTEGER','type',1,'p_type','parser.py',118),
  ('type -> STRING','type',1,'p_type','parser.py',119),
  ('type -> BOOL','type',1,'p_type','parser.py',120),
  ('type -> VECTOR OF type','type',3,'p_type','parser.py',121),
  ('type -> errors','type',1,'p_type_error','parser.py',131),
  ('variables -> variable COMMA variables','variables',3,'p_variables','parser.py',137),
  ('variables -> assignment COMMA variables','variables',3,'p_variables','parser.py',138),
  ('variables -> variable','variables',1,'p_variables','parser.py',139),
  ('variables -> assignment','variables',1,'p_variables','parser.py',140),
  ('assignment -> variable ASSIGNMENT expression','assignment',3,'p_assignment','parser.py',148),
  ('variable -> VARIABLE indexing','variable',2,'p_variable','parser.py',153),
  ('variable -> VARIABLE','variable',1,'p_variable','parser.py',154),
  ('indexing -> L_QBRACKET expression R_QBRACKET indexing','indexing',4,'p_indexing','parser.py',162),
  ('indexing -> L_QBRACKET expression R_QBRACKET','indexing',3,'p_indexing','parser.py',163),
  ('expression -> variable','expression',1,'p_expression','parser.py',171),
  ('expression -> const','expression',1,'p_expression','parser.py',172),
  ('expression -> qstring','expression',1,'p_expression','parser.py',173),
  ('expression -> math_expression','expression',1,'p_expression','parser.py',174),
  ('expression -> robot_command','expression',1,'p_expression','parser.py',175),
  ('expression -> converting_command','expression',1,'p_expression','parser.py',176),
  ('expression -> vector_pop','expression',1,'p_expression','parser.py',177),
  ('expression -> call','expression',1,'p_expression','parser.py',178),
  ('qstring -> DOUBLE_QUOTE string DOUBLE_QUOTE','qstring',3,'p_qstring','parser.py',183),
  ('qstring -> QUOTE string QUOTE','qstring',3,'p_qstring','parser.py',184),
  ('string -> VARIABLE string','string',2,'p_string','parser.py',189),
  ('string -> DECIMAL string','string',2,'p_string','parser.py',190),
  ('string -> FALSE string','string',2,'p_string','parser.py',191),
  ('string -> TRUE string','string',2,'p_string','parser.py',192),
  ('string -> FALSE','string',1,'p_string','parser.py',193),
  ('string -> TRUE','string',1,'p_string','parser.py',194),
  ('string -> DECIMAL','string',1,'p_string','parser.py',195),
  ('string -> VARIABLE','string',1,'p_string','parser.py',196),
  ('const -> TRUE','const',1,'p_const','parser.py',207),
  ('const -> FALSE','const',1,'p_const','parser.py',208),
  ('const -> UNDEFINED','const',1,'p_const','parser.py',209),
  ('const -> DECIMAL','const',1,'p_const','parser.py',210),
  ('const -> EXIT','const',1,'p_const','parser.py',211),
  ('const -> WOOD','const',1,'p_const','parser.py',212),
  ('const -> STEEL','const',1,'p_const','parser.py',213),
  ('const -> GLASS','const',1,'p_const','parser.py',214),
  ('const -> CONCRETE','const',1,'p_const','parser.py',215),
  ('const -> PLASTIC','const',1,'p_const','parser.py',216),
  ('math_expression -> expression LESS expression','math_expression',3,'p_math_expression','parser.py',221),
  ('math_expression -> expression GREATER expression','math_expression',3,'p_math_expression','parser.py',222),
  ('math_expression -> expression EQ expression','math_expression',3,'p_math_expression','parser.py',223),
  ('math_expression -> expression NOTEQ expression','math_expression',3,'p_math_expression','parser.py',224),
  ('math_expression -> expression PLUS expression','math_expression',3,'p_math_expression','parser.py',225),
  ('math_expression -> expression MINUS expression','math_expression',3,'p_math_expression','parser.py',226),
  ('while -> DO statements_group UNTIL expression','while',4,'p_while','parser.py',231),
  ('if -> IF expression THEN statements_group','if',4,'p_if','parser.py',236),
  ('if -> IF expression THEN statements_group ELSE statements_group','if',6,'p_if','parser.py',237),
  ('function -> FUNCTION OF type VARIABLE LBRACKET parameters RBRACKET statements_group','function',8,'p_function','parser.py',245),
  ('function -> FUNCTION OF type VARIABLE BRACKETS statements_group','function',6,'p_function','parser.py',246),
  ('command -> vector_command','command',1,'p_command','parser.py',255),
  ('command -> robot_command','command',1,'p_command','parser.py',256),
  ('converting_command -> expression TO type','converting_command',3,'p_converting_command','parser.py',261),
  ('converting_command -> expression TO expression','converting_command',3,'p_converting_command','parser.py',262),
  ('converting_command -> expression TO vector_of','converting_command',3,'p_converting_command','parser.py',263),
  ('vector_of -> VECTOR OF vector_of','vector_of',3,'p_vector_of','parser.py',268),
  ('vector_of -> VECTOR','vector_of',1,'p_vector_of','parser.py',269),
  ('vector_command -> variable PUSH BACK expression','vector_command',4,'p_vector_command','parser.py',277),
  ('vector_command -> variable PUSH FRONT expression','vector_command',4,'p_vector_command','parser.py',278),
  ('vector_pop -> variable POP BACK','vector_pop',3,'p_vector_command_pop','parser.py',283),
  ('vector_pop -> variable POP FRONT','vector_pop',3,'p_vector_command_pop','parser.py',284),
  ('robot_command -> LEFT','robot_command',1,'p_robot_command','parser.py',289),
  ('robot_command -> RIGHT','robot_command',1,'p_robot_command','parser.py',290),
  ('robot_command -> FORWARD','robot_command',1,'p_robot_command','parser.py',291),
  ('robot_command -> BACK','robot_command',1,'p_robot_command','parser.py',292),
  ('robot_command -> ROTATE_RIGHT','robot_command',1,'p_robot_command','parser.py',293),
  ('robot_command -> ROTATE_LEFT','robot_command',1,'p_robot_command','parser.py',294),
  ('robot_command -> LMS','robot_command',1,'p_robot_command','parser.py',295),
  ('robot_command -> REFLECT','robot_command',1,'p_robot_command','parser.py',296),
  ('robot_command -> DRILL','robot_command',1,'p_robot_command','parser.py',297),
  ('call -> VARIABLE LBRACKET parameters RBRACKET','call',4,'p_call','parser.py',302),
  ('call -> VARIABLE BRACKETS','call',2,'p_call','parser.py',303),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',311),
  ('parameters -> parameters COMMA parameter','parameters',3,'p_parameters','parser.py',316),
  ('parameters -> parameter','parameters',1,'p_parameters','parser.py',317),
  ('parameters -> CONTINUE','parameters',1,'p_parameters','parser.py',318),
  ('parameter -> expression','parameter',1,'p_parameter','parser.py',326),
  ('parameter -> VARIABLE EQ expression','parameter',3,'p_parameter','parser.py',327),
  ('errors -> errors error','errors',2,'p_errors','parser.py',335),
  ('errors -> error','errors',1,'p_errors','parser.py',336),
]
