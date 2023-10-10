#!/usr/bin/env python
# coding: utf-8

# ## Параллельная обработка изображений в многозадачной среде

# In[13]:


import os
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageEnhance, ImageOps


# ### Фильтры

# 1. Фильтр сепии

# In[14]:


def sepia(inp, out_path):
    try:
        image = Image.open(inp)
        sepia_image = ImageOps.colorize(image.convert('L'), '#704214', '#C0C080')
        sepia_image.save(out_path)
    except Exception as e:
        print(f'К файлу {inp} невозможно применить фильтр в виду ошибки: {str(e)}')


# 2. Фильтр резкости

# In[15]:


def sharpen(inp, out_path):
    try:
        image = Image.open(inp)
        sharpened_image = ImageEnhance.Sharpness(image).enhance(2.0)
        sharpened_image.save(out_path)
    except Exception as e:
        print(f'К файлу {inp} невозможно применить фильтр в виду ошибки: {str(e)}')


# 3. Фильтр уменьшения размера

# In[16]:


def resize(inp, out_path):
    try:
        image = Image.open(inp)
        resized_image = image.resize((300, 300))
        resized_image.save(out_path)
    except Exception as e:
        print(f'К файлу {inp} невозможно применить фильтр в виду ошибки: {str(e)}')


# ### Обработка изображений

# In[18]:


def process(inp, out_folder):
    image_name = os.path.basename(inp)
    filename, _ = os.path.splitext(image_name)

    sharpen(inp, os.path.join(out_folder, f'{filename}_f1.jpg'))
    sepia(inp, os.path.join(out_folder, f'{filename}_f2.jpg'))
    resize(inp, os.path.join(out_folder, f'{filename}_f3.jpg'))

def parallel_images(image_folder, out_folder):
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    tasks = []
    for image_name in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_name)
        if os.path.isfile(image_path) and image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            tasks.append((image_path, out_folder))

    with ThreadPoolExecutor() as executor:
        executor.map(lambda args: process(*args), tasks)
        
image_folder = r'C:\Users\sibfl\OneDrive\photo'
out_folder = r'C:\Users\sibfl\OneDrive\photo\new'

parallel_images(image_folder, out_folder)

