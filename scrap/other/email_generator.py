import pyperclip as pc

#"college", "name", "role" 
my_dict = {'Christ\'s': ['Sam', 'JCR President'], 'Christ\'s': ['Camille', 'JCR Green Officer'], 'Christ\'s': ['Julie', 'MCR Green Officer'], 'Christ\'s': ['Juliane', 'MCR President'], 'Churchill': ['President', 'JCR President'], 'Churchill': ['Nick', 'MCR Green Officer'], 'Churchill': ['Michaela', 'MCR President'], 'Clare': ['Lily', 'JCR President'], 'Clare': ['Ruairidh, David', 'Green Officer'], 'Clare': ['Sammie', 'MCR President'], 'Clare Hall': ['Srijit', 'President'], 'Clare Hall': ['Lydia', 'Green Officer'], 'Corpus': ['Jamie', 'JCR President'], 'Corpus': ['Kitty', 'JCR Green Officer'], 'Corpus': ['Lina', 'MCR Green Officer'], 'Corpus': ['Isabella', 'MCR President'], 'Darwin': ['Fariza', 'International Officer interested in environmentalism'], 'Darwin': ['Megan', 'Environmental Affairs Officer'], 'Darwin': ['Daniel', 'DCSA President'], 'Downing': ['Liam', 'President'], 'Downing': ['Antonia, Miles', 'Green Officer'], 'Downing': ['Caitlin', 'President'], 'Emma': ['Sawen','President'], 'Emma': ['Morwenna', 'Accommondation and Environment Officer'], 'Emma': ['Mia', 'Green Officer'], 'Emma': ['Aadi', 'MCR President'], 'Caius': ['Natalia', 'JCR President'], 'Caius': ['Clarissa', 'Green Officer'], 'Caius': ['Julian', 'MCR President'], 'Hughes Hall': ['Janina', 'Ethical and Environmental Officer'], 'Hughes Hall': ['Kudzai', 'MCR President'], 'Jesus': ['Jezz', 'President'], 'Jesus': ['Georgia', 'Green Officer'], 'Jesus': ['Charlotte', 'MCR President'], 'Jesus': ['Kefeshe', 'Green Officer'], 'King\'s': ['President', 'President'], 'King\'s': ['Bethan', 'Environment Officer'], 'King\'s': ['Sergio', 'President'], 'Magdalene': ['Harry', 'President'], 'Magdalene': ['James', 'Green Officer'], 'Medwards':['Sophie', 'Green Officer'], 'Medwards': ['Ruby', 'President'], 'Medwards': ['Dianna', 'President'], 'Medwards': ['Lea', 'MCR Green Officer'], 'Newnham' : ['Charlotte', 'Green and Ethical Affairs Officer'], 'Newnham' : ['Hanna', 'JCR President'], 'Pembroke': ['Bella', 'Charities Officer'], 'Pembroke': ['Arden', 'Environment Officer'], 'Pembroke': ['Ira', 'President'], 'Peterhouse': ['Kam', 'President'], 'Peterhouse': ['Georgia', 'President'], 'Peterhouse': ['Josey', 'President'], 'Queen\'s':['Shukri', 'Environment Officer'], 'Queen\'s':['Saiorse', 'Environment Officer'], 'Queen\'s': ['Juliette', 'President'], 'Queen\'s':['Jed', 'President'], 'Robinson\'s':['Jamie', 'Green Officer'], 'Robinson\'s': ['Green Officer', 'Green Officer'], 'Robinson\'s':['Caroline, Christopher', 'President'], 'Robinson\'s':['Tamsin', 'President'], 'Selwyn': ['Ollie', 'Green Officer'], 'Selwyn': ['Chloe', 'Green Officer'], 'Selwyn':['Bella', 'President'], 'Selwyn':['Elsa', 'President'], 'Sidney Sussex':['Rosa', 'Green and Ethical Affairs Officer'], 'Sidney Sussex': ['Miguel', 'Green Officer'], 'Sidney Sussex':['Skyler', 'JCR President'], 'Sidney Sussex':['Jinal', 'President'], 'St Catherine\'s':['Zsófi, Emilia', 'Ethical and Environmental Officers'], 'St Catherine\'s':['Sam', 'Green Officer'], 'St Catherine\'s':['Ammie', 'President'] ,'St Catherine\'s':['Souradip, Ashirbad', 'Co-President'], 'St Edmunds':['Minnie', 'Environment Officer'], 'St Edmunds':['Liane', 'President'], 'St Johns':['Ed', 'Ethical Affairs Officer'], 'St Johns':['Margherita', 'Environment Officer'], 'St Johns':['Sophia', 'Environment Officer'], 'St Johns':['Sarah, Maryam', 'Co-President'], 'St Johns':['Dillon', 'SBR President'], 'Trinity': ['William', 'Environment Officer'], 'Trinity': ['Tayla', 'President'], 'Trinity Hall': ['Rosie', 'Green and Ethics Officer'], 'Trinity Hall': ['Joshua, Zephyr', 'Green and Ethical Affairs Officer'], 'Trinity Hall': ['Sam', 'President'], 'Wolfson': ['Sachi', 'Green Officer'], 'Wolfson':['Scott', 'President']}


text_base1 = "Dear "
text_base2 = ",\n\nI am a student from Girton College, and I am running a campaign here in Cambridge to generate awareness about a key ecological issue; soil degradation.\n\nGlobally, 52 percent of agricultural soils are already degraded. (ELD Initiative, 2015), and the UN predicts severe food shortages that will result from this continued fast-paced desertification across the world. With public pressure, we can push governments to put soil health, and other key ecological issues, as part of their policies, and elect on basis of environmental policy.\n\nTo help reach students at Cambridge, and in "
text_base3 = " specifically, I need your help as "
text_base4 = ", and other committee members who feel strongly about environmentalism, to help in publicising this very poorly known ecological issue at your college."
text_base5 = "\n\nThis is posed to develop into a serious problem within our lifetime. Please reply expressing interest/disinterest, and feel free to ask any further questions about the issue!\n\nThank you,\nShashvat Verma\nPresident at Cambridge University Save Soil Society"


for college, value in my_dict.items():
    namee = str(value[0])
    role = str(value[1])
    college = str(college)
    a1 = text_base1 + namee + text_base2 + college + text_base3 + role + text_base4 + text_base5
    pc.copy(a1)
    print(a1)
    print(namee)
    print(college)
    input("Press Enter to continue...")