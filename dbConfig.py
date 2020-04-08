import  nltk
from nltk import load_parser
from nltk.sem import chat80
from nltk.sem import cooper_storage as cs







#LogicParser
def LogicParser():
    read_expr = nltk.sem.Expression.fromstring
    read_expr('-(P & Q)')
    read_expr('P & Q')
    read_expr('P | (R -> Q)')
    read_expr('P <-> -- P')

#Syntactic validity
def syntactic_validity():
    lp = nltk.sem.Expression.fromstring
    SnF = read_expr('SnF')
    NotFnS = read_expr('-FnS')
    R = read_expr('SnF -> -FnS')
    prover = nltk.Prover9()
    prover.prove(NotFnS, [SnF, R])

#valuation
def valuation():
    val = nltk.Valuation([('P', True), ('Q', True), ('R', False)])
    print(val['P'])

#model
def logic_form():
    val = nltk.Valuation([('P', True), ('Q', True), ('R', False)])
    dom = set()
    g = nltk.Assignment(dom)
    m = nltk.Model(dom,val)
    print(m.evaluate('(P & Q)', g))
    print(m.evaluate('-(P & Q)', g))
    print(m.evaluate('(P & R)', g))
    print(m.evaluate('(P | R)', g))


def queryMake():
    #cp = load_parser('sql0.fcfg')
    #query = 'What cities are located in China'

    cp = load_parser('sql1.fcfg')
    query = 'What cities are in China and have populations above 1,000,000'


    trees = next(cp.parse(query.split()))
    answer = trees[0].label()['SEM']
    answer = [s for s in answer if s]
    q = ' '.join(answer)
    rows = chat80.sql_query('corpora/city_database/city.db', q)
    for r in rows:
        print(r[0])








#First Order Logic
def first_order_logic():
    read_expr = nltk.sem.Expression.fromstring
    expr = read_expr('walk(angus)', type_check=True)
    print(expr.argument)
    print(expr.argument.type)
    print(expr.function)
    print(expr.function.type)
    sig = {'walk': '<e, t>'}
    expr = read_expr('walk(angus)', signature=sig)
    print(expr.function.type)

    read_expr('dog(cyril)').free()
    set()
    print(read_expr('dog(x)').free())
    print(read_expr('own(angus, cyril)').free())
    set()
    read_expr('exists x.dog(x)').free()
    set()
    print(read_expr('((some x. walk(x)) -> sing(x))').free())
    print(read_expr('exists x.own(y, x)').free())





#3.4 Truth Model
def truthModel():
    dom = {'b','o','c'}
    v = """
    bertie => b
    olive => o
    cyril => c
    boy => {b}
    girl => {o}
    dog => {c}
    walk => {o, c}
    see => {(b, o), (c, b), (o, c)}
    """
    val = nltk.Valuation.fromstring(v)
    print(val)
    print(('o', 'c') in val['see'])
    print(('b',) in val['boy'])
    #individual variable assignemt
    g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
    print(g)
    #Evaluate atomic formula of firt order logic

    m = nltk.Model(dom, val)
    m.evaluate('see(olive, y)', g)
    print(g['y'])
    m.evaluate('see(y, x)', g)

    #quantification
    print(m.evaluate('exists x.(girl(x) & walk(x))', g))
    print(m.evaluate('girl(x) & walk(x)', g.add('x', 'o')))

    read_expr = nltk.sem.Expression.fromstring
    fmla1 = read_expr('girl(x) | boy(x)')
    m.satisfiers(fmla1, 'x', g)

    fmla2 = read_expr('girl(x) -> walk(x)')
    m.satisfiers(fmla2, 'x', g)
    fmla3 = read_expr('walk(x) -> girl(x)')
    m.satisfiers(fmla3, 'x', g)

    #Quantifier Scope Ambiguity
    v2 = """
    bruce => b
    elspeth => e
    julia => j
    matthew => m
    person => {b, e, j, m}
    admire => {(j, b), (b, b), (m, e), (e, m)}
    """
    val2 = nltk.Valuation.fromstring(v2)
    dom2 = val2.domain

    m2 = nltk.Model(dom2, val2)
    g2 = nltk.Assignment(dom2)
    fmla4 = read_expr('(person(x) -> exists y.(person(y) & admire(x, y)))')
    print(m2.satisfiers(fmla4, 'x', g2))

    fmla5 = read_expr('(person(y) & all x.(person(x) -> admire(x, y)))')
    print(m2.satisfiers(fmla5, 'y', g2))
    set()

    fmla6 = read_expr('(person(y) & all x.((x = bruce | x = julia) -> admire(x, y)))')
    print(m2.satisfiers(fmla6, 'y', g2))


    #Model Building
    a3 = read_expr('exists x.(man(x) & walks(x))')
    c1 = read_expr('mortal(socrates)')
    c2 = read_expr('-mortal(socrates)')
    mb = nltk.Mace(5)
    print(mb.build_model(None, [a3, c1]))
    print(mb.build_model(None, [a3, c2]))
    print(mb.build_model(None, [c1, c2]))

    a4 = read_expr('exists y. (woman(y) & all x. (man(x) -> love(x,y)))')
    a5 = read_expr('man(adam)')
    a6 = read_expr('woman(eve)')
    g = read_expr('love(adam,eve)')
    mc = nltk.MaceCommand(g, assumptions=[a4, a5, a6])
    mc.build_model()

    print(mc.valuation)

    a7 = read_expr('all x. (man(x) -> -woman(x))')
    g = read_expr('love(adam,eve)')
    mc = nltk.MaceCommand(g, assumptions=[a4, a5, a6, a7])
    mc.build_model()

    print(mc.valuation)


