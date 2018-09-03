from cbs import cbs
import pandas as pd
import pytest

#Get the CBS K dataframe
@pytest.fixture(scope="module")
def K():
    return cbs.Cbs().parser('K')

def test_cbs_k_columns(K):
    assert K.columns.tolist() == ['Name', 'fg', 'fg_att', 'fg_lng', 'PAT_made', 'PAT_att', 'PAT_blckd',
                                  '1-19', '20-29', '30-39', '40-49', '1-49','50+']
#Test top and bottom names
def test_cbs_k_projection1(K):
    assert type(K.iloc[0].Name) == str

def test_cbs_k_projection2(K):
    assert type(K.iloc[1].Name) == str

def test_cbs_k_projection3(K):
    assert type(K.iloc[20].Name) == str

def test_cbs_k_projection4(K):
    assert type(K.iloc[21].Name) == str

#Test top and bottom Stats
def test_cbs_k_projection5(K):
    assert pd.to_numeric(K.iloc[0].fg, errors='ignore') > 0

def test_cbs_k_projection6(K):
    assert pd.to_numeric(K.iloc[1].fg_att, errors='ignore') > 0

def test_cbs_k_projection7(K):
    assert pd.to_numeric(K.iloc[21].PAT_made, errors='ignore') > 0

def test_cbs_k_projection8(K):
    assert pd.to_numeric(K.iloc[20].fg_lng, errors='ignore') >= 0
