#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    result = []
    x = 0

    for ind in range(0, list_length):
        try:
            x = my_list_1[ind] / my_list_2[ind]
        except (TypeError):
            x = 0
            print("wrong type")

        except (ZeroDivisionError):
            x = 0
            print("division by 0")
        except (IndexError):
            x = 0
            print("out of range")

        finally:
            pass

        result.append(x)
    return(result)
