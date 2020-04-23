
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGNMENT BACK BEGIN BOOL BRACKETS COMMA COMMENT CONCRETE CONTINUE DECIMAL DO DOUBLE_QUOTE DRILL ELSE END EQ EXIT FALSE FORWARD FRONT FUNCTION GLASS GREATER IF INTEGER LBRACKET LEFT LESS LMS L_QBRACKET MINUS NEWLINE NOTEQ OF PLASTIC PLUS POP PUSH QUOTE RBRACKET REFLECT RETURN RIGHT ROTATE_LEFT ROTATE_RIGHT R_QBRACKET STEEL STRING THEN TO TRUE UNDEFINED UNTIL VARIABLE VECTOR WOODapplication : statementsstatements_group : BEGIN statements END\n                            | inner_statementinner_statement : declaration\n                     | assignment\n                     | while\n                     | if\n                     | command\n                     | function\n                     | call\n                     | RETURN expression\n                     | emptystatements : statements statement\n                      | statementstatement : declaration NEWLINE\n                     | comment NEWLINE\n                     | assignment NEWLINE\n                     | while NEWLINE\n                     | if NEWLINE\n                     | command NEWLINE\n                     | function NEWLINE\n                     | call NEWLINE\n                     | RETURN expression NEWLINE\n                     | empty NEWLINEdeclaration : type variablescomment : COMMENT anyany : any VARIABLE\n               | VARIABLEtype : INTEGER\n                | STRING\n                | BOOL\n                | VECTOR OF type\n        variables : variable COMMA variables\n                | assignment COMMA variables\n                | variable\n                | assignmentassignment : variable ASSIGNMENT expressionvariable : VARIABLE L_QBRACKET expression R_QBRACKET\n                    | VARIABLEexpression : variable\n                      | const\n                      | qstring\n                      | math_expression\n                      | callqstring : DOUBLE_QUOTE string DOUBLE_QUOTE\n                   | QUOTE string QUOTEstring : string VARIABLE\n                   | VARIABLEconst : TRUE\n                 | FALSE\n                 | UNDEFINED\n                 | DECIMAL\n                 | EXIT\n                 | WOOD\n                 | STEEL\n                 | GLASS\n                 | CONCRETE\n                 | PLASTICmath_expression : expression PLUS expression\n                           | expression MINUS expression\n                           | MINUS expression\n                           | expression LESS expression\n                           | expression GREATER expression\n                           | expression EQ expression\n                           | expression NOTEQ expressionwhile : DO statements_group UNTIL expressionif : IF expression THEN statements_group\n              | IF expression THEN statements_group ELSE statements_groupfunction : FUNCTION OF type VARIABLE LBRACKET parameters RBRACKET statements_group\n                    | FUNCTION OF type VARIABLE BRACKETS statements_groupcommand : vector_command\n                   | robot_command\n                   | converting_commandconverting_command : expression TO type\n                              | expression TO expressionvector_command : VARIABLE PUSH BACK expression\n                          | VARIABLE POP BACK\n                          | VARIABLE PUSH FRONT expression\n                          | VARIABLE POP FRONTrobot_command : LEFT\n                    | RIGHT\n                    | FORWARD\n                    | BACK\n                    | ROTATE_RIGHT\n                    | ROTATE_LEFT\n                    | LMS\n                    | REFLECT\n                    | DRILLcall : VARIABLE LBRACKET parameters RBRACKET\n                | VARIABLE BRACKETSempty : parameters : parameters COMMA parameter\n                      | parameter\n                      | parameters CONTINUEparameter : expression\n                     | VARIABLE EQ expression'
    
