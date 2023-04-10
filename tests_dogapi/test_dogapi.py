import pytest
import requests


class TestsDogApi:
    dogapi_url = 'https://dog.ceo/api'

    def test_breeds_list(self):
        response = requests.get(f'{self.dogapi_url}/breeds/list/all')
        assert response.status_code == 200

    def test_single_random_image(self):
        response = requests.get(f'{self.dogapi_url}/breeds/image/random')
        assert response.status_code == 200

    @pytest.mark.parametrize('number', [0, 1, 20, 50])
    def test_multiple_random_images(self, number: int):
        response = requests.get(f'{self.dogapi_url}/breeds/image/random/{number}')
        assert response.status_code == 200
        # посчитать количество картинок, которые вернулись

    @pytest.mark.parametrize('breed', [
        'affenpinscher',
    ])
    def test_all_images_by_breed(self, breed: str):
        response = requests.get(f'{self.dogapi_url}/breed/{breed}/images')
        assert response.status_code == 200

    @pytest.mark.parametrize('number', [0, 1, 20, 50])
    @pytest.mark.parametrize('breed', [
        'affenpinscher',
    ])
    def test_images_by_breed(self, number: int, breed: str):
        url = f'{self.dogapi_url}/breed/{breed}/images/random'
        if number:
            response = requests.get(f'{url}/{number}')
            assert response.status_code == 200
        else:
            response = requests.get(f'{url}')
            assert response.status_code == 200
        # посчитать количество картинок, которые вернулись

    @pytest.mark.parametrize('breed', [
        'affenpinscher',
    ])
    def test_subbreed_list(self, breed):
        response = requests.get(f'{self.dogapi_url}/breed/{breed}/list')
        assert response.status_code == 200

    @pytest.mark.parametrize('breed, subbreed', [
        ('hound', 'afghan'),
    ])
    def test_all_images_by_subbreed(self, breed: str, subbreed: str):
        response = requests.get(f'{self.dogapi_url}/breed/{breed}/{subbreed}/images')
        assert response.status_code == 200

    @pytest.mark.parametrize('number', [0, 1, 20, 50])
    @pytest.mark.parametrize('breed, subbreed', [
        ('hound', 'afghan'),
    ])
    def test_all_images_by_subbreed(self, breed: str, subbreed: str, number: int):
        url = f'{self.dogapi_url}/breed/{breed}/{subbreed}/images/random'
        if number:
            response = requests.get(f'{url}/{number}')
            assert response.status_code == 200
        else:
            response = requests.get(f'{url}')
            assert response.status_code == 200
    # посчитать количество картинок, которые вернулись
