from cbs import cbs
import pandas as pd
import pytest

#Get the CBS RB dataframe
@pytest.fixture(scope="module")
def RB():
    return cbs.Cbs().parser('RB')

def test_cbs_rb_columns(RB):
    assert RB.columns.tolist() == ['Name', 'pass_att', 'pass_cmp', 'pass_yds', 'pass_td', 'intercept', 'rate', 'rush_att',
                      'rush_yds', 'rush_avg', 'rush_td', 'rec_tgt', 'recept', 'rec_yds', 'rec_avg', 'rec_td', '2pt',
                      'fum_lost']

#Test top and bottom names
def test_cbs_rb_projection1(RB):
    assert type(RB.iloc[0].Name) == str

def test_cbs_rb_projection2(RB):
    assert type(RB.iloc[1].Name) == str

def test_cbs_rb_projection3(RB):
    assert type(RB.iloc[120].Name) == str

def test_cbs_rb_projection4(RB):
    assert type(RB.iloc[121].Name) == str

#Test top and bottom Stats

def test_cbs_rb_projection5(RB):
    assert pd.to_numeric(RB.iloc[0].rush_td, errors='ignore') >= 0

def test_cbs_rb_projection6(RB):
    assert pd.to_numeric(RB.iloc[1].rush_att, errors='ignore') >= 0

def test_cbs_rb_projection7(RB):
    assert pd.to_numeric(RB.iloc[120].rush_avg, errors='ignore') >= 0

def test_cbs_rb_projection8(RB):
    assert pd.to_numeric(RB.iloc[121].rec_avg, errors='ignore') >= 0
