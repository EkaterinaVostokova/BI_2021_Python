#!/usr/bin/env python
# coding: utf-8
1. Сделайте небольшой класс, описывающий какую-то сущность на ваш выбор (организм/тип данных/что-то ещё). В классе должен быть конструктор и пара методов
# In[140]:


from Bio.Seq import Seq
import os.path
import Bio
from Bio import SeqIO
from Bio.Seq import Seq
import matplotlib.pyplot as plt
import numpy as np
from Bio.SeqUtils import GC
from matplotlib.pyplot import figure
import threading
from threading import Thread


# In[2]:


# age in months
class Mouse:
    def __init__ (self, color, weight, age):
        self.color = color
        self.weight = weight
        self.age = age
    def grow(self):
        self.weight += 1
    def one_more_month(self):
        self.age += 1
    def reverse_colors(self):
        if self.color == "white":
            self.color = "black"
        elif self.color == "black":
            self.color = "white"

2. Напишите класс, описывающий РНК, у него должны быть:
Конструктор - принимает последовательность РНК и создаёт объект с ней
Метод трансляции - возвращает строку, соответствующую белку из этой РНК по стандартному коду
Метод обратной транскрипции - возвращает строку, соответствующую ДНК из этой РНК
Подумайте, какие атрибуты должны быть заданы для объекта и класса

# In[34]:


string = str(input())
class RNA:
    def __init__(self, input_seq=string):
        self.seq = Seq(input_seq.upper())
        self.length = len(input_seq)
    def translation(self):
        if self.length % 3 == 0:
            return self.seq.translate()
        else:
            return "Partial codon"
    def reverse_transcription(self):        
        return str(self.seq.back_transcribe())

3. Напишите класс, унаследовавшись от сэтов, который будет содержать в себе только положительные числа при создании и не будет добавлять неположительные элементы (подсказка - методы конструктора и add)
# In[23]:


class Sort_positives(set):    
    def __init__(self, element):
        self.positive = {int(i) for i in element if i > 0}
    def add(self, number):
        if number > 0:
            self.positive.add(number)
        else:
            return "Not a positive number"

4. Создайте класс для сбора статистик по фастам.
Входные параметры:
Путь к фаста файлу
Методы:
Подсчёт числа последовательностей в фаста файле
Построение гистограммы длин последовательностей
Подсчёт GC состава
Построение гистограммы частоты 4-меров (по оси x каждый из возможных 4-меров, а по y - их частота)
Переопределение метода для вывода информации при принте (достаточно текста с указанием путя к файлу)
Выполнение всех реализованных методов по подсчёту метрик
Можно придумать дополнительные метрики и реализовать их (по 1 баллу за каждую)

# In[225]:


class Statistics_Fasta:
    def __init__(self, path):
        self.path = path
        with open(self.path):
            self.sequences = list(SeqIO.parse(self.path, "fasta"))
    
    # Подсчёт числа последовательностей в фаста файле
    def sequences_number(self):
        return len(self.sequences)
    
    # Построение гистограммы длин последовательностей
    def sequences_length_distribution(self):
        sequences_lengths = np.array([len(i.seq) for i in self.sequences])
        figure(figsize=(30, 15))
        names, counts = np.unique(sequences_lengths, return_counts=True)
        plt.bar(range(len(names)), counts)
        plt.xticks(range(len(names)), names)
        plt.title("Sequence length distribution")           
        plt.show()
    
    # Подсчёт GC состава
    def count_GC(self):
        gcs = np.array([GC(j.seq) for j in self.sequences])
        return gcs.mean()
    
    # Построение гистограммы GC состава
    def sequences_GC_distribution(self):
        gcs = np.array([GC(j.seq) for j in self.sequences])
        figure(figsize=(30, 15))
        names, counts = np.unique(gcs, return_counts=True)
        plt.bar(range(len(names)), counts)
        plt.xticks(range(len(names)), names)
        plt.title("GC content distribution")
        plt.show()
    
    # Построение гистограммы частоты 4-меров (по оси x каждый из возможных 4-меров, а по y - их частота)
    def counts_4_mers(self):
        possible_4_mers = dict()
        k = 4
        sequences = [s.seq for s in self.sequences]
        for seq in sequences:
            for i in range(len(seq) - k + 1):
                kmr = seq[i:i + k]
                if kmr in possible_4_mers:
                    possible_4_mers[kmr] += 1
                else:
                    possible_4_mers[kmr] = 1
        new = {k: v for k, v in sorted(possible_4_mers.items(), key=lambda x: x[1], reverse=True)}
        y = list(new.values())
        names = list(new.keys())
        figure(figsize=(40, 10))
        plt.bar(range(len(y)), y)
        plt.xticks(range(len(names)), names, rotation='vertical')
        plt.title("Distribution of 4-mers counts")
        plt.show()
        
    # Переопределение метода для вывода информации при принте (достаточно текста с указанием путя к файлу)
    def __repr__(self):
        return self.path
        
    # Выполнение всех реализованных методов по подсчёту метрик
    def runall(self):
        if __name__ == '__main__':
            Thread(target = self.sequences_number).start()
            Thread(target = self.sequences_length_distribution).start()
            Thread(target = self.count_GC).start()
            Thread(target = self.counts_4_mers).start()
            Thread(target = self.sequences_GC_distribution).start()

