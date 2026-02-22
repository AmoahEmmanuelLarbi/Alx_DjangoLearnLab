📚 Role-Based Permissions System
Overview

This application uses Django’s built-in Group and Permission system to implement Role-Based Access Control (RBAC).

There are three roles:

Admins

Editors

Viewers

Each role is mapped to a Django Group, and permissions are assigned programmatically using signals.

🔐 Permission Structure

The Book model uses Django’s automatic permissions:

add_book

change_book

delete_book

view_book

We map these to role-based logical permissions:

Logical Permission	Django Permission
can_create	add_book
can_edit	change_book
can_delete	delete_book
can_view	view_book
👥 Groups and Their Permissions
🛡 Admins

can_create

can_edit

can_delete

can_view

Admins have full control over books.

✏ Editors

can_create

can_edit

can_view

Editors can modify and create books but cannot delete them.

👀 Viewers

can_view

Viewers can only see books.