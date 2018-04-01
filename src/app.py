import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Création d'un graphe non dirigé
    my_graph = nx.Graph()

    # Le code rajoute un node dans le graphe :
    # le premier argument est son identifiant (ça peut être nimporte quoi pouvant être hashé)
    # les arguments suivants sont des attributs supplémentaires optionnels si on veut customiser le node
    my_graph.add_node("node1", nom="Mourad", age=200, sexe="Apache d'helicoptere", annee="MA2")
    my_graph.add_node("node2", nom="Mounir", age=459, sexe="femelle", annee="BA4", est_homosexuel=True)
    my_graph.add_node("node3", nom="Trumps", age=1e300, sexe="femelle", annee="PhD", est_homosexuel=False)

    # On peut également rajouter des edges :
    # On donne une paire de nodes. Comme le graphe n'est pas dirigé, on ne parle pas de "source destination".
    my_graph.add_edge("node1", "node2")

    # On peut aussi créer un tuple pour le rajouter
    mon_edge = ("node1", "node3")
    my_graph.add_edge(*mon_edge)  # Oui, je sais, ça fait penser au C++, on ferait mieux d'éviter cette méthode mdr.

    # Ah, et on peut aussi rajouter plusieurs noeuds à la volée en donnant un array en paramètre
    my_graph.add_nodes_from(["node4", "node5", "node6"])

    # Pareil pour les edges, on peut en rajouter plusieurs d'un coup :
    my_graph.add_edges_from([
        ("node4", "node5", {'attribut1': 'jaune'}),
        ("node3", "node6", {'attribut1': 'gold'})
    ])

    # L'instruction suivante supprime tous les noeuds et edges
    # graph.clear()

    # Attention, comme les strings en python sont des "array de char",
    # le fait de faire l'instruction suivante va rajouter 4 nodes :
    my_graph.add_nodes_from("spam")
    # les nodes "s", "p", "a" et "m", qui sont les chars dans le string.

    # Connaitre le degré d'un node ( = nombre de edges incident à ce node)
    print(my_graph.degree["node1"])
    # Connaitre le degré de plusieurs nodes d'un coup :
    print(my_graph.degree(["node1", "node2"]))
    # Connaitre les nodes adjacents à un node donné
    print(my_graph.adj["node1"])

    # Retirer un node
    # -- ATTENTION : retirer un node, retire également tous les EDGES incidents à ce node,
    # c'est normal.
    my_graph.remove_node("node5")
    # Retirer un edge
    my_graph.remove_edge("node3", "node6")
    # Lire/écrire un attribut d'un edge
    my_graph["node1"]["node2"]["propiete_du_edge"] = 42
    print(my_graph["node1"]["node2"]["propiete_du_edge"])

    # On peut rajouter des weighted edges
    my_graph.add_weighted_edges_from([("node1", "node3", 666), ("node3", "s", 9999)])
    print("\npetit for des familles qui montre "
          "tous les edges qui ont un poids (donc un attribut qui s'appelle weight) :")
    for (u, v, wt) in my_graph.edges.data('weight'):
        if wt is not None:
            print('    (%s, %s, %.3f)' % (u, v, wt))

    # Affiche tous les edges
    print(my_graph.edges)
    # Affiche tous les nodes
    print(my_graph.nodes)

    # On peut même créer des attributs sur le graphe en lui-même :
    my_graph.graph["name"] = "Carte du bourg-palette - Pokémon Rubis"
    print(my_graph.graph)

    # On peut faire plein d'opérations qu'on s'abstiendra
    # de faire sinon c'est de la triche je pense
    """
    > union(G1,G2)             - graph union
    > disjoint_union(G1,G2)    - graph union assuming all nodes are different
    > cartesian_product(G1,G2) - return Cartesian product graph
    > compose(G1,G2)           - combine graphs identifying nodes common to both
    > complement(G)            - graph complement
    > create_empty_copy(G)     - return an empty copy of the same graph class
    > convert_to_undirected(G) - return an undirected representation of G
    > convert_to_directed(G)   - return a directed representation of G
    """

    # Plein d'autres fantaisies encores (création de graphes bien précis) :
    """
    >>> petersen = nx.petersen_graph()
    >>> tutte = nx.tutte_graph()
    >>> maze = nx.sedgewick_maze_graph()
    >>> tet = nx.tetrahedral_graph()
    """

    # Création de graphes particuliers :
    """
    >>> K_5 = nx.complete_graph(5)
    >>> K_3_5 = nx.complete_bipartite_graph(3, 5)
    >>> barbell = nx.barbell_graph(10, 10)
    >>> lollipop = nx.lollipop_graph(10, 20)
    """

    # Création de graphes random en utilisant des random generator connus
    """
    >>> er = nx.erdos_renyi_graph(100, 0.15)
    >>> ws = nx.watts_strogatz_graph(30, 3, 0.1)
    >>> ba = nx.barabasi_albert_graph(100, 5)
    >>> red = nx.random_lobster(100, 0.9, 0.9)
    """

    # Lire/écrire le graphe dans un fichier (il y a un format standard)
    """
    >>> nx.write_gml(red, "path.to.file")
    >>> mygraph = nx.read_gml("path.to.file")
    """

    # Et encore pleins de merveilleuses choses :
    # https://networkx.github.io/documentation/stable/reference/algorithms/index.html

    # Dessiner le graphe (pour l'afficher à l'écran)
    # Il y a plusieurs manières de dessiner : draw_shell, draw_random, draw_spectral, draw_circular, etc.
    # https://networkx.github.io/documentation/stable/reference/drawing.html
    nx.draw_random(my_graph, with_labels=True, font_weight='bold')
    # Enregistrer l'image
    plt.savefig("graphe.png")
    # Afficher à l'écran
    plt.show()

    # La librairie est très connue et implémente déjà dikstra, etc.
    # mais on n'utilisera pas leur implémentation lol :
    # https: // networkx.github.io / documentation / stable / index.html
