'''
1. Product Review Analysis
Objective:
The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

Task 1: Keyword Highlighter

Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". 
Print out each review with the keywords in uppercase so they stand out.
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review. 
Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.
'''


def uppercase_positive(review):
    final_string = ""
    for word in review:
            word = word.split()
            for wor in word:
                if wor == "good." or wor == "excellent." or wor == "bad" or wor == "Poor" or wor == "average.":
                  wor = wor.upper()
                  final_string += wor
                  final_string += " "
                else:
                  final_string += wor 
                  final_string += " "
                
    print(final_string)

def tally_words(review, pos_words, neg_words):
    pos_tally = 0
    neg_tally = 0
    for word in review:
            word = word.replace(".", "")
            word = word.lower()
            word = word.replace("!", "").split()
            for wor in word:
                 if wor in pos_words:
                      pos_tally += 1
                 elif wor in neg_words:
                      neg_tally += 1
    print(f"Total Positive words: {pos_tally}\n Total Negative words: {neg_tally}")

def summary():

    while True:
        summary = str(input("Please provide a review. Keep in mind it should only be 30 characters or less and should end with proper puncutation! "))
        if len(summary) <= 30:
            if summary[-1] == '.' or summary[-1] == '!':
              print(summary)
              break
            else:
              print("Need to end your summary with proper puncuation!")
        else:
            print("Your summary has more than 30 characters (spaces included)!")
                        
    
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar", "average"]
tally_words(reviews, positive_words, negative_words)
uppercase_positive(reviews)

while True:
    summ = str(input("Welcome! would you like to write a summary? (yes/no) ").lower())
    if summ == 'yes':
         summary()
    elif summ == 'no':
         break
    else:
         print("Invalid choice")

