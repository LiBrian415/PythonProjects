import os 

def main():
    dic = {}
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = 'testfile.txt' 
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as f:
        for line in f:
            words = line.split()
            for word in words:
                if not word[len(word)-1].isalpha():
                    word = word[:len(word)-1]
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] += 1
    for word in dic:
        print(word, dic[word])
        
if __name__ == '__main__':
    main()
