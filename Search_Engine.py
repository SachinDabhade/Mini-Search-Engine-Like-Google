# ****************************** Mini Search Engine Like google ********************************

def matchingWords(sentence1, sentence2,):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score = score + 1
    return score

if __name__ == '__main__':

    while True:
        sentences = ["Sachin is a good boy", "vaibhav is my brother", "Vinayak vasant dabhade is my father", "mandakin dabhade is is is my mother"]
        query = input("\nSearch Engine is ready to work:")
        scores = [matchingWords(query, sentence) for sentence in sentences]
        sortedSentScored = [sentScore for sentScore in sorted(zip(scores, sentences), reverse = True) if sentScore[0] != 0] # This is list comprehension.
        print(f"\n{len(sortedSentScored)} results found...!\n")

        for score, items in sortedSentScored:
            print(f"\"{items}\": with a source of {score}")
        continue

