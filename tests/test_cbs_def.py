from cbs import cbs
import pandas as pd
import pytest

#Get the CBS K dataframe
@pytest.fixture(scope="module")
def DEF():

    return cbs.Cbs().parser('DEF')

def test_cbs_def_columns(DEF):
    assert DEF.columns.tolist() == ['Name', 'def_int', 'def_saftey', 'def_sk', 'tackles', 'fum_rec',
       'forced_fumbles', 'def_td', 'itd', 'ftd', 'pts_allowd','pass_yds_allowed', 'rush_yds_allowed', 'yds_allowed',
        'kick_rt_td']

#Test top and bottom names
def test_cbs_def_projection1(DEF):
    assert len(DEF.iloc[0].Name) <= 3

def test_cbs_def_projection2(DEF):
    assert len(DEF.iloc[1].Name) <= 3

def test_cbs_def_projection3(DEF):
    assert len(DEF.iloc[30].Name) <= 3

def test_cbs_def_projection4(DEF):
    assert len(DEF.iloc[31].Name) <= 3

#Test top and bottom Stats
def test_cbs_def_projection5(DEF):
    assert pd.to_numeric(DEF.iloc[0].def_int, errors='ignore') > 0

def test_cbs_def_projection6(DEF):
    assert pd.to_numeric(DEF.iloc[1].def_sk, errors='ignore') > 0

def test_cbs_def_projection7(DEF):
    assert pd.to_numeric(DEF.iloc[30].def_td, errors='ignore') > 0

def test_cbs_def_projection8(DEF):
    assert pd.to_numeric(DEF.iloc[31].yds_allowed, errors='ignore') > 0