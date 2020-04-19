# VAR 70 (***)

"""Разработать систему для управления клеточным роботом, осуществляющим передвижение по
    клеточному лабиринту. Клетка лабиринта имеет форму квадрата, клетки лабиринта могут быть
    разделены стенами (толщиной стен можно пренебречь), из различных материалов (пластик, дерево,
    бетон, и т.п.)
    Робот может передвинуться в соседнюю клетку в случае отсутствия между ними препятствия, у
    робота есть ограниченные возможности разрушать препятствия (см. соответствующий раздел)"""


"""
    1. Знаковые целочисленные литералы в десятичной форме
    2. false, true, undefined
    3. "String" or 'String'
    4. boolean <name> [:=false] [, <name2> [:= smth]];
    5. string <name> [:=     ...
    6. integer <name> [:=   ...
    7. vector of <TYPE> <arr> [, <arr2>...]
        1. arr[0]
        2. <arr> push/pop back/front <smth>
    8. <smth> to <TYPE>
    9 <smth1> to <smth2>
    
    ---------
    
    10. <var> := <smth>
    11. <smth> +/- <smth>
    12. <smth> (<,>, =, <>) <smth>
    13. begin, end
    14. do <sentence(s)> until <logical>
    15. if <logical> then <sentence(s)> [else <sentence(s)>]
    
    ---- ROBOT ----
    
    1. right, left, forward, back  
    2. rotate_right, rotate_left
    3. lms
    4. reflect
    5. drill 

    ----------------
    
    16. function of <RETURN_TYPE> <name> ([<name> = <default>,..) <sentence(s)>
        1. RETURN is last sentence or 'return <smth>'
        2. MAIN is 'application' function
        3. YOU CAN'T CALL APPLICATION
        4. YOU CAN'T DEFINE FUNCTION IN OTHER FUNCTION
    17. <name> ([<name> = <default>,..)
    
    ---- EXAMPLES ----
    
    function of boolean test(first, second)
    return first < second
    
    function of integer num_test(tester, first, second)
    if test(first, second) return 42 else return 100500
    
    function of integer application(int_param = 0, vector_of_strings)
    num_test(test, first = 5, second = 25)
    
    ---- MY EXAMPLE BUBBLE SORT ----
    
    vector of int my_vector
    my_vector push front 3
    my_vector push front 5
    my_vector push back 7
    my_vector push back 1
    my_vector push back -3
    my_vector push front 4
    
    # 45371(-3)
    
    integer size := 6
    integer temp := 0
    integer i := 0
    integer j := 0
    
    do begin
        do begin
            if my_vector[j] < my_vector[j+1] begin
                temp := my_vector[j+1]
                my_vector[j+1] := my_vector[j]
                my_vector[j] := temp
                end
            j := j + 1
            end until j < size-1
        i := i + 1
    end until i < size-1
    
    # (-3)13457

"""