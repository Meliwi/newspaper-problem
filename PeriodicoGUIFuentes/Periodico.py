from minizinc import *
from DisplayInfo import displayInfo

def periodico(number_pages, topics, min_nb_pages, max_nb_pages, potential_readers):
    with open("PeriodicoData.dzn", "w") as dzn_file:
        dzn_file.write("num_pages="+str(number_pages)+";"+"\n")
        dzn_file.write("Topics={"+topics+"};"+"\n")
        dzn_file.write("min_nb_pages = ["+min_nb_pages+"];"+"\n")
        dzn_file.write("max_nb_pages = ["+max_nb_pages+"];"+"\n")
        dzn_file.write("potential_readers = ["+potential_readers+"];"+"\n")
        newspaper_model = Model("./PeriodicoGenerico.mzn")
        newspaper_model.add_file("./PeriodicoData.dzn")
        solver = Solver.lookup("gecode")
        instance = Instance(solver, newspaper_model)
    result = instance.solve()
    newspaper_topics_list = result.solution.newspaper_topics
    newspaper_list = result.solution.newspaper
    sol_potential_readers = result.solution.objective
    newspaper_topics_index = [index for index in range(len(newspaper_topics_list)) if newspaper_topics_list[index] == 1]
    topics_list = topics.split(",")
    chosen_topics = []
    pages_topics = []
    for index in newspaper_topics_index:
        chosen_topics.append(topics_list[index])
    for index in newspaper_topics_index:
        pages_topics.append(newspaper_list[index])
    displayInfo()