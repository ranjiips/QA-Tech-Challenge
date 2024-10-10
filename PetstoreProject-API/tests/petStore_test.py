import logging
import pytest
import unittest

from pages.petDetails import PetDetails
from pages.storeDetails import PetStoreDetails
from utilities.readConfig import ConfigReader

# Execution Command:
# python -m pytest tests/petStore_test.py -v -s --html=reports/petStoreReport.html

@pytest.mark.store
class PetStoreTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.baseURL = ConfigReader.getBaseURL()
        self.pd = PetDetails()
        self.op = PetStoreDetails()

    @pytest.mark.orderPet
    @pytest.mark.run(order=1)
    def test_orderPet(self):
        print("*#" * 20)
        print("Order Pet from the store Test case")
        print("*#" * 20)
        addPetendPointURL = ConfigReader.get_addPetEndpoint()
        petID = self.pd.addNewPet(self.baseURL + addPetendPointURL)
        orderPetendPointURL = ConfigReader.get_placeOrderEndpoint()
        self.op.orderPetFromStore(self.baseURL + orderPetendPointURL, petID, 1)

    @pytest.mark.deleteOrder
    @pytest.mark.run(order=2)
    def test_deleteOrder(self):
        print("*#" * 20)
        print("Delete Order from the store Test case")
        print("*#" * 20)
        addPetendPointURL = ConfigReader.get_addPetEndpoint()
        petID = self.pd.addNewPet(self.baseURL + addPetendPointURL)
        orderPetendPointURL = ConfigReader.get_placeOrderEndpoint()
        orderID = self.op.orderPetFromStore(self.baseURL + orderPetendPointURL, petID, 1)
        deleteOrderEndPointURL = ConfigReader.get_deleteOrderEndpoint()
        self.op.deleteOrderById(self.baseURL + deleteOrderEndPointURL, orderID)



