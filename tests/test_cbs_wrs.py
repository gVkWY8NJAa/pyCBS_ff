from cbs import cbs
import pandas as pd
import pytest

#Get the CBS WR dataframe
@pytest.fixture(scope="module")
def WR():
    return cbs.Cbs().parser('WR')

def test_cbs_wr_columns(WR):
    assert WR.columns.tolist() == ['Name', 'pass_att', 'pass_cmp', 'pass_yds', 'pass_td', 'intercept', 'rate', 'rush_att',
                      'rush_yds', 'rush_avg', 'rush_td', 'rec_tgt', 'recept', 'rec_yds', 'rec_avg', 'rec_td', '2pt',
                      'fum_lost']

#Test top and bottom names
def test_cbs_wr_projection1(WR):
    assert type(WR.iloc[0].Name) == str

def test_cbs_wr_projection2(WR):
    assert type(WR.iloc[1].Name) == str

def test_cbs_wr_projection3(WR):
    assert type(WR.iloc[20].Name) == str

def test_cbs_wr_projection4(WR):
    assert type(WR.iloc[160].Name) == str

#Test top and bottom Stats
def test_cbs_wr_projection5(WR):
    assert pd.to_numeric(WR.iloc[0].rec_yds, errors='ignore') > 1000

def test_cbs_wr_projection6(WR):
    assert pd.to_numeric(WR.iloc[1].recept, errors='ignore') > 0

def test_cbs_wr_projection7(WR):
    assert pd.to_numeric(WR.iloc[20].rec_tgt, errors='ignore') > 0

def test_cbs_wr_projection8(WR):
    assert pd.to_numeric(WR.iloc[30].fum_lost, errors='ignore') > 0