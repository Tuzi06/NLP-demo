Main idea: take a audio file that has multiple people taking (can have a loud background noise), output the script or subtitle for each person

Workflow:
    1. input wav file
    2. convert to signal 
    3. filter 
    4. nlp
    5.output to txt file




each person should have different frequency range
-> differentiate people by fft sound signal and filter frequency [ don't know if this will work :( ] 
    => will use some kind of machine learning algo to do the seperation
    -> maybe too much overlap and cannot seperate signal if multiple person speak at same time
    -> also need filter out noise 
-> use nlp algo to transfer each person's sound to txt file





Source paper:
Supervised Speech Separation Based on Deep Learning: An Overview
    https://arxiv.org/ftp/arxiv/papers/1708/1708.07524.pdf