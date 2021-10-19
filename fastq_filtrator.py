#!/usr/bin/env python
# coding: utf-8

# In[78]:


# Defining the functions
# 1. main function (just combines all the rest). works through iterating over lists
def main(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold, save_filtered):
    # opens
    open_file(input_fastq, full_length_file)
    # now we have open the file and created a "full length file" list
    for read in full_length_file:
        gc_bounds_function(read, gc_bounds, reads_passed_GC, reads_not_passed_GC)
    for read in reads_passed_GC:
        length_bounds_function(read, length_bounds, reads_passed_GC_length, reads_not_passed_GC_length)
    for read in reads_passed_GC_length:
        threshold_quality_function(read, reads_passed_GC_length_quality)
    filename_passed = str(output_file_prefix) + "_passed.fastq"
    filename_failed = str(output_file_prefix) + "_failed.fastq"
    writing_results(filename_passed, filename_failed)


# In[79]:


# OPENING THE FILE
def divide_into_read_parts(lines=None):
    name_parts = ['name', 'sequence', 'optional', 'quality']
    return {k: v for k, v in zip(name_parts, lines)}
    # maybe it will be better not to create it later so it does not take space
    # the idea was found at https://www.biostars.org/p/317524/


def open_file(input_fastq, full_length_file):
    with open(input_fastq, 'r') as f:
        lines = []
        for line in f:
            lines.append(line.rstrip())
            if len(lines) == 4:
                record = divide_into_read_parts(lines)
                full_length_file.append(record)
                lines = []


# In[80]:


# GC COUNT RELATED FUNCTIONS
def GC_count(read):
    # sub-function 1 for gc bounds one
    # just the sum of C and G occurrences over the length of this read
    return 100*(read['sequence'].count("C")+read['sequence'].count("G"))/len(read['sequence'])


# In[81]:


# gc bounds itself. if it will be the first function, it would take the initial list and after it
# the reads that pass further are saved in reads_passed_GC
def gc_bounds_function(read, gc_bounds, reads_passed_GC, reads_not_passed_GC):
    gc_bounds_number = list()
    gc_bounds = gc_bounds.split()
    if len(gc_bounds) == 1:
        if gc_bounds[0] == "default":
            gc_bounds_number = (0, 100)
        elif gc_bounds[0].isdigit():
            gc_bounds_number = (0, int(gc_bounds[0]))
    elif len(gc_bounds) == 2 and gc_bounds[0].isdigit() and gc_bounds[1].isdigit():
        if int(gc_bounds[0]) <= int(gc_bounds[1]):
            gc_bounds_number = (int(gc_bounds[0]), int(gc_bounds[1]))
    if GC_count(read) >= gc_bounds_number[0] and GC_count(read) <= gc_bounds_number[1]:
        reads_passed_GC.append(read)
    else:
        if save_filtered.lower() == "true":
            reads_not_passed_GC.append(read)


# In[82]:


def length_bounds_function(read, length_bounds, reads_passed_GC_length, reads_not_passed_GC_length):
    # NOW LENGTH BOUNDS
    # here no subfunction like the one counting GC content first is needed
    # here you can only enter number as it is, without **
    length_bounds_number = list()
    length_bounds = length_bounds.split()
    if len(length_bounds) == 1:
        if length_bounds[0] == "default":
            length_bounds_number = (0, 2**32)
        elif length_bounds[0].isdigit():
            length_bounds_number = (0, int(length_bounds[0]))
    elif len(length_bounds) == 2 and length_bounds[0].isdigit() and length_bounds[1].isdigit():
        if int(length_bounds[0]) <= int(length_bounds[1]):
            length_bounds_number = (int(length_bounds[0]), int(length_bounds[1]))
    if len(read['sequence']) >= length_bounds_number[0] and len(read['sequence']) <= length_bounds_number[1]:
        reads_passed_GC_length.append(read)
    else:
        if save_filtered.lower() == "true":
            reads_not_passed_GC_length.append(read)


# In[83]:


def average_quality(read):
    # пороговое значение среднего качества рида для фильтрации, по-умолчанию равно 0 (шкала phred33)
    # Риды со средним качеством по всем нуклеотидам ниже порогового отбрасываются
    # it converts to ASCII score
    sum_of_reads = 0
    for i in read["quality"]:
        sum_of_reads += ord(i)-33
    return sum_of_reads/len(read["quality"])


# In[84]:


def threshold_quality_function(read, reads_passed_GC_length_quality):
    quality_threshold_number = 0
    if quality_threshold.isdigit():
        quality_threshold_number = int(quality_threshold)
    if average_quality(read) >= quality_threshold_number:
        reads_passed_GC_length_quality.append(read)
    else:
        if save_filtered.lower() == "true":
            reads_not_passed_GC_length_quality.append(read)


# In[85]:


def writing_results(filename_passed, filename_failed):
    with open(filename_passed, "w") as file1:
        # Writing data to a file
        for item in reads_passed_GC_length_quality:
            for el in item:
                file1.write("%s\n" % item[el])
    if save_filtered.lower() == "true":
        with open(filename_failed, "a") as file2:
            for item1 in reads_not_passed_GC_length_quality:
                for element in item1:
                    file2.write("%s\n" % item1[element])
            for item2 in reads_not_passed_GC_length:
                for element1 in item2:
                    file2.write("%s\n" % item2[element1])
            for item3 in reads_not_passed_GC:
                for element2 in item3:
                    file2.write("%s\n" % item3[element2])


# In[101]:


# input of all files
input_fastq = input("Enter path to the file")
output_file_prefix = input("Write any prefix name")
# gc_bounds =
gc_bounds = input("Define GC bounds - from/to, to, default")
# length_bounds =
length_bounds = input("Define length bounds - from/to (2 numbers, to (1 number), default (write 'default')")
# quality_threshold
quality_threshold = input("Enter quality threshold (one number) or choose 'default'")
# save_filtered
save_filtered = input("Do you need to save reads which did not pass filter? Type 'True' or 'False'")
full_length_file = []
reads_passed_GC = []
reads_not_passed_GC = []
reads_passed_GC_length = []
reads_not_passed_GC_length = []
reads_passed_GC_length_quality = []
reads_not_passed_GC_length_quality = []


# In[103]:


main(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold, save_filtered)
