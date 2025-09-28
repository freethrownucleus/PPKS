from professional import Professional, Artist, Scientist, Entrepreneur
import random


artist_enterprise_level = random.randint(1, 10)
scientist_enterprise_level = random.randint(1, 5)
entrepreneur_enterprise_level = random.randint(0, 3)


# Stvaranje objekata za "profesionalce" opcenito
professionals = [
    Professional("Georgia", "O'Keeffe", 89, 8, 120000, "American"),
    Professional("Isaac", "Newton", 64, 10, 140000, "English"),
    Professional("Steve", "Jobs", 56, 9, 180000, "American"),
    Professional("Martha", "Stewart", 80, 7, 150000, "American"),
    Professional("Leonhard", "Euler", 76, 8, 130000, "Swiss")
]

# Stvaranje objekata za slikare 
artists = [
    Artist("Leonardo", "da Vinci", 28, artist_enterprise_level, 100000, "Italian", "Renaissance", 5),
    Artist("Vincent", "van Gogh", 45, artist_enterprise_level, 90000, "Dutch", "Post-Impressionist", 3),
    Artist("Pablo", "Picasso", 33, artist_enterprise_level, 110000, "Spanish", "Cubism", 7),
    Artist("Frida", "Kahlo", 40, artist_enterprise_level, 95000, "Mexican", "Surrealism", 4),
    Artist("Jackson", "Pollock", 50, artist_enterprise_level, 85000, "American", "Abstract Expressionism", 6)
]

# Stvaranje objekata za znanstvenike
scientists = [
    Scientist("Marie", "Curie", 35, scientist_enterprise_level, 120000, "Polish", "Physics", 10),
    Scientist("Albert", "Einstein", 50, scientist_enterprise_level, 150000, "German", "Theoretical Physics", 15),
    Scientist("Stephen", "Hawking", 40, scientist_enterprise_level, 130000, "British", "Cosmology", 12),
    Scientist("Ada", "Lovelace", 38, scientist_enterprise_level, 110000, "British", "Computer Science", 8),
    Scientist("Jane", "Goodall", 45, scientist_enterprise_level, 100000, "British", "Primatology", 6)
]

# Stvaranje objekata za poduzetnike
entrepreneurs = [
    Entrepreneur("Elon", "Musk", 40, entrepreneur_enterprise_level, 200000, "American", "Technology", 3),
    Entrepreneur("Oprah", "Winfrey", 32, entrepreneur_enterprise_level, 180000, "American", "Media", 5),
    Entrepreneur("Jeff", "Bezos", 45, entrepreneur_enterprise_level, 250000, "American", "E-commerce", 7),
    Entrepreneur("Richard", "Branson", 55, entrepreneur_enterprise_level, 220000, "British", "Aviation", 4),
    Entrepreneur("Mark", "Zuckerberg", 48, entrepreneur_enterprise_level, 210000, "American", "Social Media", 6)
]


for prof in professionals: 
    print(prof.name())
    print(prof.achievements())
    print(prof.personal_info())
    print(prof.perform_action())
    print()

for artist in artists:
    print(artist.achievements())
    print(artist.personal_info())
    print(artist.create_masterpiece())
    print(artist.practice())
    print(artist.perform_action())
    print()

for scientist in scientists:
    print(scientist.achievements())
    print(scientist.personal_info())
    print(scientist.conduct_experiment())
    print(scientist.analyze_data())
    print(scientist.perform_action())
    print()

for entrepreneur in entrepreneurs:
    print(entrepreneur.achievements())
    print(entrepreneur.personal_info())
    print(entrepreneur.launch_startup())
    print(entrepreneur.negotiate_deals())
    print(entrepreneur.perform_action())
    print()
    

# Racunanje srednje vrijednosti placa i rangiranje profesionalaca prema placama
avg_salary = Professional.calculate_avg_salary(professionals + artists + scientists + entrepreneurs)
ranked_professionals = Professional.rank_by_salary(professionals + artists + scientists + entrepreneurs)

print("\nAverage salary of these professionals is ${:.2f}.".format(avg_salary))
print("\nProfessionals ranked by their salary:")
for i, prof in enumerate(ranked_professionals):
    print(f"{i+1}. {prof.name()} - ${prof.salary}")
