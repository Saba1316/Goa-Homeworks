# Codewars 8 kyu: 
# Enumerable Magic #30 - Split that Array!


def partition(list, classifier_method):
    listTrue = []
    listFalse = []
    for l in list:
        if classifier_method(l):
            listTrue.append(l)
        else:
            listFalse.append(l)
    return listTrue, listFalse