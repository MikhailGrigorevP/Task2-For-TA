"""
    Turn:

     3
    2 0
     1

     Algorithm:

    function of integer return_y (stack_y, size_y, y)
        return y + stack_y[size_y-1] - stack_y[size_y-2]
    function of integer return_x (stack_x, size_x, x)
        return x + stack_x[size_x-1] - stack_x[size_x-2]
    function of integer expand_x_back (vm, size_y, y, size_x, lms1)
        # EXPAND TO RIGHT
        if x + lms1 < size_x - 1 then begin
        integer steps := x + lms1 - size_x + 1
        size_x := size_x + steps
        do begin
            integer i := size_y
            do begin
                if steps = y then vm[steps] push back True else vm[steps] push back False
                i := i - 1
                end until i <> 0
            steps := steps - 1
            end until steps <> 0
    function of integer expand_x_front (vm, size_y, y, x, size_x, stack_x, stack_x_size, lms1)
        # EXPAND TO LEFT
        if x - lms1 < 0 then begin
        integer steps := lms1 - x
        size_x := size_x + steps
        do begin
            integer i := size_y
            do begin
                if steps = y then vm[steps] push front True else vm[steps] push front False
                i := i - 1
                end until i <> 0
            steps := steps - 1
            end until steps <> 0
        steps := lms1 - x
        x:= x + steps
        integer i := 0
        do begin
            stack_x [ i ] := stack_x [ i ] + steps
            i := i + 1
            end until i <> stack_x_size
    function of integer expand_y_front(vm, size_x, x, size_y, lms1)
        # EXPAND TO RIGHT
        if y + lms1 < size_y - 1 then begin
        integer steps := y + lms1 - size_y + 1
        size_y := size_y + steps
        do begin
            integer i := size_x
            do begin
                if steps = x then vm push front True else vm push front False
                i := i - 1
                end until i <> 0
            steps := steps - 1
            end until steps <> 0
    function of integer expand_y_back (vm, size_x, y, x, size_y, stack_y, stack_y_size, lms1)
        # EXPAND TO LEFT
        if y - lms1 < 0 then begin
        integer steps := lms1 - y
        size_y := size_y + steps
        do begin
            integer i := size_x
            do begin
                if steps = x then vm push back True else vm push back False
                i := i - 1
                end until i <> 0
            steps := steps - 1
            end until steps <> 0
        steps := lms1 - y
        y:= y + steps
        integer i := 0
        do begin
            stack_y [ i ] := stack_y [ i ] + steps
            i := i + 1
            end until i <> stack_y_size
    function of integer findPath(x, y) begin
        # size
        vector of vector of boolean vm
        vector of boolean x
        x push back true
        vm push back x
        integer size_x := 0
        integer size_y := 0
        # direction off look
        integer turn := 0
        # num off turns in current cell
        integer numOfTurns := 0
        # exit flag
        boolean willTurn := true
        boolean exit := false
        do begin
            # iff we found exit
            if reflect = "EXIT" then exit := true else begin
                # iff we CAN move forw
                if lms <> 0 then begin
                    numOfTurns := 0
                    willTurn := false
                    # we should expand our map
                    integer i := lms
                    integer free := lms
                    if turn = 0 then free := size_x - 1 - x else if turn = 1 then free := y else if turn = 2 then free := x else if turn = 3 then free := size_y - 1 - y
                    if free < i then i := free
                    do begin
                        # step
                        forward
                        # change current coordinates off robot
                        # add x
                        if vm[y] = false then begin
                            if turn = 0 then x := x + 1 else if turn = 1 then y := y - 1 else if turn = 2 then x := x - 1 else if turn = 3 then y := y + 1
                            # add current position too stack
                            stack_x push front x
                            stack_y push front y
                            i := i - 1
                        end else begin
                            i:= 0
                            willTurn := true
                            end
                        end until i <> 0
                    if lms then
                        if willTurn <> 1 then begin
                            if turn = 0 then expand_x_back (vm, size_y, y, size_x, lms) else if turn = 1 then expand_y_back(vm, size_x, y, x, size_y, stack_y, stack_y_size, lms) else if turn = 2 then expand_x_front (vm, size_y, y, x, size_x, stack_x, stack_x_size, lms) else if turn = 3 then expand_y_front(vm, size_x, x, size_y, lms)
                            # counter for cycle
                            i := lms
                            # make steps
                            # counter for cycle
                            i := lms
                            do begin
                                # step
                                forward
                                # change current coordinates off robot
                                if turn = 0 then x := x + 1 else if turn = 1 then y := y - 1 else if turn = 2 then x := x - 1 else if turn = 3 then y := y + 1
                                # add current position too stack
                                stack_x push front x
                                stack_y push front y
                                i := i - 1
                            end until i <> 0
                        end
                    end
                end
                # iff we CANT move forw
                if willTurn then begin
                    right
                    turn := turn + 1
                    numOfTurns := numOfTurns + 1
                end
                if numOfTurns = 4 then begin
                    numOfTurns := 0
                    x := stack_x pop front
                    y := stack_y pop front
                end
            end until exit <> true
    end
    # Main
    function of integer application() begin
        # Start position
        integer x := 0
        integer y := 0
        stack_x push front x
        stack_y push front y
        return findPath(x, y)
        end






"""