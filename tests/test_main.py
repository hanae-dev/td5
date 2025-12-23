from main import greet

def test_greet():
    # Vérifie que greet retourne la bonne chaîne
    assert greet("Alice") == "Hello Alice"
    assert greet("Hanae") == "Hello Hanae"
