from collections import Counter
import re

with open(r'Oliver Twist(雾都孤儿(孤星血泪)).txt', 'r') as f:
    all_words = f.read().lower()
    
rule = re.compile(r'\w+')  #这是从别的语言带来的陋习，可以直接如下行所示使用正则表达式
words = re.findall(r'\w+', all_words)

counter_words = Counter(words)
common_words = counter_words.most_common(20)
print(common_words)

