
# pyCBS_ff
</hr>

pyCBS_ff is a python module to help you scrape fantasy football projections from cbssports.com

## Installation
```
git clone git@github.com:gVkWY8NJAa/pyCBS_ff.git
cd pyCBS_ff
pip install -r requirements.txt
```

## Usage

import module


```python
from cbs import Cbs
```

Choose from any of the 'QB', 'WR', 'RB', 'TE', 'K', 'DEF'


```python
df = Cbs().parser('QB')
```


```python
df.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>pass_att</th>
      <th>pass_cmp</th>
      <th>pass_yds</th>
      <th>pass_td</th>
      <th>intercept</th>
      <th>rate</th>
      <th>rush_att</th>
      <th>rush_yds</th>
      <th>rush_avg</th>
      <th>rush_td</th>
      <th>rec_tgt</th>
      <th>recept</th>
      <th>rec_yds</th>
      <th>rec_avg</th>
      <th>rec_td</th>
      <th>2pt</th>
      <th>fum_lost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Deshaun Watson (HOU)</td>
      <td>561</td>
      <td>335</td>
      <td>3992</td>
      <td>27</td>
      <td>20</td>
      <td>82.7</td>
      <td>76</td>
      <td>526</td>
      <td>6.92</td>
      <td>5.3</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0</td>
      <td>0</td>
      <td>3.9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aaron Rodgers (GB)</td>
      <td>600</td>
      <td>391</td>
      <td>3858</td>
      <td>32</td>
      <td>10</td>
      <td>94.0</td>
      <td>56</td>
      <td>324</td>
      <td>5.79</td>
      <td>1.7</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0</td>
      <td>0</td>
      <td>3.1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tom Brady (NE)</td>
      <td>617</td>
      <td>396</td>
      <td>4651</td>
      <td>31</td>
      <td>10</td>
      <td>97.0</td>
      <td>30</td>
      <td>41</td>
      <td>1.37</td>
      <td>0.3</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0</td>
      <td>0</td>
      <td>3.1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Russell Wilson (SEA)</td>
      <td>560</td>
      <td>340</td>
      <td>3790</td>
      <td>25</td>
      <td>18</td>
      <td>82.4</td>
      <td>91</td>
      <td>532</td>
      <td>5.85</td>
      <td>3.7</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0</td>
      <td>0</td>
      <td>3.3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Andrew Luck (IND)</td>
      <td>584</td>
      <td>367</td>
      <td>4189</td>
      <td>26</td>
      <td>16</td>
      <td>87.8</td>
      <td>66</td>
      <td>342</td>
      <td>5.18</td>
      <td>1.9</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0</td>
      <td>0</td>
      <td>3.3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = Cbs().parser('WR')
```


```python
df.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>pass_att</th>
      <th>pass_cmp</th>
      <th>pass_yds</th>
      <th>pass_td</th>
      <th>intercept</th>
      <th>rate</th>
      <th>rush_att</th>
      <th>rush_yds</th>
      <th>rush_avg</th>
      <th>rush_td</th>
      <th>rec_tgt</th>
      <th>recept</th>
      <th>rec_yds</th>
      <th>rec_avg</th>
      <th>rec_td</th>
      <th>2pt</th>
      <th>fum_lost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Antonio Brown (PIT)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>1</td>
      <td>2</td>
      <td>2.00</td>
      <td>0</td>
      <td>176.0</td>
      <td>111</td>
      <td>1582</td>
      <td>14.25</td>
      <td>10.1</td>
      <td>0</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DeAndre Hopkins (HOU)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0</td>
      <td>165.0</td>
      <td>94</td>
      <td>1325</td>
      <td>14.10</td>
      <td>9.4</td>
      <td>0</td>
      <td>1.1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Julio Jones (ATL)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>1</td>
      <td>19</td>
      <td>19.00</td>
      <td>0</td>
      <td>159.0</td>
      <td>97</td>
      <td>1390</td>
      <td>14.33</td>
      <td>5.5</td>
      <td>0</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Davante Adams (GB)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0</td>
      <td>141.0</td>
      <td>90</td>
      <td>1043</td>
      <td>11.59</td>
      <td>10</td>
      <td>0</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Odell Beckham (NYG)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>2</td>
      <td>19</td>
      <td>9.50</td>
      <td>0</td>
      <td>184.0</td>
      <td>109</td>
      <td>1229</td>
      <td>11.28</td>
      <td>7.1</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = Cbs().parser('RB')
```


```python
df.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>pass_att</th>
      <th>pass_cmp</th>
      <th>pass_yds</th>
      <th>pass_td</th>
      <th>intercept</th>
      <th>rate</th>
      <th>rush_att</th>
      <th>rush_yds</th>
      <th>rush_avg</th>
      <th>rush_td</th>
      <th>rec_tgt</th>
      <th>recept</th>
      <th>rec_yds</th>
      <th>rec_avg</th>
      <th>rec_td</th>
      <th>2pt</th>
      <th>fum_lost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Todd Gurley (LAR)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>318</td>
      <td>1391</td>
      <td>4.37</td>
      <td>12.2</td>
      <td>88.0</td>
      <td>62</td>
      <td>691</td>
      <td>11.15</td>
      <td>4.8</td>
      <td>0</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>LeVeon Bell (PIT)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>324</td>
      <td>1319</td>
      <td>4.07</td>
      <td>10.5</td>
      <td>117.0</td>
      <td>90</td>
      <td>714</td>
      <td>7.93</td>
      <td>2.4</td>
      <td>0</td>
      <td>3.8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ezekiel Elliott (DAL)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>340</td>
      <td>1480</td>
      <td>4.35</td>
      <td>8</td>
      <td>53.0</td>
      <td>37</td>
      <td>388</td>
      <td>10.49</td>
      <td>2.1</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David Johnson (ARI)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>275</td>
      <td>934</td>
      <td>3.40</td>
      <td>6.6</td>
      <td>117.0</td>
      <td>82</td>
      <td>922</td>
      <td>11.24</td>
      <td>2.8</td>
      <td>0</td>
      <td>5.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Saquon Barkley (NYG)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>285</td>
      <td>1173</td>
      <td>4.12</td>
      <td>8.2</td>
      <td>94.0</td>
      <td>60</td>
      <td>415</td>
      <td>6.92</td>
      <td>1.6</td>
      <td>0</td>
      <td>1.8</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = Cbs().parser('TE')
```


