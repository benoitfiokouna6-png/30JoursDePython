# Tuples 

# Créer tuples vide 

tuple_vide = tuple()

# créer un tuple contenant le nom de mes frères et soeurs

tuple_mes_frères_et_soeurs = ('elisés', 'enok', 'marceline', 'germaine')

# nombres de frères et soeurs

print(len(tuple_mes_frères_et_soeurs)) # nombres de frères et soeurs dans la famille est (4)

# tuples mes parents 

tuple_parents = ('kodjo','abla')

# modifications des tuples 


membres_de_familles = (tuple_parents+tuple_mes_frères_et_soeurs)

Exercices:2

# déballer les tuples mes freres et soeurs et mes parents

kodjo, abla = tuple_parents

print("kodjo =", kodjo)

elisé, enok, marceline, germaine = tuple_mes_frères_et_soeurs

tuple_fruits = ('banane','orange','citron','mangue')

tuple_légumes = ('salade','chou','tomate','poivrons','haricots')

tuple_produits_animales = ('viande','lait','oeufs','poison')

food_stuff_tp = (tuple_fruits+tuple_légumes+tuple_produits_animales)

print(food_stuff_tp)

# Changements de tuple en liste 

food_stuff_tp = list(food_stuff_tp)

# découpage de trois premiers éléments

trois_premiers_elements = food_stuff_tp[:3]  #les trois premiers éléments de la liste est (['banana','orange','citron'])

print(trois_premiers_elements)

trois_derniers_elements = food_stuff_tp[-3:]

print(trois_derniers_elements)  #les trois derniers éléments de la liste est (['oeufs','poison','lait'])

# suppressiondu tuple food_stuff_tp

del food_stuff_tp # la liste food_stuff_tp a été supprimée

# verification dans un tuple

tuple_nordic_countries = ('danemark', 'finland', 'iceland' 'norway', 'sweden')

print( 'estonie' in tuple_nordic_countries ) # false car 'estonie' n'est pas dans le tuple no, des pays nordiques

