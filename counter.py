from collections import Counter

def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    # count the number of email messages from each sender
    try:
        if len(name) < 1 : name = "mbox-short.txt"
        handle = open(name)
        emailCountPerSender = dict()
        for line in handle :
            line = line.strip()
            if line == '' :
                continue
            wordsInThisLine = line.split()
            if len(wordsInThisLine) < 1 :
                continue
            if wordsInThisLine[0] == 'From' :
                emailCountPerSender[wordsInThisLine[1]] = emailCountPerSender.get(wordsInThisLine[1], 0) + 1
        # use Counter class to sort in descending numeric value order
        # this pre-processes data for presentation as a visual histogram
        sortedDict = Counter(emailCountPerSender)
        for entry in sortedDict.most_common() :
            print(entry[0], entry[1])
    except:
        print('File cannot be opened:', name)
        quit()       
## if you want to test locally before you try to sync
## uncomment countEmail() and run > python counter.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## countEmail()