```python
df.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>pass_att</th>
      <th>pass_cmp</th>
      <th>pass_yds</th>
      <th>pass_td</th>
      <th>intercept</th>
      <th>rate</th>
      <th>rush_att</th>
      <th>rush_yds</th>
      <th>rush_avg</th>
      <th>rush_td</th>
      <th>rec_tgt</th>
      <th>recept</th>
      <th>rec_yds</th>
      <th>rec_avg</th>
      <th>rec_td</th>
      <th>2pt</th>
      <th>fum_lost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rob Gronkowski (NE)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0</td>
      <td>116.0</td>
      <td>73</td>
      <td>1071</td>
      <td>14.67</td>
      <td>7.3</td>
      <td>0</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Travis Kelce (KC)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>2</td>
      <td>4</td>
      <td>2.00</td>
      <td>0</td>
      <td>134.0</td>
      <td>90</td>
      <td>1043</td>
      <td>11.59</td>
      <td>7.2</td>
      <td>0</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Zach Ertz (PHI)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0</td>
      <td>112.0</td>
      <td>76</td>
      <td>826</td>
      <td>10.87</td>
      <td>6.4</td>
      <td>0</td>
      <td>1.1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Trey Burton (CHI)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0</td>
      <td>99.0</td>
      <td>67</td>
      <td>728</td>
      <td>10.87</td>
      <td>5.4</td>
      <td>0</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Evan Engram (NYG)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>1</td>
      <td>18</td>
      <td>18.00</td>
      <td>0</td>
      <td>116.0</td>
      <td>67</td>
      <td>732</td>
      <td>10.93</td>
      <td>5.1</td>
      <td>0</td>
      <td>0.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = Cbs().parser('K')
```


```python
df.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>fg</th>
      <th>fg_att</th>
      <th>fg_lng</th>
      <th>PAT_made</th>
      <th>PAT_att</th>
      <th>PAT_blckd</th>
      <th>1-19</th>
      <th>20-29</th>
      <th>30-39</th>
      <th>40-49</th>
      <th>1-49</th>
      <th>50+</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Stephen Gostkowski (NE)</td>
      <td>35.6</td>
      <td>40.2</td>
      <td>0</td>
      <td>46</td>
      <td>46</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Greg Zuerlein (LAR)</td>
      <td>34.7</td>
      <td>37.1</td>
      <td>0</td>
      <td>43.1</td>
      <td>43.1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Harrison Butker (KC)</td>
      <td>34.8</td>
      <td>39.4</td>
      <td>0</td>
      <td>42.4</td>
      <td>42.4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Robbie Gould (SF)</td>
      <td>35.6</td>
      <td>37.3</td>
      <td>0</td>
      <td>38.2</td>
      <td>38.2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Jake Elliott (PHI)</td>
      <td>31.4</td>
      <td>36.1</td>
      <td>0</td>
      <td>42.4</td>
      <td>42.4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = Cbs().parser('DEF')
```


```python
df.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>def_int</th>
      <th>def_saftey</th>
      <th>def_sk</th>
      <th>tackles</th>
      <th>fum_rec</th>
      <th>forced_fumbles</th>
      <th>def_td</th>
      <th>itd</th>
      <th>ftd</th>
      <th>pts_allowd</th>
      <th>pass_yds_allowed</th>
      <th>rush_yds_allowed</th>
      <th>yds_allowed</th>
      <th>kick_rt_td</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>JAX</td>
      <td>18</td>
      <td>1</td>
      <td>52</td>
      <td>647</td>
      <td>15</td>
      <td>21</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>281</td>
      <td>2891</td>
      <td>1784</td>
      <td>4675</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TEN</td>
      <td>16</td>
      <td>0</td>
      <td>40</td>
      <td>670</td>
      <td>13</td>
      <td>17</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>332</td>
      <td>3193</td>
      <td>1595</td>
      <td>4788</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MIN</td>
      <td>15</td>
      <td>0</td>
      <td>40</td>
      <td>657</td>
      <td>11</td>
      <td>15</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>293</td>
      <td>3210</td>
      <td>1496</td>
      <td>4706</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>LAR</td>
      <td>15</td>
      <td>1</td>
      <td>53</td>
      <td>666</td>
      <td>14</td>
      <td>19</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>325</td>
      <td>3390</td>
      <td>1830</td>
      <td>5220</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BAL</td>
      <td>19</td>
      <td>0</td>
      <td>39</td>
      <td>649</td>
      <td>15</td>
      <td>21</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>295</td>
      <td>3253</td>
      <td>1654</td>
      <td>4907</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
