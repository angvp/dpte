from django.core.urlresolvers import reverse


def test_change_settings(settings):
    # despues de que este test corre se resetea el settings de nuevo
    settings.DATE_FORMAT = 'd-m-Y'


def test_index(client):
    # client es una instancia de django.test.TestCase.TestClient
    url = reverse('index')
    rq = client.get(url)
    assert rq.status_code == 200
