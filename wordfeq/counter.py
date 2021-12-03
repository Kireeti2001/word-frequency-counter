
f = open("text.txt","r")
lines = f.readlines()
f.close()


#making everything lower case 

length =len(lines)
for i in range(length):
    lines[i]=lines[i].lower()

#removing puncuations

chars_to_replace = ['\n','.','_','-','!','{','}','[',']','?',',',';',':',"'"]
for i in range(length):
    for s in chars_to_replace:
        lines[i] = lines[i].replace(s,' ')

# converting everything into strings
text = " ".join(lines)
words = text.split()


#counting freq
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# sorting the dict by alphabetical order
sorted_list_alpha = sorted(word_freq.items())

# sorting the dict by frequency
sorted_list_freq = sorted(word_freq.items(),key=lambda item: item[1],reverse= False)

sorted_list_freq.reverse()

with open('words_with_frequencies.txt','w') as f_out:
    for item in sorted_list_freq[:]:
        f_out.write(item[0]+"--->"+str(item[1])+ "\n")

with open('words_in_alphabetical_order.txt','w') as f_out:
    for item in sorted_list_alpha[:]:
        f_out.write(item[0]+"--->"+ str(item[1])+ "\n")