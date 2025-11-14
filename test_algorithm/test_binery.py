import Binery_Search
def test_binery() :
    l = list(range(1,101))
    assert Binery_Search.binery_search(l, 7)==True
    assert Binery_Search.binery_search(l, 0)==False
    assert Binery_Search.binery_search(l, 101)==False
    assert Binery_Search.binery_search(l, 50)==True
    assert Binery_Search.binery_search(l, 70)==True
    assert Binery_Search.binery_search(l, 17)==True
