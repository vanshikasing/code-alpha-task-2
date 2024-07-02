import time
now = time.ctime()

qna={
    "Hi":"hey",
    "How are you":"I am fine",
    "What is your name":"My name is Vanshika Singh",
    "How old are you":"I am 20 years old",
    "What are you doing now":"I'm doing study in Btech Department of Computer Science and Engineering",
    ""
    "What is the time now": now,
}

while True:
    qs = input()

    if(qs == "quit"):
        break
    else:
        print(qna[qs])