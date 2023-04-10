import pytest
import requests

from jsonschema import validate


class TestsDogApi:
    dogapi_url = 'https://dog.ceo/api'

    breeds_list = {
        "message": {
            "affenpinscher": [],
            "african": [],
            "airedale": [],
            "akita": [],
            "appenzeller": [],
            "australian": [
                "shepherd"
            ],
            "basenji": [],
            "beagle": [],
            "bluetick": [],
            "borzoi": [],
            "bouvier": [],
            "boxer": [],
            "brabancon": [],
            "briard": [],
            "buhund": [
                "norwegian"
            ],
            "bulldog": [
                "boston",
                "english",
                "french"
            ],
            "bullterrier": [
                "staffordshire"
            ],
            "cattledog": [
                "australian"
            ],
            "chihuahua": [],
            "chow": [],
            "clumber": [],
            "cockapoo": [],
            "collie": [
                "border"
            ],
            "coonhound": [],
            "corgi": [
                "cardigan"
            ],
            "cotondetulear": [],
            "dachshund": [],
            "dalmatian": [],
            "dane": [
                "great"
            ],
            "deerhound": [
                "scottish"
            ],
            "dhole": [],
            "dingo": [],
            "doberman": [],
            "elkhound": [
                "norwegian"
            ],
            "entlebucher": [],
            "eskimo": [],
            "finnish": [
                "lapphund"
            ],
            "frise": [
                "bichon"
            ],
            "germanshepherd": [],
            "greyhound": [
                "italian"
            ],
            "groenendael": [],
            "havanese": [],
            "hound": [
                "afghan",
                "basset",
                "blood",
                "english",
                "ibizan",
                "plott",
                "walker"
            ],
            "husky": [],
            "keeshond": [],
            "kelpie": [],
            "komondor": [],
            "kuvasz": [],
            "labradoodle": [],
            "labrador": [],
            "leonberg": [],
            "lhasa": [],
            "malamute": [],
            "malinois": [],
            "maltese": [],
            "mastiff": [
                "bull",
                "english",
                "tibetan"
            ],
            "mexicanhairless": [],
            "mix": [],
            "mountain": [
                "bernese",
                "swiss"
            ],
            "newfoundland": [],
            "otterhound": [],
            "ovcharka": [
                "caucasian"
            ],
            "papillon": [],
            "pekinese": [],
            "pembroke": [],
            "pinscher": [
                "miniature"
            ],
            "pitbull": [],
            "pointer": [
                "german",
                "germanlonghair"
            ],
            "pomeranian": [],
            "poodle": [
                "medium",
                "miniature",
                "standard",
                "toy"
            ],
            "pug": [],
            "puggle": [],
            "pyrenees": [],
            "redbone": [],
            "retriever": [
                "chesapeake",
                "curly",
                "flatcoated",
                "golden"
            ],
            "ridgeback": [
                "rhodesian"
            ],
            "rottweiler": [],
            "saluki": [],
            "samoyed": [],
            "schipperke": [],
            "schnauzer": [
                "giant",
                "miniature"
            ],
            "segugio": [
                "italian"
            ],
            "setter": [
                "english",
                "gordon",
                "irish"
            ],
            "sharpei": [],
            "sheepdog": [
                "english",
                "shetland"
            ],
            "shiba": [],
            "shihtzu": [],
            "spaniel": [
                "blenheim",
                "brittany",
                "cocker",
                "irish",
                "japanese",
                "sussex",
                "welsh"
            ],
            "spitz": [
                "japanese"
            ],
            "springer": [
                "english"
            ],
            "stbernard": [],
            "terrier": [
                "american",
                "australian",
                "bedlington",
                "border",
                "cairn",
                "dandie",
                "fox",
                "irish",
                "kerryblue",
                "lakeland",
                "norfolk",
                "norwich",
                "patterdale",
                "russell",
                "scottish",
                "sealyham",
                "silky",
                "tibetan",
                "toy",
                "welsh",
                "westhighland",
                "wheaten",
                "yorkshire"
            ],
            "tervuren": [],
            "vizsla": [],
            "waterdog": [
                "spanish"
            ],
            "weimaraner": [],
            "whippet": [],
            "wolfhound": [
                "irish"
            ]
        },
        "status": "success"
    }

    schema = {
        'type': 'object',
        'properties': {
            'message': {'type': [
                'object',
                'string',
                'array',
            ]},
            'status': {'type': 'string'},
        },
    }

    def test_breeds_list(self):
        response = requests.get(f'{self.dogapi_url}/breeds/list/all')
        assert response.status_code == 200
        validate(instance=response.json(), schema=self.schema)

    def test_single_random_image(self):
        response = requests.get(f'{self.dogapi_url}/breeds/image/random')
        assert response.status_code == 200
        validate(instance=response.json(), schema=self.schema)

    @pytest.mark.parametrize('number', [0, 1, 20, 50])
    def test_multiple_random_images(self, number: int):
        response = requests.get(f'{self.dogapi_url}/breeds/image/random/{number}')
        assert response.status_code == 200
        validate(instance=response.json(), schema=self.schema)
        # посчитать количество картинок, которые вернулись

    @pytest.mark.parametrize('breed', [
        'affenpinscher',
    ])
    def test_all_images_by_breed(self, breed: str):
        response = requests.get(f'{self.dogapi_url}/breed/{breed}/images')
        assert response.status_code == 200
        validate(instance=response.json(), schema=self.schema)

    @pytest.mark.parametrize('number', [0, 1, 20, 50])
    @pytest.mark.parametrize('breed', [
        'affenpinscher',
    ])
    def test_images_by_breed(self, number: int, breed: str):
        url = f'{self.dogapi_url}/breed/{breed}/images/random'
        if number:
            response = requests.get(f'{url}/{number}')
            assert response.status_code == 200
            validate(instance=response.json(), schema=self.schema)
        else:
            response = requests.get(f'{url}')
            assert response.status_code == 200
            validate(instance=response.json(), schema=self.schema)
        # посчитать количество картинок, которые вернулись

    @pytest.mark.parametrize('breed', [
        'affenpinscher',
    ])
    def test_subbreed_list(self, breed):
        response = requests.get(f'{self.dogapi_url}/breed/{breed}/list')
        assert response.status_code == 200
        validate(instance=response.json(), schema=self.schema)

    @pytest.mark.parametrize('breed, subbreed', [
        ('hound', 'afghan'),
    ])
    def test_all_images_by_subbreed(self, breed: str, subbreed: str):
        response = requests.get(f'{self.dogapi_url}/breed/{breed}/{subbreed}/images')
        assert response.status_code == 200
        validate(instance=response.json(), schema=self.schema)

    @pytest.mark.parametrize('number', [0, 1, 20, 50])
    @pytest.mark.parametrize('breed, subbreed', [
        ('hound', 'afghan'),
    ])
    def test_all_images_by_subbreed(self, breed: str, subbreed: str, number: int):
        url = f'{self.dogapi_url}/breed/{breed}/{subbreed}/images/random'
        if number:
            response = requests.get(f'{url}/{number}')
            assert response.status_code == 200
            validate(instance=response.json(), schema=self.schema)
        else:
            response = requests.get(f'{url}')
            assert response.status_code == 200
            validate(instance=response.json(), schema=self.schema)
    # посчитать количество картинок, которые вернулись
