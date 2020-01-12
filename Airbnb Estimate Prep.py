#!/usr/bin/env python
# coding: utf-8

# # Notebook to prepare data for analysis

# In[1]:


import json

import matplotlib
import pandas
import shapely.geometry

get_ipython().run_line_magic('matplotlib', 'inline')


# ## Prep materials

# In[2]:


listings_all = pandas.read_csv('listings.csv')


# In[3]:


listings_all['availability_365'].plot.hist(bins=36)


# In[4]:


listings = listings_all #listings_all[listings_all['availability_365'] >= 30].copy()


# In[5]:


with open('zoning.geojson') as f:
    zoning_raw = json.load(f)


# In[55]:


with open('zoning_simplifications.json') as f:
    zoning_simplifications = json.load(f)


# In[7]:


zoning_raw['features'][0]


# In[8]:


zone_geometries = []


# In[9]:


for feature in zoning_raw['features']:
    properties = feature['properties']
    zone_geometries.append({
        'name': properties['districtname'],
        'zoning': properties['zoning'],
        'geometry': shapely.geometry.shape(feature['geometry'])
    })


# ## Join

# In[10]:


len(zone_geometries)


# **Prep Points**

# In[11]:


listings.head(5)


# In[12]:


listings['point'] = listings.apply(lambda x: shapely.geometry.Point(x['longitude'], x['latitude']), axis=1)


# **Prep Lookup**

# In[13]:


def lookup_zone(point):
    results = list(filter(lambda x: x['geometry'].contains(point), zone_geometries))
    if len(results) == 0:
        return [{'name': 'Unknown', 'zoning': 'unknown'}]
    else:
        return results


# **Test Lookup**

# In[14]:


sample = listings.iloc[100]


# In[15]:


lookup_zone(sample['point'])


# **Execute**

# In[16]:


def lookup_zone_str_with_error_handle(point):
    try:
        return lookup_zone(point)
    except:
        return [{'name': 'Error', 'zoning': 'error'}]


# In[17]:


listings['zoningDetailed'] = listings['point'].map(lambda x: lookup_zone_str_with_error_handle(x))


# In[39]:


def serialize_zoning_detailed(original_list):
    new_list = list(map(lambda x: {'name': x['name'], 'zoning': x['zoning']}, original_list))
    return json.dumps(new_list)


# In[40]:


listings['zoning'] = listings['zoningDetailed'].map(lambda x: x[0]['zoning'])
listings['numZones'] = listings['zoningDetailed'].map(lambda x: len(x))
listings['zoningDetailedJson'] = listings['zoningDetailed'].map(serialize_zoning_detailed)


# ## Cleanup

# **Siplify Zones**

# In[56]:


zone_counts = listings.groupby('zoning').count()['id']


# In[57]:


zone_counts.sort_values(ascending=False).head(10)


# In[58]:


listings['zoningSimplified'] = listings['zoning'].map(lambda x: zoning_simplifications.get(x, 'unknown'))


# In[59]:


zone_counts_simplified = listings.groupby('zoningSimplified').count()['id']


# In[60]:


zone_counts_simplified.sort_values(ascending=True).plot.barh()


# In[61]:


zone_counts_simplified.sort_values(ascending=False).to_csv('sorted_counts.csv')


# ## Export

# In[62]:


with open('col_mapping.json') as f:
    col_mapping = json.load(f)


# In[63]:


listings.rename(columns=col_mapping).to_csv('listings_with_zone.csv')


# In[ ]:




