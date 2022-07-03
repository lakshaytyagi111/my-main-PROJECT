

def facto(number):
    if number == 0:
        constant = 1
        return constant
    elif number > 0:
        i=1
        result = 1
        while i !=(number+1):
            result *=i
            i+=1
        return(result)

    elif number < 0:
        print('________factorial is not defined for negative values________')

def Combination(number, selected, y=0):
    if number >= selected:
        if number == int(number):
            pass
        else:
            number = int(number)
            print('cannot take input as decimal thus changing it to : ' + str(number))

        u = number-selected
        result_of_combination = int(
            facto(number))/int(facto(u)*facto(selected))

        if y == 1:
            print(result_of_combination)
            return result_of_combination
        else:
            return result_of_combination
            pass
    else:
        print('_______not valid request_________')
        exit()

def permutation(number, selected, y=0):
    if number >= selected:
        if number == int(number):
            pass
        else:
            number = int(number)
            print('cannot take input as decimal thus changing it to : ' + str(number))
        u = number-selected
        result_of_permutation = (facto(number))/(facto(u))

        if y == 1:
            print(result_of_permutation)
            return result_of_permutation
        else:
            return result_of_permutation
            pass
    else:
        print('_______not valid request_________')
        exit()


def lines(total_points, colinear_points, y=0):
    points = int(total_points)
    colinear_points = int(colinear_points)
    if colinear_points == 0:
        result_of_lines = Combination(points, 2, y)
        return result_of_lines
    elif colinear_points >= 2:
        result_of_lines = int(Combination(points, 2, 0)) - \
            int(Combination(colinear_points, 2, 0)) + 1
        return result_of_lines
    else:
        print('______something gone wrong please recheck if number of colinear points is less than total points or not OR must not less than 2_______')
        exit()

def diagonals(number_of_sides, y=0):
    result_of_diagonals = Combination(number_of_sides, 2, 0) - number_of_sides
    result_of_diagonals = int(result_of_diagonals)
    if y == 1:
        print(result_of_diagonals)
        return result_of_diagonals
    else:
        return result_of_diagonals


def triangles(sides_of_polygon, sides_common_with_polygon, y=0):
    if sides_common_with_polygon <= sides_of_polygon:
        if sides_common_with_polygon == 1:
            result_of_triangle = int(sides_of_polygon*(sides_of_polygon-1))

            if y == 1:
                return result_of_triangle
                print(result_of_triangle)
            else:
                return result_of_triangle

        elif sides_common_with_polygon == 2:
            result_of_triangle = int(sides_of_polygon)

            if y == 1:
                return result_of_triangle
                print(result_of_triangle)
            else:
                return result_of_triangle

        elif sides_common_with_polygon == 0:
            result_of_triangle = int(Combination(
                sides_of_polygon, 3, 0) - sides_of_polygon - sides_of_polygon*(sides_of_polygon-1))

            if y == 1:
                return result_of_triangle
                print(result_of_triangle)
            else:
                return result_of_triangle
        else:
            print('__unsupported input__')
    else:
        print('error: i guess something is wrong with the input OR nuber of commmon sides is greater than total nmber of sides of polygon')


def inter_lines(number_of_lines, number_of_concurrent_lines, y=0):
    n = number_of_lines
    x = number_of_concurrent_lines
    if x!=0:
        result_of_inter_lines = Combination(n, 2, 0) - Combination(x, 2, 0) + 1
    else:
        result_of_inter_lines = Combination(n, 2, 2)
    if y == 1:
        print(result_of_inter_lines)
    else:
        return result_of_inter_lines

def inter_circles(number_of_circles, number_of_lines, y=0):
    m = number_of_circles
    n = number_of_lines
    if number_of_lines==0:
        result_of_inter_circles = Combination(n, 2, 0)
        result_of_inter_circles = int(result_of_inter_circles)
    else:
        result_of_inter_circles = Combination(n, 2, 0) + 2*Combination(m, 2, 0) + 2*(Combination(n, 1, 0))*(Combination(m, 1, 0))
        result_of_inter_circles = int(result_of_inter_circles)
    
    if y == 1:
        print(int(result_of_inter_circles))
        return result_of_inter_circles
    else:
        return int(result_of_inter_circles)

def rectangle(x, y, z):
    result_of_rectangle = Combination(x+1, 2, 0)*Combination(y+1, 2, 0)
    return result_of_rectangle

