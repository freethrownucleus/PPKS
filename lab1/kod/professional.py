import random


class Professional:
    def __init__(self, first_name, last_name, age, expertise_level, salary, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = str(age)
        self.expertise_level = expertise_level
        self.salary = salary
        self.nationality = nationality

    def name(self):
        return str(self.first_name + " " + self.last_name)
    
    def personal_info(self):
        return str("Personal information about " + self.name() + " (age, nationality, specialty): "
                   + self.age + ", " + self.nationality + ", " +  "It's necessary to specify the profession!")

    def achievements(self):
        return f"{self.name()} accomplished an achievement. For more details please specify the profession!"

    @staticmethod
    def calculate_avg_salary(professionals):
        total_salary = sum([prof.salary for prof in professionals])
        return total_salary / len(professionals)
 
    @staticmethod
    def rank_by_salary(professionals):
        ranked_professionals = sorted(professionals, key=lambda x: x.salary, reverse=True)
        return ranked_professionals

    def perform_action(self):
        return f"{self.name()} performs a professional action. For more details please specify the profession!"


class Artist(Professional):
    def __init__(self, first_name, last_name, age, expertise_level, salary, nationality, art_style, awards):
        super().__init__(first_name, last_name, age, expertise_level, salary, nationality)
        self.art_style = art_style
        self.awards = awards

    # Polimorfizam
    def personal_info(self):
        return str("Personal information about " + self.name() + " (age, nationality, specialty): "
                   + self.age + ", " + self.nationality + ", " + self.art_style + " art")

    # Polimorfizam
    def achievements(self):
        # enterprise_level € [1, 10]
        if self.expertise_level < 4:
            return f"{self.name()} is still exploring their potential in the world of {self.art_style} art."
        elif 4 <= self.expertise_level < 8:
            return f"{self.name()} has established a unique style in {self.art_style} art and won {self.awards} awards."
        else:
            return f"{self.name()} is a master of {self.art_style} art, with {self.awards} prestigious awards to their name."

    def create_masterpiece(self):
        masterpiece_types = ["painting", "sculpture", "music composition", "poetry"]
        masterpiece = random.choice(masterpiece_types)
        return f"{self.name()} creates a masterpiece {masterpiece}!"

    def practice(self):
        return f"{self.name()} spends hours practicing their art."

    # Polimorfizam
    def perform_action(self):
        actions = ["creates a masterpiece", "practices their art", "showcases their work"]
        action = random.choice(actions)
        return f"{self.name()} {action}."


class Scientist(Professional):
    def __init__(self, first_name, last_name, age, expertise_level, salary, nationality, field, publications):
        super().__init__(first_name, last_name, age, expertise_level, salary, nationality)
        self.field = field
        self.publications = publications

    # Polimorfizam
    def personal_info(self):
        return str("Personal information about " + self.name() + " (age, nationality, specialty): "
                   + self.age + ", " + self.nationality + ", " + self.field + " research")

    # Polimorfizam
    def achievements(self):
        # enterprise_level € [1, 5]
        if self.expertise_level < 2:
            return f"{self.name()} is still grasping the fundamentals of {self.field} research."
        elif 2 <= self.expertise_level < 4:
            return f"{self.name()} has made significant breakthroughs in {self.field} and published {self.publications} papers."
        else:
            return f"{self.name()} is a leading authority in {self.field}, with {self.publications} influential publications to their name."

    def conduct_experiment(self):
        return f"{self.name()} conducts a groundbreaking experiment in {self.field}!"

    def analyze_data(self):
        return f"{self.name()} spends days analyzing the collected data."

    # Polimorfizam
    def perform_action(self):
        actions = ["conducts an experiment", "analyzes data", "publishes a paper"]
        action = random.choice(actions)
        return f"{self.name()} {action}."


class Entrepreneur(Professional):
    def __init__(self, first_name, last_name, age, expertise_level, salary, nationality, industry, ventures):
        super().__init__(first_name, last_name, age, expertise_level, salary, nationality)
        self.industry = industry
        self.ventures = ventures

    # Polimorfizam
    def personal_info(self):
        return str("Personal information about " + self.name() + " (age, nationality, specialty): "
                   + self.age + ", " + self.nationality + ", " + self.industry + " industry")

    # Polimorfizam
    def achievements(self):
        # enterprise_level € [0, 3]
        if self.expertise_level < 1:
            return f"{self.name()} is navigating the challenges of the {self.industry} industry."
        elif 1 <= self.expertise_level <= 2:
            return f"{self.name()} has successfully launched and sustained {self.ventures} ventures in the {self.industry} sector."
        else:
            return f"{self.name()} is a titan of the {self.industry} industry, with {self.ventures} successful ventures reshaping global markets."

    def launch_startup(self):
        return f"{self.name()} successfully launches a startup in the {self.industry} industry!"

    def negotiate_deals(self):
        return f"{self.name()} negotiates lucrative deals for their company."

    # Polimorfizam
    def perform_action(self):
        actions = ["launches a startup", "negotiates deals", "networks"]
        action = random.choice(actions)
        return f"{self.name()} {action}."
