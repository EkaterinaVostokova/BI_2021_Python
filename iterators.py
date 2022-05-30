#!/usr/bin/env python
# coding: utf-8
# 1. Сделайте генератор, который принимает на вход путь к фаста файлу и выдаёт по очереди пары id последовательности (то, что после ">") и последовательности. (5 баллов)
# In[20]:


def read_fasta(path):
    name, seq = None, []
    with open(path) as fp:
        for line in fp:
            line = line.rstrip()
            if line.startswith(">"):
                if name: yield (name, ''.join(seq))
                name, seq = line, []
            else:
                seq.append(line)
        if name: yield (name, ''.join(seq))

reader = read_fasta('sequences.fasta')
print(type(reader))
for name, seq in reader:
    print(name, seq[:50])

2. Напишите класс, производящий чтение последовательностей с небольшими изменениями. (15 баллов)
Класс должен иметь конструктор хотя бы с одним аргументом - путь к фаста файлу
Объект данного класса должен поддерживать итерацию по нему. Не по атрибутам, а именно по самому объекту.
В процессе итерации класс бесконечно перебирает последовательности в файле. Если файл закончился, то итерация продолжается с его начала.
При возвращении каждой очередной последовательности класс немного изменяет её с заданной вероятностью (способ задачи вероятности придумайте сами). Можно менять часть аминокислот, делать делеции, вставки и т.д.. Функционал для изменения последовательностей выделите в отдельный(е) метод(ы).
Наследоваться запрещается

# In[2]:


import random


# In[33]:


class Mutating_Class:
    aminoacids = ('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 
                  'R', 'S', 'T', 'V', 'W', 'Y')
    def __init__(self, path):
        self.path = path
        self.__generator = read_fasta(path)
        self.seq = []
        self.mutation_probability = random.uniform(0, 1)
        
    def __iter__(self):
        return self
    
    def deletion(self, seq):
        if random.random() < self.mutation_probability:
            where_to_delete = random.randrange(len(seq)-5)
            seq = seq[:where_to_delete] + seq[where_to_delete + random.randint(1, 5)]
        return seq
    
    def substitution(self, seq):
        if random.random() < self.mutation_probability:
            where_to_substitute = random.randrange(len(seq))
            seq = seq[:where_to_substitute]+ str(random.choice([self.aminoacids])) + seq[where_to_substitute+1:]
        return seq
    
    def mutation(self, seq):
        mutate = random.choice([self.substitution, self.deletion])
        seq = mutate(seq)
        return seq
    def __next__(self):
        try:
            id_, seq = next(self.__generator)
        except StopIteration:
            self.__generator = read_fasta(self.path)
            id_, seq = next(self.__generator)
        return id_, self.mutation(seq)
        

3. Напишите генератор iter_append(iterable, item), который "добавляет" элемент item в "конец" iterable. (5 доп баллов)
# In[ ]:


def iter_append(iterable, item):
    yield from iterable
    yield item

4. Сделайте функцию, которая "распаковывает" вложенные списки (5 доп баллов)
# In[39]:


def generator(lis):
    for i in lis:
        if isinstance(i, list):
            yield from generator(i)
        else:
            yield i


def nested_list_unpacker(lis):
    out = []
    for j in generator(lis):
        out.append(j)
    return out

