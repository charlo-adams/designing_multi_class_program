from lib.contact_entry import * 

def test_new_contact_can_be_made():
    new_contact = Contacts("Nikki: 079573957673")
    assert new_contact.number == "Nikki: 079573957673"
