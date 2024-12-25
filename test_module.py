import pytest
from mean_var_std import calculate

def test_calculate():
    # تست ورودی‌های معتبر
    result = calculate([0,1,2,3,4,5,6,7,8])
    assert result['mean'] == [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0]
    assert result['variance'] == [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667]
    assert result['standard deviation'] == [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611]
    assert result['max'] == [[6, 7, 8], [2, 5, 8], 8]
    assert result['min'] == [[0, 1, 2], [0, 3, 6], 0]
    assert result['sum'] == [[9, 12, 15], [3, 12, 21], 36]
    
    # تست ورودی‌های نامعتبر
    with pytest.raises(ValueError):
        calculate([1, 2, 3])  # کمتر از 9 عدد
    
    with pytest.raises(ValueError):
        calculate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # بیشتر از 9 عدد
