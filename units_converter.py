#!/usr/bin/env python
# coding: utf-8

# In[9]:


# goal: find out most used American values and convert them into European ones
# data used: Температура по Цельсия = (Температура по Фаренгейту - 32) * 5 / 9
# 1 Лига [lea] = 3 милям = 24 фурлонгам = 4828.032 м
# 1 Миля [mi] = 8 фурлонгов = 1760 ярдов = 5280 футов = 1609.344 м
# 1 Фут [ft] = 12 дюймов = 0.3048 м
# 1 Дюйм [in] = 0.0254 м
# Миля в секунду [mps] = 1609.34401 м/с.

data = input("What to convert? American -> European. Possible: temperature, distance, velocity")
if data == "temperature":
    temperature = (float(input("What is the temperature in Fahrenheit? ")) - 32) * (5/9)
    print(temperature, "celsius")
elif data == "distance":
    distance_type = input("League, Yard, Mile, Foot or Inch? ")
    distance = float(input("How many?"))
    if distance_type == "League":
        distance = distance * 4828.032
        print(distance, "meters")
    elif distance_type == "Yard":
        distance = distance * 0.9144
        print(distance, "meters")
    elif distance_type == "Mile":
        distance = distance * 1609.344
        print(distance, "meters")
    elif distance_type == "Foot":
        distance = distance * 0.3048
        print(distance, "meters")
    elif distance_type == "Inch":
        distance = distance * 0.0254
        print(distance, "meters")
    else:
        print("Unknown distance")
elif data == "velocity":
    velocity = float(input("What is the velocity in miles per second? ")) * 1609.34401
    print(velocity, "meters per second")