_lr_action_items = {'RETURN':([0,2,3,18,54,55,56,57,58,59,60,61,62,74,83,106,120,122,150,152,158,],[12,12,-14,92,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,12,-23,12,92,92,92,92,]),'COMMENT':([0,2,3,54,55,56,57,58,59,60,61,62,74,83,106,120,],[16,16,-14,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,16,-23,16,]),'DO':([0,2,3,18,54,55,56,57,58,59,60,61,62,74,83,106,120,122,150,152,158,],[18,18,-14,18,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,18,-23,18,18,18,18,18,]),'IF':([0,2,3,18,54,55,56,57,58,59,60,61,62,74,83,106,120,122,150,152,158,],[19,19,-14,19,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,19,-23,19,19,19,19,19,]),'FUNCTION':([0,2,3,18,54,55,56,57,58,59,60,61,62,74,83,106,120,122,150,152,158,],[23,23,-14,23,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,23,-23,23,23,23,23,23,]),'VARIABLE':([0,2,3,12,15,16,18,19,25,26,27,51,52,53,54,55,56,57,58,59,60,61,62,67,68,69,70,71,72,73,74,79,80,81,83,92,96,98,102,103,104,106,115,116,117,119,120,122,123,129,130,133,135,143,145,150,151,152,158,],[24,24,-14,66,78,80,24,66,-29,-30,-31,103,103,66,-13,-15,-16,-17,-18,-19,-20,-21,-22,66,66,66,66,66,66,66,-24,117,-28,66,24,66,124,66,135,-48,135,-23,78,78,-27,66,24,24,142,66,66,-32,-47,66,124,24,124,24,24,]),'NEWLINE':([0,2,3,4,5,6,7,8,9,10,11,14,20,21,22,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,55,56,57,58,59,60,61,62,63,64,65,66,74,75,76,77,78,79,80,83,84,85,86,87,88,89,90,91,93,97,105,106,107,108,109,110,111,112,113,114,117,118,120,121,122,131,132,133,134,136,137,138,139,140,141,144,147,148,149,150,152,155,157,158,159,],[-91,-91,-14,55,56,57,58,59,60,61,62,74,-71,-72,-73,-29,-30,-31,-83,-80,-81,-82,-84,-85,-86,-87,-88,-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-13,-15,-16,-17,-18,-19,-20,-21,-22,106,-40,-44,-39,-24,-25,-35,-36,-39,-26,-28,-91,-3,-4,-5,-6,-7,-8,-9,-10,-12,-90,-61,-23,-75,-74,-59,-60,-62,-63,-64,-65,-27,-37,-91,-11,-91,-77,-79,-32,-45,-46,-33,-34,-66,-2,-67,-89,-38,-76,-78,-91,-91,-68,-70,-91,-69,]),'INTEGER':([0,2,3,18,54,55,56,57,58,59,60,61,62,67,74,83,95,101,106,120,122,150,152,158,],[25,25,-14,25,-13,-15,-16,-17,-18,-19,-20,-21,-22,25,-24,25,25,25,-23,25,25,25,25,25,]),'STRING':([0,2,3,18,54,55,56,57,58,59,60,61,62,67,74,83,95,101,106,120,122,150,152,158,],[26,26,-14,26,-13,-15,-16,-17,-18,-19,-20,-21,-22,26,-24,26,26,26,-23,26,26,26,26,26,]),'BOOL':([0,2,3,18,54,55,56,57,58,59,60,61,62,67,74,83,95,101,106,120,122,150,152,158,],[27,27,-14,27,-13,-15,-16,-17,-18,-19,-20,-21,-22,27,-24,27,27,27,-23,27,27,27,27,27,]),'VECTOR':([0,2,3,18,54,55,56,57,58,59,60,61,62,67,74,83,95,101,106,120,122,150,152,158,],[28,28,-14,28,-13,-15,-16,-17,-18,-19,-20,-21,-22,28,-24,28,28,28,-23,28,28,28,28,28,]),'LEFT':([0,2,3,18,54,55,56,57,58,59,60,61,62,74,83,106,120,122,150,152,158,],[30,30,-14,30,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,30,-23,30,30,30,30,30,]),'RIGHT':([0,2,3,18,54,55,56,57,58,59,60,61,62,74,83,106,120,122,150,152,158,],[31,31,-14,31,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,31,-23,31,31,31,31,31,]),'FORWARD':([0,2,3,18,54,55,56,57,58,59,60,61,62,74,83,106,120,122,150,152,158,],[32,32,-14,32,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,32,-23,32,32,32,32,32,]),'BACK':([0,2,3,18,54,55,56,57,58,59,60,61,62,74,83,99,100,106,120,122,150,152,158,],[29,29,-14,29,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,29,129,131,-23,29,29,29,29,29,]),'ROTATE_RIGHT':([0,2,3,18,54,55,56,57,58,59,60,61,62,74,83,106,120,122,150,152,158,],[33,33,-14,33,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,33,-23,33,33,33,33,33,]),'ROTATE_LEFT':([0,2,3,18,54,55,56,57,58,59,60,61,62,74,83,106,120,122,150,152,158,],[34,34,-14,34,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,34,-23,34,34,34,34,34,]),'LMS':([0,2,3,18,54,55,56,57,58,59,60,61,62,74,83,106,120,122,150,152,158,],[35,35,-14,35,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,35,-23,35,35,35,35,35,]),'REFLECT':([0,2,3,18,54,55,56,57,58,59,60,61,62,74,83,106,120,122,150,152,158,],[36,36,-14,36,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,36,-23,36,36,36,36,36,]),'DRILL':([0,2,3,18,54,55,56,57,58,59,60,61,62,74,83,106,120,122,150,152,158,],[37,37,-14,37,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,37,-23,37,37,37,37,37,]),'TRUE':([0,2,3,12,18,19,53,54,55,56,57,58,59,60,61,62,67,68,69,70,71,72,73,74,81,83,92,96,98,106,119,120,122,129,130,143,145,150,151,152,158,],[41,41,-14,41,41,41,41,-13,-15,-16,-17,-18,-19,-20,-21,-22,41,41,41,41,41,41,41,-24,41,41,41,41,41,-23,41,41,41,41,41,41,41,41,41,41,41,]),'FALSE':([0,2,3,12,18,19,53,54,55,56,57,58,59,60,61,62,67,68,69,70,71,72,73,74,81,83,92,96,98,106,119,120,122,129,130,143,145,150,151,152,158,],[42,42,-14,42,42,42,42,-13,-15,-16,-17,-18,-19,-20,-21,-22,42,42,42,42,42,42,42,-24,42,42,42,42,42,-23,42,42,42,42,42,42,42,42,42,42,42,]),'UNDEFINED':([0,2,3,12,18,19,53,54,55,56,57,58,59,60,61,62,67,68,69,70,71,72,73,74,81,83,92,96,98,106,119,120,122,129,130,143,145,150,151,152,158,],[43,43,-14,43,43,43,43,-13,-15,-16,-17,-18,-19,-20,-21,-22,43,43,43,43,43,43,43,-24,43,43,43,43,43,-23,43,43,43,43,43,43,43,43,43,43,43,]),'DECIMAL':([0,2,3,12,18,19,53,54,55,56,57,58,59,60,61,62,67,68,69,70,71,72,73,74,81,83,92,96,98,106,119,120,122,129,130,143,145,150,151,152,158,],[44,44,-14,44,44,44,44,-13,-15,-16,-17,-18,-19,-20,-21,-22,44,44,44,44,44,44,44,-24,44,44,44,44,44,-23,44,44,44,44,44,44,44,44,44,44,44,]),'EXIT':([0,2,3,12,18,19,53,54,55,56,57,58,59,60,61,62,67,68,69,70,71,72,73,74,81,83,92,96,98,106,119,120,122,129,130,143,145,150,151,152,158,],[45,45,-14,45,45,45,45,-13,-15,-16,-17,-18,-19,-20,-21,-22,45,45,45,45,45,45,45,-24,45,45,45,45,45,-23,45,45,45,45,45,45,45,45,45,45,45,]),'WOOD':([0,2,3,12,18,19,53,54,55,56,57,58,59,60,61,62,67,68,69,70,71,72,73,74,81,83,92,96,98,106,119,120,122,129,130,143,145,150,151,152,158,],[46,46,-14,46,46,46,46,-13,-15,-16,-17,-18,-19,-20,-21,-22,46,46,46,46,46,46,46,-24,46,46,46,46,46,-23,46,46,46,46,46,46,46,46,46,46,46,]),'STEEL':([0,2,3,12,18,19,53,54,55,56,57,58,59,60,61,62,67,68,69,70,71,72,73,74,81,83,92,96,98,106,119,120,122,129,130,143,145,150,151,152,158,],[47,47,-14,47,47,47,47,-13,-15,-16,-17,-18,-19,-20,-21,-22,47,47,47,47,47,47,47,-24,47,47,47,47,47,-23,47,47,47,47,47,47,47,47,47,47,47,]),'GLASS':([0,2,3,12,18,19,53,54,55,56,57,58,59,60,61,62,67,68,69,70,71,72,73,74,81,83,92,96,98,106,119,120,122,129,130,143,145,150,151,152,158,],[48,48,-14,48,48,48,48,-13,-15,-16,-17,-18,-19,-20,-21,-22,48,48,48,48,48,48,48,-24,48,48,48,48,48,-23,48,48,48,48,48,48,48,48,48,48,48,]),'CONCRETE':([0,2,3,12,18,19,53,54,55,56,57,58,59,60,61,62,67,68,69,70,71,72,73,74,81,83,92,96,98,106,119,120,122,129,130,143,145,150,151,152,158,],[49,49,-14,49,49,49,49,-13,-15,-16,-17,-18,-19,-20,-21,-22,49,49,49,49,49,49,49,-24,49,49,49,49,49,-23,49,49,49,49,49,49,49,49,49,49,49,]),'PLASTIC':([0,2,3,12,18,19,53,54,55,56,57,58,59,60,61,62,67,68,69,70,71,72,73,74,81,83,92,96,98,106,119,120,122,129,130,143,145,150,151,152,158,],[50,50,-14,50,50,50,50,-13,-15,-16,-17,-18,-19,-20,-21,-22,50,50,50,50,50,50,50,-24,50,50,50,50,50,-23,50,50,50,50,50,50,50,50,50,50,50,]),'DOUBLE_QUOTE':([0,2,3,12,18,19,53,54,55,56,57,58,59,60,61,62,67,68,69,70,71,72,73,74,81,83,92,96,98,102,103,106,119,120,122,129,130,135,143,145,150,151,152,158,],[51,51,-14,51,51,51,51,-13,-15,-16,-17,-18,-19,-20,-21,-22,51,51,51,51,51,51,51,-24,51,51,51,51,51,134,-48,-23,51,51,51,51,51,-47,51,51,51,51,51,51,]),'QUOTE':([0,2,3,12,18,19,53,54,55,56,57,58,59,60,61,62,67,68,69,70,71,72,73,74,81,83,92,96,98,103,104,106,119,120,122,129,130,135,143,145,150,151,152,158,],[52,52,-14,52,52,52,52,-13,-15,-16,-17,-18,-19,-20,-21,-22,52,52,52,52,52,52,52,-24,52,52,52,52,52,-48,136,-23,52,52,52,52,52,-47,52,52,52,52,52,52,]),'MINUS':([0,2,3,11,12,13,17,18,19,24,38,39,40,41,42,43,44,45,46,47,48,49,50,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,81,83,91,92,94,96,97,98,105,106,107,109,110,111,112,113,114,118,119,120,121,122,124,127,128,129,130,134,136,139,143,144,145,147,148,149,150,151,152,153,158,],[53,53,-14,-44,53,69,-40,53,53,-39,-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,53,-13,-15,-16,-17,-18,-19,-20,-21,-22,69,-40,-44,-39,53,53,53,53,53,53,53,-24,53,53,-44,53,69,53,-90,53,69,-23,69,69,69,69,69,69,69,69,53,53,69,53,-39,69,69,53,53,-45,-46,69,53,-89,53,-38,69,69,53,53,53,69,53,]),'$end':([1,2,3,54,55,56,57,58,59,60,61,62,74,106,],[0,-1,-14,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-23,]),'END':([3,54,55,56,57,58,59,60,61,62,74,106,120,],[-14,-13,-15,-16,-17,-18,-19,-20,-21,-22,-24,-23,140,]),'TO':([11,13,17,24,38,39,40,41,42,43,44,45,46,47,48,49,50,64,65,66,91,97,105,109,110,111,112,113,114,134,136,144,147,],[-44,67,-40,-39,-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-40,-44,-39,-44,-90,-61,-59,-60,-62,-63,-64,-65,-45,-46,-89,-38,]),'PLUS':([11,13,17,24,38,39,40,41,42,43,44,45,46,47,48,49,50,63,64,65,66,91,94,97,105,107,109,110,111,112,113,114,118,121,124,127,128,134,136,139,144,147,148,149,153,],[-44,68,-40,-39,-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,68,-40,-44,-39,-44,68,-90,68,68,68,68,68,68,68,68,68,68,-39,68,68,-45,-46,68,-89,-38,68,68,68,]),'LESS':([11,13,17,24,38,39,40,41,42,43,44,45,46,47,48,49,50,63,64,65,66,91,94,97,105,107,109,110,111,112,113,114,118,121,124,127,128,134,136,139,144,147,148,149,153,],[-44,70,-40,-39,-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,70,-40,-44,-39,-44,70,-90,70,70,70,70,70,70,70,70,70,70,-39,70,70,-45,-46,70,-89,-38,70,70,70,]),'GREATER':([11,13,17,24,38,39,40,41,42,43,44,45,46,47,48,49,50,63,64,65,66,91,94,97,105,107,109,110,111,112,113,114,118,121,124,127,128,134,136,139,144,147,148,149,153,],[-44,71,-40,-39,-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,71,-40,-44,-39,-44,71,-90,71,71,71,71,71,71,71,71,71,71,-39,71,71,-45,-46,71,-89,-38,71,71,71,]),'EQ':([11,13,17,24,38,39,40,41,42,43,44,45,46,47,48,49,50,63,64,65,66,91,94,97,105,107,109,110,111,112,113,114,118,121,124,127,128,134,136,139,144,147,148,149,153,],[-44,72,-40,-39,-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,72,-40,-44,-39,-44,72,-90,72,72,72,72,72,72,72,72,72,72,143,72,72,-45,-46,72,-89,-38,72,72,72,]),'NOTEQ':([11,13,17,24,38,39,40,41,42,43,44,45,46,47,48,49,50,63,64,65,66,91,94,97,105,107,109,110,111,112,113,114,118,121,124,127,128,134,136,139,144,147,148,149,153,],[-44,73,-40,-39,-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,73,-40,-44,-39,-44,73,-90,73,73,73,73,73,73,73,73,73,73,-39,73,73,-45,-46,73,-89,-38,73,73,73,]),'ASSIGNMENT':([17,24,76,78,147,],[81,-39,81,-39,-38,]),'BEGIN':([18,122,150,152,158,],[83,83,83,83,83,]),'UNTIL':([18,20,21,22,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,64,65,66,75,76,77,78,82,84,85,86,87,88,89,90,91,93,97,105,107,108,109,110,111,112,113,114,118,121,122,131,132,133,134,136,137,138,139,140,141,144,147,148,149,150,152,155,157,158,159,],[-91,-71,-72,-73,-29,-30,-31,-83,-80,-81,-82,-84,-85,-86,-87,-88,-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-40,-44,-39,-25,-35,-36,-39,119,-3,-4,-5,-6,-7,-8,-9,-10,-12,-90,-61,-75,-74,-59,-60,-62,-63,-64,-65,-37,-11,-91,-77,-79,-32,-45,-46,-33,-34,-66,-2,-67,-89,-38,-76,-78,-91,-91,-68,-70,-91,-69,]),'ELSE':([20,21,22,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,64,65,66,75,76,77,78,84,85,86,87,88,89,90,91,93,97,105,107,108,109,110,111,112,113,114,118,121,122,131,132,133,134,136,137,138,139,140,141,144,147,148,149,150,152,155,157,158,159,],[-71,-72,-73,-29,-30,-31,-83,-80,-81,-82,-84,-85,-86,-87,-88,-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-40,-44,-39,-25,-35,-36,-39,-3,-4,-5,-6,-7,-8,-9,-10,-12,-90,-61,-75,-74,-59,-60,-62,-63,-64,-65,-37,-11,-91,-77,-79,-32,-45,-46,-33,-34,-66,-2,150,-89,-38,-76,-78,-91,-91,-68,-70,-91,-69,]),'OF':([23,28,],[95,101,]),'LBRACKET':([24,66,124,142,],[96,96,96,151,]),'BRACKETS':([24,66,124,142,],[97,97,97,152,]),'L_QBRACKET':([24,66,78,124,],[98,98,98,98,]),'PUSH':([24,],[99,]),'POP':([24,],[100,]),'THEN':([38,39,40,41,42,43,44,45,46,47,48,49,50,64,65,66,94,97,105,109,110,111,112,113,114,134,136,144,147,],[-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-40,-44,-39,122,-90,-61,-59,-60,-62,-63,-64,-65,-45,-46,-89,-38,]),'COMMA':([38,39,40,41,42,43,44,45,46,47,48,49,50,64,65,66,76,77,78,97,105,109,110,111,112,113,114,118,124,125,126,127,134,136,144,146,147,153,154,156,],[-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-40,-44,-39,115,116,-39,-90,-61,-59,-60,-62,-63,-64,-65,-37,-39,145,-93,-95,-45,-46,-89,-94,-38,-96,-92,145,]),'RBRACKET':([38,39,40,41,42,43,44,45,46,47,48,49,50,64,65,66,97,105,109,110,111,112,113,114,124,125,126,127,134,136,144,146,147,153,154,156,],[-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-40,-44,-39,-90,-61,-59,-60,-62,-63,-64,-65,-39,144,-93,-95,-45,-46,-89,-94,-38,-96,-92,158,]),'CONTINUE':([38,39,40,41,42,43,44,45,46,47,48,49,50,64,65,66,97,105,109,110,111,112,113,114,124,125,126,127,134,136,144,146,147,153,154,156,],[-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-40,-44,-39,-90,-61,-59,-60,-62,-63,-64,-65,-39,146,-93,-95,-45,-46,-89,-94,-38,-96,-92,146,]),'R_QBRACKET':([38,39,40,41,42,43,44,45,46,47,48,49,50,64,65,66,97,105,109,110,111,112,113,114,128,134,136,144,147,],[-41,-42,-43,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-40,-44,-39,-90,-61,-59,-60,-62,-63,-64,-65,147,-45,-46,-89,-38,]),'FRONT':([99,100,],[130,132,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'application':([0,],[1,]),'statements':([0,83,],[2,120,]),'statement':([0,2,83,120,],[3,54,3,54,]),'declaration':([0,2,18,83,120,122,150,152,158,],[4,4,85,4,4,85,85,85,85,]),'comment':([0,2,83,120,],[5,5,5,5,]),'assignment':([0,2,15,18,83,115,116,120,122,150,152,158,],[6,6,77,86,6,77,77,6,86,86,86,86,]),'while':([0,2,18,83,120,122,150,152,158,],[7,7,87,7,7,87,87,87,87,]),'if':([0,2,18,83,120,122,150,152,158,],[8,8,88,8,8,88,88,88,88,]),'command':([0,2,18,83,120,122,150,152,158,],[9,9,89,9,9,89,89,89,89,]),'function':([0,2,18,83,120,122,150,152,158,],[10,10,90,10,10,90,90,90,90,]),'call':([0,2,12,18,19,53,67,68,69,70,71,72,73,81,83,92,96,98,119,120,122,129,130,143,145,150,151,152,158,],[11,11,65,91,65,65,65,65,65,65,65,65,65,65,11,65,65,65,65,11,91,65,65,65,65,91,65,91,91,]),'expression':([0,2,12,18,19,53,67,68,69,70,71,72,73,81,83,92,96,98,119,120,122,129,130,143,145,150,151,152,158,],[13,13,63,13,94,105,107,109,110,111,112,113,114,118,13,121,127,128,139,13,13,148,149,153,127,13,127,13,13,]),'empty':([0,2,18,83,120,122,150,152,158,],[14,14,93,14,14,93,93,93,93,]),'type':([0,2,18,67,83,95,101,120,122,150,152,158,],[15,15,15,108,15,123,133,15,15,15,15,15,]),'variable':([0,2,12,15,18,19,53,67,68,69,70,71,72,73,81,83,92,96,98,115,116,119,120,122,129,130,143,145,150,151,152,158,],[17,17,64,76,17,64,64,64,64,64,64,64,64,64,64,17,64,64,64,76,76,64,17,17,64,64,64,64,17,64,17,17,]),'vector_command':([0,2,18,83,120,122,150,152,158,],[20,20,20,20,20,20,20,20,20,]),'robot_command':([0,2,18,83,120,122,150,152,158,],[21,21,21,21,21,21,21,21,21,]),'converting_command':([0,2,18,83,120,122,150,152,158,],[22,22,22,22,22,22,22,22,22,]),'const':([0,2,12,18,19,53,67,68,69,70,71,72,73,81,83,92,96,98,119,120,122,129,130,143,145,150,151,152,158,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'qstring':([0,2,12,18,19,53,67,68,69,70,71,72,73,81,83,92,96,98,119,120,122,129,130,143,145,150,151,152,158,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'math_expression':([0,2,12,18,19,53,67,68,69,70,71,72,73,81,83,92,96,98,119,120,122,129,130,143,145,150,151,152,158,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'variables':([15,115,116,],[75,137,138,]),'any':([16,],[79,]),'statements_group':([18,122,150,152,158,],[82,141,155,157,159,]),'inner_statement':([18,122,150,152,158,],[84,84,84,84,84,]),'string':([51,52,],[102,104,]),'parameters':([96,151,],[125,156,]),'parameter':([96,145,151,],[126,154,126,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> application","S'",1,None,None,None),
  ('application -> statements','application',1,'p_application','parser.py',29),
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
  ('declaration -> type variables','declaration',2,'p_declaration','parser.py',86),
  ('comment -> COMMENT any','comment',2,'p_comment','parser.py',91),
  ('any -> any VARIABLE','any',2,'p_any','parser.py',96),
  ('any -> VARIABLE','any',1,'p_any','parser.py',97),
  ('type -> INTEGER','type',1,'p_type','parser.py',105),
  ('type -> STRING','type',1,'p_type','parser.py',106),
  ('type -> BOOL','type',1,'p_type','parser.py',107),
  ('type -> VECTOR OF type','type',3,'p_type','parser.py',108),
  ('variables -> variable COMMA variables','variables',3,'p_variables','parser.py',117),
  ('variables -> assignment COMMA variables','variables',3,'p_variables','parser.py',118),
  ('variables -> variable','variables',1,'p_variables','parser.py',119),
  ('variables -> assignment','variables',1,'p_variables','parser.py',120),
  ('assignment -> variable ASSIGNMENT expression','assignment',3,'p_assignment','parser.py',128),
  ('variable -> VARIABLE L_QBRACKET expression R_QBRACKET','variable',4,'p_variable','parser.py',133),
  ('variable -> VARIABLE','variable',1,'p_variable','parser.py',134),
  ('expression -> variable','expression',1,'p_expression','parser.py',142),
  ('expression -> const','expression',1,'p_expression','parser.py',143),
  ('expression -> qstring','expression',1,'p_expression','parser.py',144),
  ('expression -> math_expression','expression',1,'p_expression','parser.py',145),
  ('expression -> call','expression',1,'p_expression','parser.py',146),
  ('qstring -> DOUBLE_QUOTE string DOUBLE_QUOTE','qstring',3,'p_qstring','parser.py',151),
  ('qstring -> QUOTE string QUOTE','qstring',3,'p_qstring','parser.py',152),
  ('string -> string VARIABLE','string',2,'p_string','parser.py',157),
  ('string -> VARIABLE','string',1,'p_string','parser.py',158),
  ('const -> TRUE','const',1,'p_const','parser.py',166),
  ('const -> FALSE','const',1,'p_const','parser.py',167),
  ('const -> UNDEFINED','const',1,'p_const','parser.py',168),
  ('const -> DECIMAL','const',1,'p_const','parser.py',169),
  ('const -> EXIT','const',1,'p_const','parser.py',170),
  ('const -> WOOD','const',1,'p_const','parser.py',171),
  ('const -> STEEL','const',1,'p_const','parser.py',172),
  ('const -> GLASS','const',1,'p_const','parser.py',173),
  ('const -> CONCRETE','const',1,'p_const','parser.py',174),
  ('const -> PLASTIC','const',1,'p_const','parser.py',175),
  ('math_expression -> expression PLUS expression','math_expression',3,'p_math_expression','parser.py',180),
  ('math_expression -> expression MINUS expression','math_expression',3,'p_math_expression','parser.py',181),
  ('math_expression -> MINUS expression','math_expression',2,'p_math_expression','parser.py',182),
  ('math_expression -> expression LESS expression','math_expression',3,'p_math_expression','parser.py',183),
  ('math_expression -> expression GREATER expression','math_expression',3,'p_math_expression','parser.py',184),
  ('math_expression -> expression EQ expression','math_expression',3,'p_math_expression','parser.py',185),
  ('math_expression -> expression NOTEQ expression','math_expression',3,'p_math_expression','parser.py',186),
  ('while -> DO statements_group UNTIL expression','while',4,'p_while','parser.py',194),
  ('if -> IF expression THEN statements_group','if',4,'p_if','parser.py',199),
  ('if -> IF expression THEN statements_group ELSE statements_group','if',6,'p_if','parser.py',200),
  ('function -> FUNCTION OF type VARIABLE LBRACKET parameters RBRACKET statements_group','function',8,'p_function','parser.py',208),
  ('function -> FUNCTION OF type VARIABLE BRACKETS statements_group','function',6,'p_function','parser.py',209),
  ('command -> vector_command','command',1,'p_command','parser.py',218),
  ('command -> robot_command','command',1,'p_command','parser.py',219),
  ('command -> converting_command','command',1,'p_command','parser.py',220),
  ('converting_command -> expression TO type','converting_command',3,'p_converting_command','parser.py',225),
  ('converting_command -> expression TO expression','converting_command',3,'p_converting_command','parser.py',226),
  ('vector_command -> VARIABLE PUSH BACK expression','vector_command',4,'p_vector_command','parser.py',231),
  ('vector_command -> VARIABLE POP BACK','vector_command',3,'p_vector_command','parser.py',232),
  ('vector_command -> VARIABLE PUSH FRONT expression','vector_command',4,'p_vector_command','parser.py',233),
  ('vector_command -> VARIABLE POP FRONT','vector_command',3,'p_vector_command','parser.py',234),
  ('robot_command -> LEFT','robot_command',1,'p_robot_command','parser.py',242),
  ('robot_command -> RIGHT','robot_command',1,'p_robot_command','parser.py',243),
  ('robot_command -> FORWARD','robot_command',1,'p_robot_command','parser.py',244),
  ('robot_command -> BACK','robot_command',1,'p_robot_command','parser.py',245),
  ('robot_command -> ROTATE_RIGHT','robot_command',1,'p_robot_command','parser.py',246),
  ('robot_command -> ROTATE_LEFT','robot_command',1,'p_robot_command','parser.py',247),
  ('robot_command -> LMS','robot_command',1,'p_robot_command','parser.py',248),
  ('robot_command -> REFLECT','robot_command',1,'p_robot_command','parser.py',249),
  ('robot_command -> DRILL','robot_command',1,'p_robot_command','parser.py',250),
  ('call -> VARIABLE LBRACKET parameters RBRACKET','call',4,'p_call','parser.py',255),
  ('call -> VARIABLE BRACKETS','call',2,'p_call','parser.py',256),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',264),
  ('parameters -> parameters COMMA parameter','parameters',3,'p_parameters','parser.py',269),
  ('parameters -> parameter','parameters',1,'p_parameters','parser.py',270),
  ('parameters -> parameters CONTINUE','parameters',2,'p_parameters','parser.py',271),
  ('parameter -> expression','parameter',1,'p_parameter','parser.py',281),
  ('parameter -> VARIABLE EQ expression','parameter',3,'p_parameter','parser.py',282),
]
