import genepy as gp 

def test_Individual_mutate(k):
    t = gp.Individual([.3,.5,.3,.8,.7,.6,.4,.5,.7,.9])

    print(t.par)

    t.mutate(k)

    print(t.par)

test_Individual_mutate(0.3)