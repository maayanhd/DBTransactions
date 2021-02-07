def test_transaction_timing():
    """Getting input from the user"""
    print("Please enter the transaction timing string:")
    timing_str = input()

    '''Parsing transaction string  '''
    operations_vertexes_tuple = parse_transactions_str(timing_str.strip())
    operation_list = operations_vertexes_tuple[0]
    vertex_list = operations_vertexes_tuple[1]

    transactions_graph = build_graph_by_conflicts(vertex_list, operation_list)
    '''Prints'''
    transactions_graph.topological_sort()


def parse_transactions_str(timing_str):
    if timing_str[-1] == ";":
        timing_str = timing_str[:-1]

    operation_str_list = timing_str.split(";")
    operation_list = []
    vertex_list = []
    for elem in operation_str_list:
        temp_el = elem.strip()[0:-1]
        op_var_list = temp_el.split("(")

        r_or_w = (op_var_list[0])[0].strip()
        vertex = int((op_var_list[0])[1:].strip())
        var = op_var_list[1].strip()

        operation_list.append((r_or_w, vertex, var))

        if vertex not in vertex_list:
            vertex_list.append(vertex)

    return operation_list, vertex_list


def build_graph_by_conflicts(vertex_list, operation_list):
    transactions_graph = Graph(vertex_list)

    for i in range(0, len(operation_list) - 1):
        for j in range(i + 1, len(operation_list)):
            if is_adding_edge_needed(operation_list[i], operation_list[j]):
                u = operation_list[i][1]
                v = operation_list[j][1]
                transactions_graph.add_edge(u, v)

    return transactions_graph


def is_adding_edge_needed(op_1, op_2):
    if op_1[1] != op_2[1]:
        if not (op_1[0] == 'R' and op_2[0] == 'R'):
            if op_1[-1] == op_2[-1]:
                return True

    return False


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.vert_num = len(vertices)
        self.graph = [[0] * (self.vert_num + 1) for i in range(self.vert_num + 1)]  # Graph containing adjacent Matrix
        self.vertices = vertices  # No. of vertices

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u][v] = 1

    # A function used by topologicalSort
    def topological_sort(self):
        vertex_indegree_arr = [0] * (self.vert_num + 1)
        source_queue = []



        for i in range(1, self.vert_num + 1):
            for j in range(1, self.vert_num + 1):
                if self.graph[i][j] == 1:
                    vertex_indegree_arr[j] += 1

        for vert in range(1, self.vert_num + 1):
            if vertex_indegree_arr[vert] == 0:
                '''Adding vertex to queue'''
                source_queue.append(vert)

        topological_sorted_list = []
        while len(source_queue) != 0:
            '''Enqueue the first vertex'''
            first_vertex = source_queue.pop(0)
            topological_sorted_list.append(first_vertex)
            for j in range(1, self.vert_num + 1):
                '''Checking whether there is an edge (i,j) '''
                if self.graph[first_vertex][j] == 1:
                    '''Removing the edge (i,j)'''
                    vertex_indegree_arr[j] -= 1
                    '''Checking whether the vertex is a source after update'''
                    if vertex_indegree_arr[j] == 0:
                        source_queue.append(j)

        if not is_there_a_topological_sort(vertex_indegree_arr):
            print("NO")
        else:

            print_sorted_transactions(topological_sorted_list)


def is_there_a_topological_sort(vertex_indegree_arr):
    for i in range(1, len(vertex_indegree_arr)):
        if vertex_indegree_arr[i] > 0:
            return False

    return True


def print_sorted_transactions(topological_sorted_list):
    output_str = ""
    for vert in topological_sorted_list:
        output_str += "T" + str(vert) + "->"
    ''' Removing redundant arrow'''
    print(output_str[:-2])


if __name__ == '__main__':
    test_transaction_timing()