import sys
input = sys.stdin.readline


word = input().strip()

word_cnt = len(word)

word_m = "z" * word_cnt  # 'z'로 구성된 단어 수만큼의 단어.

for i in range(1, word_cnt - 1):
    for j in range(i + 1, word_cnt):
        # 단어 3개 뒤집기
        new_word = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
        
        if new_word < word_m: 
            word_m = new_word

print(word_m)