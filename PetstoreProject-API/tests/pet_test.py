import logging
import pytest
import unittest

from pages.petDetails import PetDetails
from utilities.readConfig import ConfigReader

# Execution Command:
# python -m pytest tests/pet_test.py -v -s --html=reports/petReport.html

@pytest.mark.pet
class PetTests(unittest.TestCase):
    petID = None  # Class-level attribute to store petID

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.baseURL = ConfigReader.getBaseURL()
        self.pd = PetDetails()

    @pytest.mark.addPet
    @pytest.mark.run(order=1)
    def test_addPet(self):
        print("*#" * 20)
        print("Add Pet Test case")
        print("*#" * 20)
        endPointURL = ConfigReader.get_addPetEndpoint()
        PetTests.petID = self.pd.addNewPet(self.baseURL + endPointURL)  # Store petID in class-level attribute
        print(f"Pet Id: {PetTests.petID}")

    @pytest.mark.getPet
    @pytest.mark.run(order=2)
    def test_getPetByID(self):
        print("*#" * 20)
        print("Get Pet by ID")
        print("*#" * 20)
        endPointURL = ConfigReader.get_findPetByIDEndpoint()
        if PetTests.petID is None:
            PetTests.petID = 9223372036854349804
        self.pd.getPetById(self.baseURL + endPointURL, PetTests.petID)  # Use class-level attribute

    @pytest.mark.getPet
    @pytest.mark.run(order=3)
    def test_getPetByStatus(self):
        print("*#" * 20)
        print("Get Pet by Status")
        print("*#" * 20)
        endPointURL = ConfigReader.get_findPetByStatusEndpoint()
        self.pd.getPetByStatus(self.baseURL + endPointURL, "pending")

    @pytest.mark.getPet
    @pytest.mark.negative
    @pytest.mark.run(order=4)
    def test_getPetByInvalidID(self):
        print("*#" * 20)
        print("Get Pet by Invalid ID")
        print("*#" * 20)
        endPointURL = ConfigReader.get_findPetByIDEndpoint()
        self.pd.getPetById(self.baseURL + endPointURL, 123456789)
