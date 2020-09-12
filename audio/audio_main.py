from scipy.io.wavfile import read
import matplotlib.pyplot as plt

#generate audio files
#koch -f "C:\Python27\air gapped\audio_koch_13000H_Hello.wav" -H 13000 Hello

#Hence DOT ~ 1580 gap
#and DASH ~ 6860 gap

# read audio samples
input_data = read("clue1.wav")
audio = input_data[1]
sr= input_data[0]

#get the positives values in paudio list:
paudio=list()
count_high=0
for i in audio:
    if i>2:
        paudio.append(300)
    if i==2:
        paudio.append(2)
    else:
        paudio.append(0)

flag_300_2 = 0
flag_2_300 = 0
count300=0
c=0
flag_start = 0
x=0
y=0
ans=list()
flag_space=0
x_space=0
flag_letter=0

for i in paudio:    
    if (c%10)==0:        
        if i==300 and flag_start == 0:
            flag_letter = 1
            flag_300_2 = 1
            flag_start = 1
            
        #identify 300->2
        if i==2 and flag_300_2 == 1:
            s = sum(paudio[c:c+100])
            #print s/100
            if 2<=(s/10)<=50:
                #print "i value :",i,"c value :",c
                x=c
                flag_2_300 = 1
                flag_300_2 = 0
                
        #identify 2->300
        if i==300 and flag_2_300 == 1 and flag_start == 1:
            s = sum(paudio[c:c+100])
            if 50<=(s/10):
                y=c
                flag_2_300 = 0
                if 1480<=(y-x)<=1680:
                    print ".",c
                    ans.append(".")
                    x=0
                    y=0
                    flag_start=0
                    flag_letter = 2
                if 6760<=(y-x)<=6960:
                    print "-",c
                    ans.append("-")
                    x=0
                    y=0
                    flag_start=0
                    flag_letter = 2
    c+=1

#print "Y value :",x,"Y value :",y,"distance:",y-x
print str(ans)
plt.plot(paudio)
#print audio
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("Sample Wav")
# display the plot
plt.show()
