import pickle, random, itertools, copy

# Dictionary of filename sequences: subject name -> type -> list of filenames
filenames = pickle.load(open('filenames.pickle'))

subjects = sorted(filenames.keys())

def n_sequences(subject):
    """ Return number of preictal and interictal sequence for a subject"""
    return len(filenames[subject]['preictal']), len(filenames[subject]['interictal'])

def sequence_filenames(subject, sequencetype, sequencenumber):
    """ Return list of filenames for a given subject, type (preictal or interictal), and sequence number"""
    return filenames[subject][sequencetype][sequencenumber]

def leave_N_out(subject, N_preictal=1, N_interictal=1, randomseed=None):
    """ Split by leaving out N sequences of each type. Returns two lists of filenames (train, test) """
    if randomseed:
        random.seed(randomseed)

    preictal = copy.deepcopy(filenames[subject]['preictal'])
    random.shuffle(preictal)
    interictal = copy.deepcopy(filenames[subject]['interictal'])
    random.shuffle(interictal)
    
    train = preictal[N_preictal:]+interictal[N_interictal:]
    train = list(itertools.chain.from_iterable(train))
    test = preictal[:N_preictal]+interictal[:N_interictal]
    test = list(itertools.chain.from_iterable(test))

    return train, test
