# -*- coding:Utf-8 -*-

dir = 'C:/Users/nico/Desktop/Nico/0Python/2017/tp/P5 - Open food fact/'

data = ''
with open(dir+'data.txt', 'r') as f:
    data = f.read()

'''
<tr><td><a href="/categorie/epicerie" class="tag well_known">Epicerie</a></td>
<td style="text-align:right">4379</td><td></td></tr>

Step 1 : split ////" class="tag////
Step 2 : split \\\\/categorie/\\\\
Step 3 : remove element with colon like ////en:Bottled-drinking-water////

'''

data = data.split('" class="tag')[:-1]
data = [x.split('/categorie/')[1] for x in data]
data = [x for x in data if not ':' in x]


with open(dir+'categorie.txt', 'a+') as f:
    f.write('\n'.join(data))








