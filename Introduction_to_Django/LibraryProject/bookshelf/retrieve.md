# Documentation for retrieving data from model
from bookshelf.models import Book

```
book = Book.objects.get(id = 1)
print(book.__dict__)


{'_state': <django.db.models.base.ModelState object at 0x000001CE25E93B10>, 'id': 2, 'title': 'Atomic Habits', 'author': 'James Clear', 'publication_year': 1990}
```
