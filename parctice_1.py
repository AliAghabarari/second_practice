import random


def decrypt_clue(text):
    mysterious = "ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocalpassraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelifelseexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorpassprintraisereprreturnsupertrywhilewithyieldTrueFalseNoneasyncawaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutprintlnnewMapSetGetAddRemoveClearIsEmptySizeContainsKeyContainsValueKeyValuePairsForEachDoWhileSwitchCaseDefaultbreakcontinueiteratoriterablecollectionsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypeerasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobservermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousprogrammingeventdrivenarchitecturefunctionalprogrammingimmutables...quantumcomputingqubitsentanglementsuperpositionquantumalgorithmsShorsGroverquantumcryptographyquantumteleportationartificialintelligenceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepthfirstsearchbreadthfirstsearchAstaralgorithmgeneticalgorithmssimulatedannealingparticlewarmoptimizationantcolonyoptimizationmachinelearningdeeplearningunsupervisedlearningreinforcementlearningneuralnetworksconvolutionalneuralnetworksrecurrentneuralnetworkslongshorttermmemorynetworksgenerativeadversar...blockchaintechnologydistributedledgerconsensusalgorithmsproofOfWorkproofOfStakeByzantineFaultTolerancepeer-to-peerP2PnetworkscryptographyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigitalcertificatesdigital signaturesmartcontractsdecentralizedapplicationsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNFTsnon-fungibletokensDeFidecentralizedfinancedecentralizedexchangesDEXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypoolsoraclesDAOsdecentralizedautonomousorganizati..."
    a = []
    for i in text:
        if i in mysterious:
            a.append(i)
    return a

def solve_puzzle(text):
    puzzles = ['ali', '1233', '0', '', '[]', '{}', "'False'", "'0'", "'None'",
               'None', '-1', '[1,2,3]',"{'key':'value'}", 'True', "''", "'[]'",
               "'[1,2,3]'", "'{}'", "'{'a':1}'", "'True'", "'ali'", "'1234'", '1',
               '0.1', '-0.1', 'True', "''", "'[]'", "'[1,2,3]'", "'{}'", "'{'a':1}'",
               "'True'", "'ali'", "'1234'", '1', '0.1', '-0.1', 'True', "''", "'[]'",
               "'[1,2,3]'","'{}'", "'{'a':1}'", "'True'", "'ali'", "'1234'", '1', '0.1']
    for i in puzzles:
        if i == '1' or i == 'True':
            text.append(True)
        elif i == '0' or i == 'False':
            text.append(False)
    return text
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

print(keys)

#print(keys)
is_exist = []
is_exist = decrypt_clue(keys)
print(is_exist)

puzzles = []
solve_puzzle(puzzles)

print(puzzles)