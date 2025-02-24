#  Project discontinued

# Corona Atlas <img src="assets/img/corona-atlas-icon.png" align="right" width="120"/>

_Visit
[our website](https://dieghernan.github.io/corona-atlas.de/)
or contact us directly
[via mail](mailto:info@corona-atlas.de)._
</br></br></br>


Interactive map of the international COVID-19 risk areas as designated by the German authorities.

The data is updated periodically from the website of the [Robert Koch Institute][rki].

Data scraping is performed on **Python** with
[**scrapy**](https://scrapy.org/).
The scraper also uses
[**pandas**](https://pandas.pydata.org/) and
[**pycountry**](https://pypi.org/project/pycountry/).

Map visualization is created with **R** and generates a map via [{rmarkdown}](https://rmarkdown.rstudio.com/). The map is created using [{leaflet}](http://rstudio.github.io/leaflet/), [{giscoR}](https://dieghernan.github.io/giscoR/) and some packages included on the [tidyverse](https://www.tidyverse.org/).
 
The website uses [**Chulapa**](https://dieghernan.github.io/chulapa/)
as its Jekyll theme.

## Additional resources

-   [RKI website][rki]: Data source.


[rki]: https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Risikogebiete_neu.html

## Current status

[![Corona Atlas](/assets/img/og_corona_atlas.png)][corona-atlas]

## Time-lapse

![Time-lapse](/assets/img/corona_atlas_timelapse.gif)

[corona-atlas]: https://dieghernan.github.io/corona-atlas.de/
