import random
import time
import turtle

def decrypt_clue(text):
    mysterious = "ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocalpassraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelifelseexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorpassprintraisereprreturnsupertrywhilewithyieldTrueFalseNoneasyncawaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutprintlnnewMapSetGetAddRemoveClearIsEmptySizeContainsKeyContainsValueKeyValuePairsForEachDoWhileSwitchCaseDefaultbreakcontinueiteratoriterablecollectionsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypeerasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobservermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousprogrammingeventdrivenarchitecturefunctionalprogrammingimmutables...quantumcomputingqubitsentanglementsuperpositionquantumalgorithmsShorsGroverquantumcryptographyquantumteleportationartificialintelligenceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepthfirstsearchbreadthfirstsearchAstaralgorithmgeneticalgorithmssimulatedannealingparticlewarmoptimizationantcolonyoptimizationmachinelearningdeeplearningunsupervisedlearningreinforcementlearningneuralnetworksconvolutionalneuralnetworksrecurrentneuralnetworkslongshorttermmemorynetworksgenerativeadversar...blockchaintechnologydistributedledgerconsensusalgorithmsproofOfWorkproofOfStakeByzantineFaultTolerancepeer-to-peerP2PnetworkscryptographyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigitalcertificatesdigital signaturesmartcontractsdecentralizedapplicationsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNFTsnon-fungibletokensDeFidecentralizedfinancedecentralizedexchangesDEXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypoolsoraclesDAOsdecentralizedautonomousorganizati..."
    a = []
    for i in text:
        if i in mysterious:
            a.append(i)
    return a

def solve_puzzle(text):
    puzzles = ['ali', '1233', '0', '""', '[]', '{}', "'False'", "'0'", "'None'", 'None', '-1', '[1, 2, 3]', "{'key': 'value'}", 'True', "' '", "'[]'", "'[1, 2, 3]'", "'{}'", "'{'a': 1}'", "'True'", "'ali'", "'1234'", '1', '0.1', '-0.1', 'True', "' '", "'[]'", "'[1, 2, 3]'", "'{}'", "'{'a': 1}'", "'True'", "'ali'", "'1234'", '1', '0.1', '-0.1', 'True', "' '", "'[]'", "'[1, 2, 3]'", "'{}'", "'{'a': 1}'", "'True'", "'ali'", "'1234'", '1', '0.1', '-0.1']
    for i in puzzles:
        try:
            if (i.startswith("'") and i.endswith("'")) or (i.startswith('"') and i.endswith('"')):
                text.append(bool(i))
            else:
                text.append(bool(eval(i)))
        except NameError:
            text.append(False)


    return text

def calculate_magic_number(start, end):
    r = random.randint(start, end - start)
    a = []
    for i in range(r):
        x = random.randint(start, end)
        a.append(x)
    return a

def exam_number():
    s = time.time()
    x = s
    h = []
    correct = 0
    incorrect = 0
    while True:
        x = time.time()
        if x - s <= 20:
            decimal = 0
            number = []
            for i in range(3, -1, -1):
                r = random.randint(0, 1)
                decimal += r * (2 ** i)
                number.append(r)
            for i in number:
                print(i, end = "")
            print()
            guss = int(input("enter your guss: "))
            h.append(guss == decimal)
            if guss == decimal:
                correct += 1
            else:
                incorrect += 1
        else:
            print("time ended!")
            break
    print(h)
    print(f"correct : {correct}")
    print(f"incorrect: {incorrect}")

keywords = 'False class from or None continue global pass True def if raise and del import return as elif in try assert else is while async except lambda with await finally nonlocalyield break for not'

x = len(keywords)
keys = []
j = 0
for i in range(len(keywords)):
    a = ''
    if keywords[i] == ' ':
        for k in range(j, i):
            a += keywords[k]
        keys.append(a)
        j = i + 1
print("output of first function:")

#print(keys)
is_exist = []
is_exist = decrypt_clue(keys)
print(is_exist)

puzzles = []
solve_puzzle(puzzles)
print("output of second function:")
print(puzzles)

print("output of third function: ")
exam_number()