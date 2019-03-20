import os
import sys
import json
import requests
import pprint
from dotenv import load_dotenv

sys.path.append("../")
from app import db
from models import Dog
load_dotenv()
pp = pprint.PrettyPrinter(indent=2)

PETFINDER_KEY = os.getenv("PETFINDER_API_KEY")
PETFINDER_SECRET = os.getenv("PETFINDER_API_SECRET")
API_URL = "http://api.petfinder.com/"

VALID_BREEDS = {'norfolk terrier', 'doberman pinscher', 'boxer', 'pug', 'bichon frise', 'bull terrier', 'briard', 'beagle', 'tibetan mastiff', 'shih tzu', 'field spaniel', 'keeshond', 'english springer spaniel', 'staffordshire bull terrier', 'australian terrier', 'german pinscher', 'black and tan coonhound', 'norwich terrier', 'cairn terrier', 'soft coated wheaten terrier', 'pembroke welsh corgi', 'english toy terrier', 'great pyrenees', 'alaskan husky', 'thai ridgeback', 'shetland sheepdog', 'irish terrier', 'appenzeller sennenhund', 'toy fox terrier', 'tibetan spaniel', 'american pit bull terrier', 'lhasa apso', 'boykin spaniel', 'standard schnauzer', 'miniature pinscher', 'miniature schnauzer', 'yorkshire terrier', 'border collie', 'west highland white terrier', 'samoyed', 'american eskimo dog', 'bearded collie', 'smooth fox terrier', 'bluetick coonhound', 'shiba inu', 'english toy spaniel', 'australian cattle dog', 'cocker spaniel', 'great dane', 'coton de tulear', 'tibetan terrier', 'old english sheepdog', 'affenpinscher', 'pharaoh hound', 'scottish deerhound', 'cocker spaniel (american)', 'welsh springer spaniel', 'rottweiler', 'australian kelpie', 'chow chow', 'american bulldog', 'treeing walker coonhound', 'vizsla', 'chesapeake bay retriever', 'belgian malinois', 'siberian husky', 'saluki', 'whippet', 'kuvasz', 'cardigan welsh corgi', 'maltese', 'irish setter', 'rat terrier', 'scottish terrier', 'border terrier', 'komondor', 'bull terrier (miniature)', 'pomeranian', 'alaskan malamute', 'clumber spaniel', 'schipperke', 'redbone coonhound', 'bernese mountain dog', 'rhodesian ridgeback', 'basset hound', 'greyhound', 'wire fox terrier', 'cavalier king charles spaniel', 'english setter', 'alapaha blue blood bulldog', 'papillon', 'irish wolfhound', 'french bulldog', 'golden retriever', 'bedlington terrier', 'nova scotia duck tolling retriever', 'airedale terrier', 'german shorthaired pointer', 'boston terrier', 'newfoundland', 'italian greyhound', 'giant schnauzer', 'american staffordshire terrier', 'american water spaniel', 'afghan hound', 'weimaraner', 'silky terrier', 'labrador retriever', 'dalmatian', 'glen of imaal terrier', 'basset bleu de gascogne', 'gordon setter', 'akita', 'basenji'}

def delete_dogs():
    """
    TODO
    """
    Dog.query.delete()
    db.session.commit()



# TODO: Pagination to keep getting dogs?
# TODO: Get dogs by shelter rather than by this API call? Consider this after database is set up.
def get_dogs(location = "texas", count = 1000, offset = 0):
    """
    Interfaces with petfinder api to get relevant pet info local to a certain
    zipcode
    location - string, state
    count - int, number of results to return
    offset - int, where to start
    """
    payload = {"key" : PETFINDER_KEY, "animal" : "dog",
               "location" : str(location), "offset" : str(offset),
               "count" : str(count), "format" : "json"}

    response = requests.get(API_URL + "pet.find", params=payload)

    if response.status_code == 200:
        response_obj = json.loads(response.text)
        pet_dict = response_obj["petfinder"]["pets"]["pet"]
        return pet_dict
    else:
        print("Request to get details about dogs failed.")




def build_dog(pet):
    """
    Builds a dog dict from petfinder data
    """
    if (pet == {}):
        return None

    breed = ""

    if isinstance(pet["breeds"]["breed"], dict):
        breed = pet["breeds"]["breed"]["$t"]
    else:
        breed = pet["breeds"]["breed"][0]["$t"]

    if "photos" not in pet["media"]:
        return None

    if breed.lower() not in VALID_BREEDS:
        # Manual fixing of inconsistent breeds
        # TODO: Find more manual fixes for hounds
        manual_fix = False
        if breed.lower() == "pit bull terrier":
            breed = "american pit bull terrier"
            manual_fix = True
        if breed.lower() == "australian cattle dog / blue heeler" or breed.lower() == "cattle dog":
            breed = "australian cattle dog"
            manual_fix = True
        if breed.lower() == "collie":
            breed = "border collie"
            manual_fix = True

        if (not manual_fix):
            return None

    images = {"image_1": None,
              "image_2": None,
              "image_3": None,
              "image_4": None,
              }

    pic_id = 0
    for picture in pet["media"]["photos"]["photo"]:
        if int(picture['@id']) > pic_id and picture['@size'] == 'x' and pic_id < 4:
            pic_id += 1
            images["image_" + str(pic_id)] = picture["$t"]

    # TODO: Add "options" (noKids houseTrained, hasShots, etc)
    dog = Dog(
        id = pet['id']['$t'],
        shelter_id = pet['shelterId']['$t'],
        name = pet['name']['$t'],
        breed = breed.lower(),
        age = pet['age']['$t'],
        size = pet['size']['$t'],
        sex = pet['sex']['$t'],
        description = pet['description']['$t'] if '$t' in pet['description'] else None,
        image_1 = images["image_1"],
        image_2 = images["image_2"],
        image_3 = images["image_3"],
        image_4 = images["image_4"],
        )

    db.session.add(dog)
    db.session.commit()


def main():
    """
    Seeds database with records of local dogs based on Texas Zip Codes
    """
    delete_dogs()
    print("Previos dogs deleted from database!")

    dog_dict = get_dogs()
    for dog in dog_dict:
        build_dog(dog)

    print("Dog seeding complete!")

if __name__ == "__main__":
    main()