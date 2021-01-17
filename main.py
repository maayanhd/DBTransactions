# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




def test_transaction_timing():

    print("Please enter the transaction timing string:")
    timing_s = input()
    operation_str_list = timing_s.split(";")

    operation_list = []
    vertex_list = []
    for elem in operation_str_list:
        temp_el = elem.strip()[0:-1]
        op_var_list = temp_el.split("(")

        r_or_w = (op_var_list[0])[0].strip()
        vertex = (op_var_list[0])[1:].strip()
        var = op_var_list[1].strip()

        operation_list.append((r_or_w,vertex,var))

        if not vertex in vertex_list:
            vertex_list.append(vertex)


    print(operation_list)
    print(vertex_list)
    ''' transactions_graph = build_graph(vertex_list)


    for i in range(0,len(operation_list)-1):
        for j in range (i+1,len(operation_list)):
            if is_adding_edge_needed(operation_list[i],operation_list[j])
                u = operation_list[i][1]
                v = operation_list[j][1]
                transactions_graph.add_edge(u,v)

    '''
def is_adding_edge_needed(op_1,op_2):

    if op_1[1] != op_2[1]:
        if not (op_1[0] == 'R' and op_2[0] == 'R'):
            if op_1[-1] == op_2[-1]:
                return True

    return False




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_transaction_timing()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
