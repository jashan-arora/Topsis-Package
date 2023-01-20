# Topsis-Jashan-102003206

## **Project-1 (UCS654)**
_Submitted by: **Jashan Arora**_ 
_Roll no: **102003206**_
_Group: **3COE9**_

<br> 
<b>Topsis-Jashan-102003206 is a Python library for dealing with Multiple Criteria Decision Making(MCDM) problems by using Technique for Order of Preference by Similarity to Ideal Solution(TOPSIS).</b> <br> <br>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Topsis-Jashan-102003206.

```bash
pip install Topsis-Jashan-102003206
```

## Usage

Enter csv filename followed by _.csv_ extentsion, then enter the _weights_ vector with vector values separated by commas, followed by the _impacts_ vector with comma separated signs _(+,-)_, followed by name of output file to be generated
### Syntax

```topsis <input_file> <weights> <impacts> <output_file>```
```bash
topsis input.csv "1,1,1,1" "+,-,+,+" result.csv
```

## Example

#### <b><u>Data.csv</u></b>

A csv file containing input showing data for different mobile handsets having varying features.

| Model | Storage space | Camera | Price | Looks |
| :---: | :-----------: | :----: | :---: | :---: |
|  M1   |      16       |   12   |  250  |   5   |
|  M2   |      16       |   8    |  200  |   3   |
|  M3   |      32       |   16   |  300  |   4   |
|  M4   |      32       |   8    |  275  |   4   |
|  M5   |      16       |   16   |  225  |   2   |

<b>weights vector</b> = [ 0.25 , 0.25 , 0.25 , 0.25 ]

<b>impacts vector </b>= [ + , + , - , + ]

### Input:

```python
topsis Data.csv "0.25,0.25,0.25,0.25" "+,+,-,+" Result.csv
```

### Output:

#### <b><u>Result.csv</u></b>

A csv file containing output showing original data with Topsis Score and Rank columns.

| Model | Storage space | Camera | Price | Looks | Topsis Score | Rank  |
| :---: | :-----------: | :----: | :---: | :---: | :----------: | :---: |
|  M1   |      16       |   12   |  250  |   5   |   0.534277   |   3   |
|  M2   |      16       |   8    |  200  |   3   |   0.308368   |   5   |
|  M3   |      32       |   16   |  300  |   4   |   0.691632   |   1   |
|  M4   |      32       |   8    |  275  |   4   |   0.534737   |   2   |
|  M5   |      16       |   16   |  225  |   2   |   0.401046   |   4   |



## Other notes

* The first column and first row are removed by the library before processing, in attempt to remove indices and headers. So make sure the csv follows the format as shown in sample.csv.
* Make sure the csv does not contain categorical values
* Impacts must be either + or - 
* Weights must be numeric only
* Weights and Impacts must be seperated only by commas (' , ')


## License
[MIT](https://choosealicense.com/licenses/mit/)