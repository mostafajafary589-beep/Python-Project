import random

class Hangman:

    
    def __init__(self, param1):
        pass
    
    
    def init(self, words, max_wrong=6):
        self.word = random.choice(words)
        self.guessed = set()
        self.wrong = 0
        self.max_wrong = max_wrong

    def display(self):
        return " ".join(c if c in self.guessed else "_" for c in self.word)

    def guess(self, letter):
        if letter in self.guessed:
            return "كررت هذا الحرف"
        self.guessed.add(letter)
        if letter in self.word:
            return "صح!"
        self.wrong += 1
        return "خطأ!"

    def is_won(self):
        return all(c in self.guessed for c in self.word)

    def is_lost(self):
        return self.wrong >= self.max_wrong

game = Hangman(["python", "coding", "robot", "data"])
while not (game.is_won() or game.is_lost()):
    print(game.display(), f"| أخطاء: {game.wrong}/{game.max_wrong}")
    letter = input("حرف: ").lower().strip()
    if len(letter) != 1 or not letter.isalpha():
        print("أدخل حرفاً واحداً فقط")
        continue
    print(game.guess(letter))
print("فزت! 🎉" if game.is_won() else f"خسرت، الكلمة: {game.word}")