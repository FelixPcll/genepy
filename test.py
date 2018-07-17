import genepy as gp
import numpy as np
import matplotlib.pyplot as plt

print('\n'+'-+'*84+'-'+'\n')


def test_Individual_mutate(k):
    t = gp.Individual([.3, .5, .3, .8, .7, .6, .4, .5, .7, .9])

    print(t.par)

    t.mutate(k)

    print(t.par)


def test_Individual_breed(p):
    ind1 = gp.Individual([.0, .1, .2, .3, .4, .5, .6, .7, .8, .9])
    ind2 = gp.Individual([.0001, .01, .02, .03, .04, .05, .06, .07, .08, .09])

    ind1.breed(ind2, p)

    print(ind1.sons[0].par)
    print(ind2.sons[1].par)


def test_Environment_gen_population(n):
    planes = gp.Environment()
    planes.gen_population(n)
    print(len(planes.start_population))
    for i in planes.start_population:
        print(i.par)


def test_Environment_preasure(n):
    forest = gp.Environment()
    forest.gen_population(n)
    perfect = gp.Individual(par=[1 for _ in range(10)])
    forest.curr_pop.append(perfect)
    for i in forest.curr_pop:
        forest.preasure(i)
        right = 0
        for j in i.par:
            right += 1-(1-j)**2

        print('DNA -> {}\nSCORE -> {} || Right -> {}\n'.format(i.par,
                                                               i.score, right))


def test_Environment_evolve(n, k, m, t):
    E = gp.Environment()
    E.gen_population(n)

    df = []
    for _ in range(t):
        E.evolve(keep=k, mutate=m)

        now = np.array(list(map(lambda x: x.score, E.curr_pop)))
        df.append(now.mean())

    ipop = []
    ipop.extend(E.start_population)

    fpop = []
    fpop.extend(E.curr_pop)

    print("""\n\n
             Start Pop: {}\n
             Start Score: {}\n
             \n
             Final Pop: {}\n
             Final Score {}""".format(len(list(map(lambda x: x.par, ipop))),
                                      max(list(map(lambda x: x.score, ipop))),
                                      len(list(map(lambda x: x.par, fpop))),
                                      max(list(map(lambda x: x.score, fpop)))))

    return df


df = test_Environment_evolve(n=100, k=30, m=0.10, t=100)

plt.plot(df)
plt.show()
