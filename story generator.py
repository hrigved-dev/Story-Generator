import random

# Introduction and taking the input for the characters name
print("WELCOME TO YOUR VERY OWN STORY \n")
character = input("Enter the protagonist's name: ")
enemy = input("Enter the opponent's name: ")
print("\n")
enemyadj = ["cunning", "ugly", "wicked", "beast-like", "evil", "furious", "disorganized", "bitter", "mindless", "crooked", "unseen"]

#Part of the story which will be selected
intro1 = "Once upon a time there was a knight called "+character+ " who was very hardworking and wanted to serve for the King. The King was very generous and always had a soft corner for "+character+". The Knight considered himself to be pretty content with his life." 
intro2 = "There lived a person named "+character+" who was good at everything he did."+character+" had a pretty good life and had everything sorted. He had money, famevand a motive to live. He was a happy person."
intro3 = "A person named "+character+" lived in the busy streets of Baghdad. Begging all day to get a meal to eat was the routine. The clothes ripped and the hair so untidy that the face was hardly seen."+character+" had accepted his conditions and was content with his living. He had no expectations out of his life."
prob1 = "One day when " + character + " was moving around the city, he encountered a meet with a " + random.choice(enemyadj) + " person called " + enemy + ". He wanted to take everything from " + character + " and wanted to leave him nothing. The bad guy attacked him and took away everything that he had " + character + " in order to save himself could not do a thing."
prob2 = "There was something unusual going on around. Everything seemed to be in chaos and it just didn't feel right. " + character + " tried to move around the city to check what was wrong, when he saw a " + random.choice(enemyadj) + " person named " + enemy + ". " + enemy + " was known for his brutal nature and always left the people helpless. He demanded " + character + " to leave everything that he had on the ground and leave. But " + character + " refused. So " + enemy + " attacked him and took everything that he had leaving him with nothing but with his life."
prob3 = character + " didn't feel good one day. Nothing seemed normal. Everything seemed to be in a chaos. To dig deeper into the matter " + character + " decided to check what was going around. When he reached a dense forest he found a " + random.choice(enemyadj) + " person named " + enemy + ". " + character + " did not find it safe to be around the hound and ran for his life. But " + enemy + " finally caught him and took every last thing that he had."
sol1 = " Now " + character + " was all broken as he had nothing with him. He had no motive to live and was depressed. He wanted a real source so as to make him happier again and start a new life. He left the city which was already in a turmoil in a hope that he will find a better place to start a new life. On his way, he met a monk. The monk immediately understood that something was wrong with " + character + ". The monk advised " + character + " to come with him to the monaestry and live a monk's life there. " + character + " agreed to the monk's advice and left for the monaestry."
sol2 = "After this " + character + " had lost everything and was ashamed and sad. He felt as if there was no land under his foot. He wandered around but did not find any hope of living. When " + character + " was moving to a new city, he found a baby lying on the roadside. Immediately, his heart melted and he took the baby in his arms. He found a new home in the new city and lived there with the baby."
sol3 = character + " after facing all this was completely broken. He wanted his life to be as it was earlier where he was content with everythig that he had. He found a family living in a hut and asked them for accomodation.They agreed and " + character + " started living with them. He had started smiling finally and the family too were happy to keep " + character + " in thei home." 
end1 = "After five years " + character + " had finally set himself free of every greed and lived happily ever-after."
end2 = "Then after a huge span of time, " + character + " finally learnt to stay happy and he continued to stay like that forever."
end3 = "As time passed, " + character + " realised the real meaning of life and was happy and content again."


#Selecting random from the lists
intros = [intro1, intro2, intro3]
problems = [prob1, prob2, prob3]
solutions = [sol1, sol2, sol3]
endings = [end1, end2, end3]

#Printing the random story
print(random.choice(intros))
print(random.choice(problems))
print(random.choice(solutions))
print(random.choice(endings))