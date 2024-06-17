Library Manager
Description
Library Manager est un système de gestion de bibliothèque simple implémenté en Python. Il permet aux utilisateurs d'ajouter, de supprimer, de rechercher et de lister des livres dans une bibliothèque. Ce projet est structuré pour démontrer les principes de base de la programmation orientée objet et des tests unitaires en Python.

Structure du Projet
markdown
Copier le code
library_manager/
├── library/
│   ├── __init__.py
│   ├── book.py
│   ├── library.py
├── tests/
│   ├── __init__.py
│   ├── test_book.py
│   ├── test_library.py
│   ├── test_integration.py
├── requirements.txt
└── README.md
Modules
library.book: Contient la classe Book représentant un livre avec un titre et un auteur.
library.library: Contient la classe Library qui gère une collection de livres.
Installation
Prérequis
Assurez-vous d'avoir Python 3.x installé. Vous pouvez le télécharger depuis le site officiel Python.

Étapes
Clonez le dépôt :

sh
Copier le code
git clone https://github.com/yourusername/library_manager.git
cd library_manager
Créez et activez un environnement virtuel (optionnel mais recommandé) :

sh
Copier le code
python -m venv venv
source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`
Installez les dépendances :

sh
Copier le code
pip install -r requirements.txt
Utilisation
Exemple
Voici un exemple rapide pour démontrer comment utiliser les classes Library et Book :

python
Copier le code
from library.book import Book
from library.library import Library

# Créer une instance de la bibliothèque
library = Library()

# Créer quelques instances de livres
book1 = Book("1984", "George Orwell")
book2 = Book("Brave New World", "Aldous Huxley")

# Ajouter des livres à la bibliothèque
library.add_book(book1)
library.add_book(book2)

# Lister tous les livres dans la bibliothèque
print(library.list_books())

# Trouver un livre par son titre
found_book = library.find_book_by_title("1984")
print(found_book)

# Supprimer un livre de la bibliothèque
library.remove_book(book1)

# Lister tous les livres à nouveau pour voir la liste mise à jour
print(library.list_books())
API de la Bibliothèque
Classe Book
Représente un livre avec un titre et un auteur.

Initialisation :

python
Copier le code
book = Book(title, author)
Attributs :

title (str) : Le titre du livre.
author (str) : L'auteur du livre.
Méthodes :

__str__() : Retourne une représentation en chaîne du livre au format "title by author".
Classe Library
Gère une collection de livres.

Initialisation :

python
Copier le code
library = Library()
Attributs :

books (list) : Une liste pour stocker les instances de livres.
Méthodes :

add_book(book) : Ajoute un livre à la bibliothèque.
remove_book(book) : Supprime un livre de la bibliothèque. Lève une exception ValueError si le livre n'est pas trouvé.
find_book_by_title(title) : Trouve et retourne un livre par son titre. Retourne None si le livre n'est pas trouvé.
list_books() : Retourne une liste de représentations en chaîne de tous les livres dans la bibliothèque.
Exécution des Tests
Tests Unitaires
Le projet inclut des tests unitaires pour les classes Book et Library. Pour exécuter les tests unitaires, utilisez la commande suivante :

sh
Copier le code
python -m unittest discover -s tests
Couverture des Tests
Les tests couvrent :

L'initialisation et la représentation en chaîne de Book.
L'ajout, la suppression, la recherche et la liste des livres dans Library.
Cas de Tests
test_book.py : Tests pour la classe Book.

test_book_initialization() : Teste l'initialisation d'un livre.
test_book_str() : Teste la représentation en chaîne d'un livre.
test_library.py : Tests pour la classe Library.

test_add_book() : Teste l'ajout d'un livre à la bibliothèque.
test_remove_book() : Teste la suppression d'un livre de la bibliothèque.
test_remove_book_not_in_library() : Teste la suppression d'un livre non présent dans la bibliothèque (doit lever une exception).
test_find_book_by_title() : Teste la recherche d'un livre par son titre.
test_find_book_by_title_not_found() : Teste la recherche d'un livre qui n'existe pas.
test_list_books() : Teste la liste de tous les livres dans la bibliothèque.
test_integration.py : Tests d'intégration pour les interactions entre Book et Library.

test_integration_add_and_find_book() : Teste l'ajout d'un livre et sa recherche par titre.
test_integration_add_and_remove_book() : Teste l'ajout puis la suppression d'un livre.
Intégration Continue
Ce projet utilise GitHub Actions pour l'intégration continue. Le fichier de workflow se trouve dans .github/workflows/python-app.yml. Les tests sont automatiquement exécutés à chaque push ou pull request.

Configuration de GitHub Actions
Créez un fichier de workflow dans .github/workflows/python-app.yml avec le contenu suivant :

yaml
Copier le code
name: Application Python

on: [push, pull_request]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        python -m unittest discover -s tests
Cette configuration garantit que vos tests sont automatiquement exécutés dans un environnement propre à chaque fois que vous poussez des modifications vers le dépôt.

Contribuer
Les contributions sont les bienvenues ! Veuillez suivre les étapes suivantes pour contribuer au projet :

Forkez le dépôt.
Créez une nouvelle branche (git checkout -b feature-branch).
Apportez vos modifications.
Commitez vos modifications (git commit -m 'Add new feature').
Poussez vers la branche (git push origin feature-branch).
Ouvrez une pull request.
Veuillez vous assurer de mettre à jour les tests si nécessaire et de suivre le style de code existant.

Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.