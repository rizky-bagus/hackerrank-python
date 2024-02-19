# Enter your code here. Read input from STDIN. Print output to STDOUT
number_of_english_subscribers = input()
english_subscribers = set(map(int, input().split()))
number_of_french_subscribers = input()
french_subscribers = set(map(int, input().split()))
print(len(english_subscribers.difference(french_subscribers)))