

# SharK Attack Dataset

The dataset includes information on shark attack occurrences around the world. Data related to the location, fatality and activities practiced during the incidents were also addressed in the analysis.

![60375-bruce-shark-marlin-png-image-high-quality](https://user-images.githubusercontent.com/101371267/162100662-56a80cdc-3bcf-40bf-a3ab-1d760838c2f7.png)

## References

 
 - [Pandas Documentation](https://pandas.pydata.org/docs/index.html)
 - [Ocean Current Map](https://upload.wikimedia.org/wikipedia/commons/9/9b/Corrientes-oceanicas.png)
 - [re — Regular expression operations](https://docs.python.org/3/library/re.html)

## Analysis approach

The initial size of the dataset was (25723, 24). The first step was to clean the data, removing duplicate values. then the columns that would answer the proposed questions were extracted (["Country", "Fatal (Y/N)", "Activity", "Area"]].
A mask was applied to filter only countries with more than 100 occurrences.
Regex was used to strip special characters and do other string cleanups in the dataframe.
The following insights were taken from the analyses, using "groupby", "loc.", "value_counts" techniques.

## Question 1: Which hemisphere has more ocurrences?

Despite little difference the northern hemisphere has more occurrences (N-2338 / S-2163), but more fatal incidents occurred in the southern hemisphere, about 68% of the total.

## Question 2: Which activity has more fatalities?

The most recorded activity during the occurrences was surfing, however, without any fatality, on the other hand the most fatal was swimming with 24% of the cases.

## Question 3: How Many ocurrences happens in Western Boundary Current areas?

Western boundary currents are hot, deep, narrow, fast-flowing currents that form on the west side of ocean basins due to western intensification. They carry warm water from the tropics towards the poles.

One of the analysis approaches was to relate the shark attack occurrences with the location of these currents and according to the data, 62% of the total occurrences are in places under the influence of the dynamics of these hot currents.


Western boundary currents map
![Corrientes-oceanicas](https://user-images.githubusercontent.com/101371267/161887110-ba5b618b-c2fa-424a-9f29-32187dfd3312.png)

