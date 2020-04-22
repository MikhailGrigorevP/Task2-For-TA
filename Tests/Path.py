"""

map:

    ###############
        ####   ####
    ###      ######
    ### #### ###  #
    ##  ####     ##
    ######### ## ##
    ##### ###
    #####      ####
    ###############

    function of integer return_y (stack_y, size_y, y)
        return y + stack_y[size_y-1] - stack_y[size_y-2]

    function of integer return_x (stack_x, size_x, x)
        return x + stack_x[size_x-1] - stack_x[size_x-2]

    function of integer findPath(x, y) begin
        integer turn := 0
        boolean exit := false
        do begin
            if reflect = "EXIT" then exit = true
            else begin
                if forward <> true then begin
                    # TODO EXPAND MAP
                    integer i := lms
                    # TODO STEPS
                end else begin
                    right
                    turn := turn + 1
                if turn = 4 then begin
                    turn := 0
                    x := stack_x pop back
                    y := stack_y pop back
                end
            end until exit <> true


        end

    ## Main
    function of integer application() begin

        integer x := 0
        integer y := 0

        return findPath(x, y)
        end






"""