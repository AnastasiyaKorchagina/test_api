import get_meas

class TestExample:

    def test_get_meas(self):
        result = get_meas.PaymentsController().get_meas()
        assert result.status_code == 200