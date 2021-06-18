import pyttsx3
friend = pyttsx3.init()
friend.say("You cool Brother")
friend.runAndWait()
friend2 = pyttsx3.init()
friend2.say("Hey Buddy")
friend2.runAndWait()

# Input from our voice

word = input("Say something")
friend.say(word)
friend.runAndWait()


# Story from our friend :
friend.say("Hi I want to tell some story")
friend2.say("Sure")
story = "A long time ago there was once a poor boy called Dick Whittington who had no mummy and daddy to look after him so he was often very hungry. He lived in a little village in the country. He’d often heard stories about a far away place called London where everybody was rich and the streets were paved with gold."
friend.say(story)
friend2.say("It was a Great Story!")
friend2.say("Thanks")
friend.runAndWait()
friend2.runAndWait()