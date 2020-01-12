# Short Term Rental SF Analysis

This is an exploration of how short term rentals impact the SF housing market with a focus on Airbnb due to [data availability](http://insideairbnb.com/). Specifically, this is the code, data, works cited, and notes behind Medium article.

(C) Data Driven Empathy LLC by Sam Pottinger. Released under the MIT license (see LICENSE.md).

<br>

## Article Notes
\* It's not entirely clear why this analysis' results do not agree with [Inside Airbnb's SF page](http://insideairbnb.com/san-francisco/) on percent of hosts with more than one listing. This can be easily reproduced with the source in `check_multi_listings.md` in this repo.

\** 10% of likely "local" hosts have ≥ 3 listings whereas 15% of potential "remote" hosts have ≥ 3 listings.

\*** The actual property type can be tricky to determine without using zoning because the unit may actually a house, for example, but the host has created an "apartment" for guests so puts "apartment" in their listing. The zoning is also helpful to determine the regulations placed on a property.

<br>

## Article Works Cited
1. Barron, Kyle, et al. "Research: When Airbnb Listings in a City Increase, So Do Rent Prices." _Harvard Business Review_, Harvard Business School Publishing, 17 Apr. 2019, [hbr.org/2019/04/research-when-airbnb-listings-in-a-city-increase-so-do-rent-prices](https://hbr.org/2019/04/research-when-airbnb-listings-in-a-city-increase-so-do-rent-prices).
2. "The Office of Short-Term Rentals: City and County of San Francisco." _San Francisco Office of Short-Term Rentals_, City and County of San Francisco, [shorttermrentals.sfgov.org](https://shorttermrentals.sfgov.org/).
3. Said, Carolyn. "Prop. F: S.F. Voters Reject Measure to Restrict Airbnb Rentals." _SFGate_, San Francisco Chronicle, 4 Nov. 2015, [www.sfgate.com/bayarea/article/Prop-F-Measure-to-restrict-Airbnb-rentals-6609176.php](https://www.sfgate.com/bayarea/article/Prop-F-Measure-to-restrict-Airbnb-rentals-6609176.php).
4. LaBarre, Suzanne. "The Bad Design That Created One of America's Worst Housing Crises." _Fast Company_, Fast Company, 28 Sept. 2018, [www.fastcompany.com/90242388/the-bad-design-that-created-one-of-americas-worst-housing-crises](https://www.fastcompany.com/90242388/the-bad-design-that-created-one-of-americas-worst-housing-crises).
5. Andropoulos, Sarah. "Six Disclaimers You May Need to Include on Your Legal Website or Blog." _Legal Marketing and Technology Blog_, Justia, 2 Sept. 2015, [onward.justia.com/2015/09/02/six-disclaimers-you-may-need-to-include-on-your-legal-website-or-blog/](https://onward.justia.com/2015/09/02/six-disclaimers-you-may-need-to-include-on-your-legal-website-or-blog/).
6. Cox, Murray. "Inside Airbnb. Adding Data to the Debate." _Inside Airbnb_, Murray Cox, [insideairbnb.com/index.html](http://insideairbnb.com/index.html).
7. "About Short-Term Rentals." _San Francisco Office of Short-Term Rentals_, City and County of San Francisco, [shorttermrentals.sfgov.org/about](https://shorttermrentals.sfgov.org/about).
8. Martineau, Paris. "How 9 People Built an Illegal $5M Airbnb Empire in New York." _Wired_, Conde Nast, 24 June 2019, www.wired.com/story/how-9-people-built-illegal-5m-airbnb-empire-new-york/.
9. "Zoning Map - Zoning Districts." _DataSF_, City and County of San Francisco, 3 Jan. 2020, [data.sfgov.org/Geographic-Locations-and-Boundaries/Zoning-Map-Zoning-Districts/xvjh-uu28](https://data.sfgov.org/Geographic-Locations-and-Boundaries/Zoning-Map-Zoning-Districts/xvjh-uu28).
10. "Article 2: Use Districts" _San Francisco Planning Code_, American Legal Publishing Corporation, 27 Nov. 2019, [library.amlegal.com/nxt/gateway.dll/California/planning/article2usedistricts?f=templates$fn=document-frameset.htm$q=%5Bfield%20folio-destination-name:%27210.1%27%5D$x=Advanced](http://library.amlegal.com/nxt/gateway.dll/California/planning/article2usedistricts?f=templates$fn=document-frameset.htm$q=%5Bfield%20folio-destination-name:%27210.1%27%5D$x=Advanced).
11. "Article 1: General Zoning Provisions." _San Francisco Planning Code_, American Legal Publishing Corporation, 27 Nov. 2019, [library.amlegal.com/nxt/gateway.dll/California/planning/article1generalzoningprovisions?f=templates&amp;fn=document-frameset.htm&amp;q=&amp;uq=&amp;x=&amp;up=1&amp;force=56&amp;vid=amlegal%3Asanfrancisco_ca_m](http://library.amlegal.com/nxt/gateway.dll/California/planning/article1generalzoningprovisions?f=templates&fn=document-frameset.htm&q=&uq=&x=&up=1&force=56&vid=amlegal:sanfrancisco_ca_m).

<br>

## Local Environment Setup

This project requires a number of open source libraries that can be installed with:

```
$ pip install -r requirements.txt
```

Users will also need [GEOS](https://trac.osgeo.org/geos/) which requires native installation. Note that it is available under conda: `conda install -c anaconda geos`.

Some users may consider use of [virtualenv](https://docs.python-guide.org/dev/virtualenvs/). Furthermore, use of [Jupyter](https://jupyter.org/) is recommended but the `.py` files are exported for convenience of those that do not wish to use Jupyter.

Finally, be sure to unzip the `data_archive.zip` file.

<br>

## Execution

Jupyter is recommended but the `.py` exports are provided. Simply run `$ jupyter notebook` in the directory where the repo was cloned. Some data prep scripts are in `Airbnb Estimate Prep` but the calculations for the article are in `Airbnb Article`.

<br>

## Open Source Libraries

This project leverages a number of open source libraries:

 - [Matplotlib](https://matplotlib.org/) under the [PSF License](https://docs.python.org/3/license.html).
 - [Scipy](https://github.com/scipy/scipy/) under the [BSD License](https://github.com/scipy/scipy/blob/master/LICENSE.txt).
 - [Pandas](https://pandas.pydata.org/) under the [BSD License](https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html#license).
 - [Numpy](https://numpy.org/) under the [BSD License](https://numpy.org/license.html).
 - [Shapely](https://shapely.readthedocs.io/en/stable/manual.html) under the [BSD License]https://github.com/Toblerity/Shapely/blob/master/LICENSE.txt).
 - [GEOS](https://trac.osgeo.org/geos/) under the [LGPL License](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
