Check Multi-Listings Calculation
=================================

t's not entirely clear why this analysis' results do not agree with [Inside Airbnb's SF page](http://insideairbnb.com/san-francisco/) on percent of hosts with more than one listing. This can be easily reproduced with the source below.

<br>

Get the data
---------------------------------
Using the command line, run the following:

```
$ wget http://data.insideairbnb.com/united-states/ca/san-francisco/2019-12-04/data/listings.csv.gz
$ gunzip listings.csv.gz
```

<br>

Run calculation
---------------------------------
Get the number of hosts per listing within a Python script:

```
import pandas

source_data = pandas.read_csv('./listings.csv')

counts = source_data.groupby('host_id').count()['id'].reset_index().rename(
  columns={
    'host_id': 'count',
    'id': 'numListings'
  }
).groupby('numListings').count()

counts['percent'] = counts['count'] / counts['count'].sum()

print(counts)
```
