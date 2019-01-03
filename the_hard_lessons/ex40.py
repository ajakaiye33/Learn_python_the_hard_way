class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics


    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)



happy_bday = Song(["Happy birthday to you",
                " I don't want to get sued",
                "So I 'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of sheels"])


happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()


#drils
tupac_shakur = Song([" I love you",
                     " I love you",
                     "You are appreciated",
                     "When I was young me and my mama had a beef",
                     "Seventeen years old kicked out on the streets",
                     "Though back at the time, I never thought I'd see her face",
                     "Ain't a woman alive that could take my mama's place",
                     "Suspended from school, and scared to go home, I was a fool",
                     "With the big boys, breaking all the rules",
                     "I shed tears with my baby sister",
                     "Over the years we was poorer than the other little kids",
                     "And even though we had different daddy's, the same drama",
                     "When things went wrong we'd blame mama",
                     "I reminisce on the stress I caused, it was hell",
                     "Hugging on my mama from a jail cell",
                     "And who'd think in elementary?",
                     "Hey! I see the penitentiary, one day",
                     "And running from the police, that's right",
                     "Mama catch me, put a whooping to my backside",
                     "And even as a crack fiend, mama",
                     "You always was a black queen, mama",
                     "I finally understand",
                     "For a woman it ain't easy trying to raise a man",
                     "(I know it ain't easy)",
                     "You always was committed",
                     "A poor single mother on welfare, tell me how ya did it",
                     "There's no way I can pay you back",
                     "But the plan is to show you that I understand",
                     "You are appreciated",
                     "Dear mama",
                     "Don't you know I love you?",
                     "Dear mama",
                     "Place no one above you",
                     "(Dear mama) Oh mama, I appreciate you",
                     "Although my shadow's gone",
                     "I will never leave you"])

tupac_shakur.sing_me_a_song()
