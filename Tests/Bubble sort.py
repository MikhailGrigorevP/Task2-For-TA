"""
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