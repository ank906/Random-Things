import pyautogui
import time
def start():
    words = ["This", "is", "for", "Rachel", "you", "big", "fat", "white", "nasty", "smelling", "fat", "bitch", "why", "you", "took", "me", "off", "the",
            "motherfucking", "schedule", "with", "your", "trifling", "dirty", "white", "racist", "ass", "you", "big", "fat", "bitch", "oompa", "loompa", "body",
            "ass", "bitch", "I'm", "coming", "outside", "and", "I'm", "going", "to", "beat", "the", "fuck", "out", "of", "you", "bitch", "and", "don't", "even",
            "call", "the", "police", "today", "because", "I'm", "gonna", "come", "unexpected", "and", "wait", "on", "yo", "motherfucking", "ass", "bitch",
            "I'm", "going", "to", "beat", "the", "fuck", "out", "of", "you", "bitch", "cause", "you", "did", "that", "on", "purpose", "with", "your", "aundry",
            "racist", "white", "ass", "danhard", "bitch", "watch", "I'm", "coming", "bout", "to", "fuck", "you", "up", "bitch", "I'm", "telling", "you",
            "watch", "I", "know", "what", "kind", "of", "car", "you", "drive", "I'm", "gonna", "wait", "on", "you", "and", "I'm", "gonna", "beat", "yo", "ass",
            "bitch", "cause", "I'mma", "show", "you", "not", "to", "play", "with", "Jasmine's", "money", "bitch", "that's", "the", "first", "thing", "you",
            "did", "and", "you", "got", "me", "fucked", "up", "cause", "bitch", "I", "told", "you", "what", "the", "fuck", "was", "going", "on", "you", "white",
            "motherfuckers", "hate", "to", "see", "black", "people", "doing", "good", "or", "doing", "goodanything", "for", "their", "motherfucking", "selfs",
            "ugly", "fat", "white", "bitchwatch", "I'm", "telling", "you", "I'm", "coming", "outside", "beat", "yo", "motherfucking", "ass", "danhard",
            "smelly", "white", "dog", "smelling", "ass", "bitch", "watch", "I'll", "come", "and", "fuck", "you", "up", "cause", "you", "got", "me", "fucked",
            "up", "we", "see", "you", "trynna", "do", "that", "old", "audnry", "ass", "shit", "bitch", "you", "aundry", "the", "first", "day", "I", "came",
            "up", "there", "talking", "about", "a", "bitch", "who", "had", "pajamas", "but", "you", "walking", "around", "here", "wearing", "those", "10$",
            "ass", "jeans", "on", "dirty", "dusty", "white", "bitch", "sitting", "up", "behind", "that", "counter", "smelling", "like", "cheese", "bitch",
            "stinky", "fat", "white", "ass", "bitch", "are", "you", "gonna", "not", "try", "to", "answer", "this", "phone", "I'm", "coming", "to", "fuck",
            "you", "up", "I'm", "telling", "you", "you", "better", "remember", "who", "I", "am", "cause", "bitch", "you", "gonna", "run", "when", "you", "see",
            "me", "cause", "I'm", "gonna", "fuck", "you", "up", "bitchyou", "wanna", "sit", "here", "and", "play", "with", "me", "about", "my", "motherfucking",
            "money", "wanna", "play", "about", "my", "motherfucking", "money", "bitch", "wanna", "sit", "up", "there", "and", "try", "to", "do", "that",
            "bitch", "little", "do", "you", "know", "little", "do", "you", "know", "I", "know", "enough", "people", "watch", "I'm", "coming", "to", "fuck",
            "you", "up", "I", "promise", "you", "that", "I", "promise", "you", "I'm", "coming", "to", "fuck", "you", "up", "you", "fat", "stinky", "white",
            "bitch", "danhard", "yellow", "yuck", "mouth", "nasty", "mouth", "ass", "bitch", "you", "stink", "you", "smell", "like", "fucking", "cheese", "you",
            "got", "that", "trifiling", "ass", "attitude", "I'mma", "beat", "that", "attitude", "up", "out", "you", "bitch", "watch", "you", "treat",
            "everybody", "like", "that", "all", "these", "black", "people", "that", "you", "do", "like", "that", "you", "in", "the", "wrong", "position", "you",
            "trifling", "ass", "racist", "ass", "bitch", "that's", "why", "nobody", "fuck", "with", "you", "you", "trifling", "and", "you", "racist", "bitch",
            "should've", "fine", "did", "all", "that", "shit", "when", "I", "told", "you", "what", "the", "fuck", "going", "on", "gonna", "tell", "me", "I",
            "worked", "at", "that", "motherfucking", "job", "when", "I", "telling", "you", "the", "fuck", "I", "didnt", "bitch", "why", "the", "fuck", "would",
            "I", "lie", "about", "shit", "like", "that", "watch", "I", "finna", "come", "outside", "and", "beat", "yo", "motherfucking", "ass", "you", "better",
            "not", "get", "out", "that", "motherfucking", "car", "bitch", "Im", "telling", "you", "fucking"]
    print("starting in 5 seconds")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("5")
    place = -1
    while place != 504:
        place += 1
        pyautogui.write(words[place])
        pyautogui.press('enter')
    if (place == 504):
        print("Completed!")
print("info:\nThis script types out all 505 words so it will take a bit make sure the program\nis open and ready as you only have 5 seconds to click the text box \n[press enter to continue]")
con = input("")
if con == "":
    start()

