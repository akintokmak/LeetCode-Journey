class Solution(object):
    def __init__(self,word1,word2):
        self.word1 = word1
        self.word2 = word2
        self.list1 = []
        self.list2 = []
        self.list3 = []
        self.count = 1
        self.count2 = 1

    def mergeAlternately(self):
        for letter in range((len(self.word1)+(len(self.word1)))):
            if letter % 2 != 0:
                self.list1.append(' ')
            else:
                if letter != 0:
                    letter -= self.count
                    self.count += 1
                self.list1.append(self.word1[letter])
        self.count = 1
        for letter in range((len(self.word2)+(len(self.word2)))):
            if letter % 2 == 0:# 0 1 2 3 4 5
                self.list2.append(' ')
            else:
                letter -= self.count
                self.count +=1
                self.list2.append(self.word2[letter])
        self.count = 1
        self.count2 = 1
        for letter in range((len(self.word2)+(len(self.word2)))):
            if letter % 2 == 0:
                if letter != 0:
                    letter -= self.count
                    self.count += 1
                self.list3.append(self.word1[letter])
            else: # 0 1 2 3 4 5
                letter -= self.count2
                self.count2 +=1
                self.list3.append(self.word2[letter])

        print(self.list1)
        print(self.list2)
        print(self.list3)

slt = Solution(word1="ab",word2="pq")
slt.mergeAlternately()





