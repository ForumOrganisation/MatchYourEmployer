from collections import defaultdict
from source.model import Matching, Link
from source.utils import log


class MatchMaker:
    # algorithm constants

    SOURCE_NODE = 'source'
    SINK_NODE = 'sink'

    def __init__(self, students, companies):
        self.students = students
        self.companies = companies

    def compute_matching(self, matching_parameters):
        log('info', 'starting matching...')
        # generate graph
        log('info', 'creating the matching graph...')
        # create graph as defaultdict of defaultdict
        graph_matching = defaultdict(lambda: defaultdict(int))

        # initiate source & sink nodes according to parameters
        # those nodes are refered by strings, the others are refered by their id
        for id_student in [student.id_student for student in self.students]:
            graph_matching[self.SOURCE_NODE][id_student] = matching_parameters.nb_company_by_student

        for id_company in [company.id_company for company in self.companies]:
            graph_matching[id_company][self.SINK_NODE] = matching_parameters.nb_student_by_company

        # for every pair of student - company, add a link between them if their association is stronger than the treshold
        # store the links
        all_links = set()
        for student in self.students:
            for company in self.companies:
                score_association = matching_parameters.distance_evaluator.evaluate(
                    student, company)
                if score_association > matching_parameters.treshold:
                    all_links.add(Link(student, company, score_association))
                    graph_matching[student.id_student][company.id_company] = 1
        # run ford fulkerson algorithm, the graph is modified
        log('info', 'running the matching algorithm...')
        number_association = self.ford_fulkerson(
            graph_matching, self.SOURCE_NODE, self.SINK_NODE)

        # extract the matching as an object and return it
        # extract all the links : they are the backward edges activated in the residual graph
        log('info', 'extracting the links...')
        selected_links = set()
        for link in all_links:
            if graph_matching[link.company.id_company][link.student.id_student] == 1:
                selected_links.add(link)
        final_matching = Matching(
            self.students, self.companies, matching_parameters, selected_links)
        log('info', 'matching computation done ! ')
        return final_matching

    # Algorithm found on https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/ and modified
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''

    def bfs(self, graph, s, t, parent):

        # Mark all the vertices as not visited
        visited = defaultdict(lambda: False)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for neigh, val in graph[u].items():
                if visited[neigh] == False and val > 0:
                    queue.append(neigh)
                    visited[neigh] = True
                    parent[neigh] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    # Returns tne maximum flow from s to t in the given graph
    def ford_fulkerson(self, graph, source, sink):

        # This array is filled by BFS and to store path
        parent = defaultdict(lambda: -1)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.bfs(graph, source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v != source):
                u = parent[v]
                graph[u][v] -= path_flow
                graph[v][u] += path_flow
                v = parent[v]

        return max_flow
