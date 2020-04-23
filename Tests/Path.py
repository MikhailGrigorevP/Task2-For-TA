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

    function of integer findPath(x, y) begin
        # size
        vector of vector of bool vm
        vector of bool x
        x push back true
        vm push back x
        integer size_x := 0
        integer size_y := 0
        # direction of look
        integer turn := 0
        # num of turns in current cell
        integer numOfTurns := 0
        # exit flag
        boolean exit := false
        do begin
            # if we found exit
            if reflect = "EXIT" then exit = true
            else begin
                # if we CAN move forward
                if lms <> 0 then begin
                    numOfTurns := 0
                    # we should expand our map


                    if turn = 0 then begin x := x + 1

                        # EXPAND TO LEFT
                        if x + lms < size_x - 1 then begin
                            integer steps := x + lms - size_x + 1
                            size_x := size_x + steps
                            do begin
                                integer i: size_y - 1
                                do begin
                                    if steps = y then vm[steps] push back True
                                        else vm[steps] push back False
                                    i := i - 1
                                    end until i <> 0
                                steps := steps - 1
                                end until steps <> 0

                        # TODO EXPAND OTHERS
                        end else if turn = 1 then begin y := y - 1

                        end else if turn = 2 then begin x := x - 1

                        end else if turn = 3 then begin y := y + 1


                    # counter for cycle
                    integer i := lms
                    # TODO EXPAND STACK
                    # update stack
                    # make steps
                    # counter for cycle
                    integer i := lms
                    do begin
                        # step
                        forward
                        # change current coordinates of robot
                        if turn = 0 then x := x + 1
                        else if turn = 1 then y := y - 1
                        else if turn = 2 then x := x - 1
                        else if turn = 3 then y := y + 1
                        # add current position to stack
                        stack_x push front x
                        stack_y push front y
                        i := i - 1
                        end until i <> 0
                # if we CAN'T move forward
                end else begin
                    right
                    turn := turn + 1
                    numOfTurns := numOfTurns + 1
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