#Sementics of English Language
#The λ-Calculus
def calculus():
    read_expr = nltk.sem.Expression.fromstring
    expr = read_expr(r'\x.(walk(x) & chew_gum(x))')
    expr
    expr.free()
    print(read_expr(r'\x.(walk(x) & chew_gum(y))'))


def betareduction():
    read_expr = nltk.sem.Expression.fromstring
    expr = read_expr(r'\x.(walk(x) & chew_gum(x))(gerald)')
    print(expr)
    print(expr.simplify())

    print(read_expr(r'\x.\y.(dog(x) & own(y, x))(cyril)').simplify())
    print(read_expr(r'\x y.(dog(x) & own(y, x))(cyril, angus)').simplify())

    expr1 = read_expr('exists x.P(x)')
    print(expr1)
    expr2 = expr1.alpha_convert(nltk.sem.Variable('z'))
    print(expr2)

    expr3 = read_expr('\P.(exists x.P(x))(\y.see(y, x))')
    print(expr3)
    print(expr3.simplify())



#Transitive Verbs
def transitiveVerbs():
    read_expr = nltk.sem.Expression.fromstring
    tvp = read_expr(r'\X x.X(\y.chase(x,y))')
    np = read_expr(r'(\P.exists x.(dog(x) & P(x)))')
    vp = nltk.sem.ApplicationExpression(tvp, np)
    print(vp)
    print(vp.simplify())



#simple-sem.fcfg
def simple_sem():
    parser = load_parser('simple-sem.fcfg', trace=0)
    sentence = 'Angus gives a bone to every dog'
    tokens = sentence.split()

    for tree in parser.parse(tokens):
        print(tree.label()['SEM'])

    sents = ['Irene walks', 'Cyril bites an ankle']
    grammar_file = 'simple-sem.fcfg'

    for results in nltk.interpret_sents(sents, grammar_file):
        for (synrep, semrep) in results:
            print(synrep)

    v = """
    bertie => b
    olive => o
    cyril => c
    boy => {b}
    girl => {o}
    dog => {c}
    walk => {o, c}
    see => {(b, o), (c, b), (o, c)}
    """
    val = nltk.Valuation.fromstring(v)
    g = nltk.Assignment(val.domain)
    m = nltk.Model(val.domain, val)
    sent = 'Cyril sees every boy'
    grammar_file = 'simple-sem.fcfg'
    results = nltk.evaluate_sents([sent], grammar_file, m, g)[0]
    for (syntree, semrep, value) in results:
        print(semrep)
        print(value)



#Quantifier Ambiguity Revisited
def quantifier_ambiguity_revisited():
    sentence = 'every girl chases a dog'
    trees = cs.parse_with_bindops(sentence, grammar='storage.fcfg')

    semrep = trees[0].label()['SEM']
    cs_semrep = cs.CooperStore(semrep)
    print(cs_semrep.core)
    for bo in cs_semrep.store:
        print(bo)
    cs_semrep.s_retrieve(trace=True)

    for reading in cs_semrep.readings:
        print(reading)


#discourse semantics
def discouse_semantics():
    read_dexpr = nltk.sem.DrtExpression.fromstring
    drs1 = read_dexpr('([x, y], [angus(x), dog(y), own(x, y)])')
    print(drs1)
    print(drs1.fol())

    #concatenation of 2
    drs2 = read_dexpr('([x], [walk(x)]) + ([y], [run(y)])')
    print(drs2)
    print(drs2.simplify())

    drs3 = read_dexpr('([], [(([x], [dog(x)]) -> ([y],[ankle(y), bite(x, y)]))])')
    print(drs3.fol())

    drs4 = read_dexpr('([x, y], [angus(x), dog(y), own(x, y)])')
    drs5 = read_dexpr('([u, z], [PRO(u), irene(z), bite(u, z)])')
    drs6 = drs4 + drs5
    print(drs6.simplify())

    print(drs6.simplify().resolve_anaphora())

    parser = load_parser('drt.fcfg', logic_parser=nltk.sem.drt.DrtParser())
    trees = list(parser.parse('Angus owns a dog'.split()))
    print(trees[0].label()['SEM'].simplify())



#discourse processing
def discourse_processing():
    dt = nltk.DiscourseTester(['A student dances', 'Every student is a person'])
    dt.readings()
    dt.add_sentence('No person dances', consistchk=True)
    dt.retract_sentence('No person dances', verbose=True)
    dt.add_sentence('A person dances', informchk=True)



from nltk.tag import RegexpTagger
def tagger():
    tagger = RegexpTagger([('^(chases|runs)$', 'VB'),
            ('^(a)$', 'ex_quant'),
            ('^(every)$', 'univ_quant'),
            ('^(dog|boy)$', 'NN'),
            ('^(He)$', 'PRP')])

    rc = nltk.DrtGlueReadingCommand(depparser=nltk.MaltParser(tagger=tagger))
    dt = nltk.DiscourseTester(['Every dog chases a boy', 'He runs'], rc)
    dt.readings()

if __name__ == '__main__':
    queryMake()
    LogicParser()
    valuation()
    logic_form()
    first_order_logic()
    truthModel()
    calculus()
    betareduction()
    transitiveVerbs()
    simple_sem()
    quantifier_ambiguity_revisited()
    discouse_semantics()
    discourse_processing()
    tagger()




