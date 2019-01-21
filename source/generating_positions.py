import numpy as np

RANDOM_SEED = 2019


def random_layout(G, dim=2):
    import random
    random.seed(RANDOM_SEED)

    vpos = {}
    for v in G.nodes():
        vpos[v] = np.array([random.random() for i in range(dim)])
    return vpos


def circular_layout(G, dim=2):
    vpos = {}
    r = 1.0
    t = 0
    dt = 2.0 * np.pi / G.order()
    for v in G:
        p = dim * [0.0]
        p[0] = r * np.cos(t)
        p[1] = r * np.sin(t)
        vpos[v] = np.array(p)
        t = t + dt
    return vpos


def spring_layout(G, iterations=50, dim=2, node_pos=None):
    vpos = random_layout(G, dim=dim)
    if iterations == 0:
        return vpos
    if G.order() == 0:
        k = 1.0
    else:
        k = np.sqrt(1.0 / G.order())

    disp = {}
    t = 0.1
    dt = 0.1 / float(iterations + 1)

    for i in range(0, iterations):
        for v in G:
            disp[v] = np.zeros(dim)
            for u in G:
                delta = vpos[v] - vpos[u]
                dn = max(np.sqrt(np.dot(delta, delta)), 0.01)
                deltaf = delta * k ** 2 / dn ** 2
                disp[v] = disp[v] + deltaf
                if G.has_edge(v, u):
                    deltaf = - delta * dn ** 2 / (k * dn)
                    disp[v] = disp[v] + deltaf

        for v in G:
            l = max(np.sqrt(np.dot(disp[v], disp[v])), 0.01)
            vpos[v] = vpos[v] + disp[v] * t / l
        t -= dt

    return vpos