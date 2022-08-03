# Template-Data
A collection of template data sources. The code covers importing and/or loading data, with options for default cleansing functions.

Clone repo code:
`git clone https://github.com/JHuardC/Template-Data.git`

Scripts can be ran in command line or imported. 

A data folder is provided to store data locally if prefered. **Note:** To reload a dataset locally from the './data/' folder, the dataset must be saved as a csv (.csv) with the same file name as the corresponding python (.py) script.

A meta.py file is included too, this file allows new data sources to easily be added to the repo and to local clones, following the same script structure as current data sets.

## Available data sets
The following is a table scripts, with a brief description of the data included, what the target variable is and links to the data sources.

| Script  | Description | Recommended Target Variable | Link  |
| ------- | ------- | ------- | ------- |
| abalone.py  | Dataset recording measurements of Abalone shells. | rings (int) | [Available at UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/abalone) |

## References
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Available at: [http://archive.ics.uci.edu/ml](http://archive.ics.uci.edu/ml)

Warwick J Nash, Tracy L Sellers, Simon R Talbot, Andrew J Cawthorn and Wes B Ford (1994). "The Population Biology of Abalone (_Haliotis_ species) in Tasmania. I. Blacklip Abalone (_H. rubra_) from the North Coast and Islands of Bass Strait", Sea Fisheries Division, Technical Report No. 48 (ISSN 1034-3288)
