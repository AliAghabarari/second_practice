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
                text.append(str(bool(i)))
            else:
                text.append(str(bool(eval(i))))
        except NameError:
            text.append("False")


    return text

def calculate_magic_number(start, end):
    a = []
    for i in range(10):
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
            h.append(str(guss == decimal))
            if guss == decimal:
                correct += 1
            else:
                incorrect += 1
        else:
            print("time ended!")
            break
    return h, f"correct : {correct}" , f"incorrect: {incorrect}"

def check_pass():
    person = []
    j = 1
    while True:
        s = 0
        name = input("enter name: ")
        while bool(name) == False:
            name = input("enter name again: ")
        if name == "quit":
            break
        print(f"person {j} name is: {name}")
        password = input("enter pssword: ")
        while bool(password) == False:
            password = input("enter password again:")

        capital_letter = 0
        small_letter = 0
        character = 0
        print(f"password of person {j} is: {password}")
        lengh = 0
        if 8 <= len(password):
            lengh = 1
        for i in password:
            if (ord(i) < 65 and 32 < ord(i)) or (ord(i) < 97 and 90 < ord(i)) or (ord(i) < 127 and 122 < ord(i)):
                character = 1
            if 65 <= ord(i) and ord(i) <= 90:
                capital_letter = 1
            if 97 <= ord(i) and ord(i) <= 122:
                small_letter = 1
        if lengh == 1 and (character == 1 or capital_letter == 1) and small_letter == 1:
            person.append(name)
        j += 1
    if bool(person) == False:
        return("not found!!")
    else:
        return person

def shape():
    x = turtle.Screen()
    s = turtle.Turtle()
    s.penup()
    s.goto(200, 100)
    s.rt(90)
    s.pendown()
    s.pensize(5)
    s.fd(100)
    s.rt(90)
    s.fd(40)
    s.rt(90)
    s.fd(100)
    s.penup()
    s.lt(90)
    s.fd(10)
    s.lt(90)
    s.fd(70)
    s.pendown()
    s.forward(30)
    s.rt(90)
    s.fd(50)
    s.penup()
    s.goto(130, 40)
    s.pendown()
    s.dot(10)
    s.penup()
    s.goto(115, 40)
    s.pendown()
    s.dot(10)
    s.penup()
    s.goto(100, 0)
    s.lt(70)
    s.pendown()
    s.fd(70)
    s.rt(70)
    s.fd(20)
    s.penup()
    s.goto(-10, 40)
    s.pendown()
    s.rt(150)
    s.fd(40)
    s.rt(70)
    s.fd(70)
    s.rt(140)
    s.fd(140)
    s.lt(90)
    s.fd(30)
    s.lt(90)
    s.fd(30)
    s.rt(90)
    s.fd(60)
    s.rt(90)
    s.fd(80)
    s.rt(90)
    s.fd(80)
    s.penup()
    s.goto(20, -5)
    s.pendown()
    s.dot(10)
    x.mainloop()



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
print("*********************")
puzzles = []
solve_puzzle(puzzles)
print("output of second function:")
print(puzzles)
print("*********************")
print("output of third function: ")
start , end = map(int, input("enter star and end: ").split())
x = calculate_magic_number(start, end)
print(calculate_magic_number(start, end))
print("************************")
print("output of fourth function: ")
ls = []
ls.append(exam_number())
print(ls)
print("************************")
print("fifth function: ")
ls2 = []
ls2.append(check_pass())
print(ls2)
shape()

def unlock_vault(clues):
    clues.append(is_exist[0][0])
    clues.append(puzzles[0][0])
    clues.append(x[0])
    clues.append(ls[0][0][0][0])
    clues.append(ls2[0][0][0])
    print("*******************")
    print("the key of vault is:", end = "    ")
    for i in clues:
        print(i, end = "")
clues = []

unlock_vault(clues)