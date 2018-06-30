import genepy as gp

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
    for i in forest.curr_pop:
        forest.preasure(i)
        right = 0
        for j in i.par:
            right += 1-(1-j)**2

        print('DNA -> {}\nSCORE -> {} || Right -> {}'.format(i.par,
                                                             i.score, right))


def test_Environment_evolve(n, t):
    E = gp.Environment()
    E.gen_population(n)
    for i in range(t):
        E.evolve()
        pop = [j.par for j in E.curr_pop]
        scr = [j.score for j in E.curr_pop]

        print('{} -> {} || {}'.format(i, pop, max(scr)))


test_Environment_evolve(6, 9)
