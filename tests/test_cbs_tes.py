from cbs import cbs
import pandas as pd
import pytest

#Get the CBS TE dataframe
@pytest.fixture(scope="module")
def TE():
    return cbs.Cbs().parser('TE')

def test_cbs_te_columns(TE):
    assert TE.columns.tolist() == ['Name', 'pass_att', 'pass_cmp', 'pass_yds', 'pass_td', 'intercept', 'rate', 'rush_att',
                      'rush_yds', 'rush_avg', 'rush_td', 'rec_tgt', 'recept', 'rec_yds', 'rec_avg', 'rec_td', '2pt',
                      'fum_lost']

#Test top and bottom names
def test_cbs_te_projection1(TE):
    assert type(TE.iloc[0].Name) == str

def test_cbs_te_projection2(TE):
    assert type(TE.iloc[1].Name) == str

def test_cbs_te_projection3(TE):
    assert type(TE.iloc[20].Name) == str

def test_cbs_te_projection4(TE):
    assert type(TE.iloc[30].Name) == str

#Test top and bottom Stats
def test_cbs_te_projection5(TE):
    assert pd.to_numeric(TE.iloc[0].rec_tgt, errors='ignore') > 0

def test_cbs_te_projection6(TE):
    assert pd.to_numeric(TE.iloc[1].rec_yds, errors='ignore') > 0

def test_cbs_te_projection7(TE):
    assert pd.to_numeric(TE.iloc[20].rec_avg, errors='ignore') > 0

def test_cbs_te_projection8(TE):
    assert pd.to_numeric(TE.iloc[30].rec_tgt, errors='ignore') > 0