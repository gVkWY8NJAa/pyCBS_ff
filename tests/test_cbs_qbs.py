from cbs import cbs
import pandas as pd
import pytest

#Get the CBS QB dataframe
@pytest.fixture(scope="module")
def QB():
    return cbs.Cbs().parser('QB')

def test_cbs_qb_columns(QB):
    assert QB.columns.tolist() == ['Name','pass_att', 'pass_cmp', 'pass_yds', 'pass_td', 'intercept', 'rate',
                                   'rush_att', 'rush_yds', 'rush_avg', 'rush_td', 'rec_tgt', 'recept', 'rec_yds',
                                   'rec_avg', 'rec_td', '2pt','fum_lost']

#Test top and bottom names
def test_cbs_qb_projection1(QB):
    assert type(QB.iloc[0].Name) == str

def test_cbs_qb_projection2(QB):
    assert type(QB.iloc[1].Name) == str

def test_cbs_qb_projection3(QB):
    assert type(QB.iloc[20].Name) == str

def test_cbs_qb_projection4(QB):
    assert type(QB.iloc[30].Name) == str

#Test top and bottom stats
def test_cbs_qb_projection5(QB):
    assert pd.to_numeric(QB.iloc[0].pass_yds, errors='ignore') > 1000

def test_cbs_qb_projection6(QB):
    assert pd.to_numeric(QB.iloc[1].rush_yds, errors='ignore') > 0

def test_cbs_qb_projection7(QB):
    assert pd.to_numeric(QB.iloc[20].pass_yds, errors='ignore') > 1000

def test_cbs_qb_projection8(QB):
    assert pd.to_numeric(QB.iloc[30].rate, errors='ignore') > 0
