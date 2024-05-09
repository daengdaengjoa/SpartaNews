# 📰 Sparta News

## 📢 Project Overview
Sparta News is a Django-based news platform that provides users with news articles from various categories. This platform not only allows users to find and read news but also enables them to share opinions and interact through social features.

## 🔧 Update Summary
- Implemented various sorting options to enhance user experience.
- Introduced a token-based authentication system to ensure secure user authentication during signup, login, and profile access.

## 👨‍🏫 Project Introduction
Sparta News is designed to provide users with convenient and trustworthy news content. Users can search and read news articles from diverse categories, share their opinions, and interact through social features.

The platform offers robust management capabilities for administrators to maintain platform integrity by managing content and user interactions.

With its user-friendly interface, advanced search options, and enhanced authentication system, Sparta News aims to be the most convenient choice for users seeking reliable news content.

## ⏲️ Development time
- 2024.05.03(금) ~ 2023.05.10(금)
- update:  ~ 2023.05.10(금)
- 아이디어 노트 작성
- 아이디어 발표
- 와이어프레임 및 SA문서 작성
- 기능구현
- 발표
<br>

## 🧑‍🤝‍🧑 Development Team: Team-13
- **김준수** : 
sorting functionality,
Search functionality,
Pagination

- **김예은** : 
- **신지혜** :
Article CRUD operations
Like feature

- **전관** :
Article CRUD operations,
Comment CRUD operations,
Token-Based Authentication,
Administrator permissions 


<br>

## 💻 Development Environment
- **Programming Language** : Python 3.x
- **Web Framework** : Django
- **Template Engine** : Django template
- **Database** : SQLite (for development and testing)
- **IDE** : Visual Studio Code
- **Version Control** : Git, GitHub
<br>

## ⚙️ Technology Stack
- **Frontend** : HTML, CSS, JavaScript
- **Backend** : Django
- **Database ORMR** : Django ORM
- **Idea Brainstorming Tools and Environments** : Slack, Zep, Notion, figma
<br>

## 📝 Project Architecture
S.A. 노션 : https://www.notion.so/teamsparta/S-A-11d6d27e54ae40758ac8178f061822ea
![image](https://github.com/daengdaengjoa/SpartaNews/assets/156053546/8547e415-0d92-4e57-a06e-7449ab26c5b0)
![image](https://github.com/daengdaengjoa/SpartaNews/assets/156053546/36ef5e02-fb65-41ec-a057-eec4d1b9d727)

시연영상
https://www.youtube.com/watch?v=lOL_L8jN1uk
<br>

## 📌 Key Features

### 1. Article CRUD
   - Users can create, read, update, and delete articles.
   - Permissions: Only authenticated users can perform CRUD operations on articles.

### 2. Comment CRUD
   - Users can create, read, update, and delete comments on articles.
   - Comments are displayed at the bottom of each article's detail page.
   - Permissions: Only authenticated users can create or edit comments.

### 3. Like Feature
   - Users can like or dislike articles.
   - Permissions: Only authenticated users can like or dislike articles.

### 4. Search Functionality
   - Users can search for articles by title, content, or author name.
   - Search results are displayed on the search results page.

### 5. Pagination
   - Pagination is implemented to display a limited number of articles per page.

### 6. Token-Based Authentication
   - Token-based authentication is used to ensure secure user authentication during signup, login, and profile access.

### 7. Administrator Permissions
   - Administrators with specific IDs have the authority to edit or delete articles and comments.

### 8. Personalized Recommendations
   - User behavior data is utilized to provide personalized article recommendations.


<br> 

## ✒️ API
| Endpoint                                   | Method | Description                                                  | Request Body Data                                                   | Response Code       |
|--------------------------------------------|--------|--------------------------------------------------------------|---------------------------------------------------------------------|---------------------|
| `/api/articles/`                          | GET    | Retrieve a list of all articles.                             | -                                                                   | 200 OK              |
|                                            | POST   | Create a new article. Requires authentication.              | `{ "title": "Article Title", "content": "Article Content" }`       | 201 Created        |
| `/api/articles/<pk>`                      | GET    | Retrieve details of a specific article.                      | -                                                                   | 200 OK              |
|                                            | PUT    | Update details of a specific article. Requires authentication.| `{ "title": "Updated Title", "content": "Updated Content" }`       | 200 OK              |
|                                            | DELETE | Delete a specific article. Requires authentication.         | -                                                                   | 204 No Content      |
| `/api/articles/<pk>/like/`                | POST   | Like or unlike a specific article. Requires authentication.| -                                                                   | 200 OK              |
| `/api/articles/<pk>/comments/`            | GET    | Retrieve comments for a specific article.                    | -                                                                   | 200 OK              |
|                                            | POST   | Create a new comment for a specific article. Requires authentication. | `{ "content": "Comment Content" }`                             | 201 Created        |
| `/api/articles/<pk>/comments/<comment_id>/`| PUT    | Update a specific comment. Requires authentication.         | `{ "content": "Updated Comment Content" }`                       | 200 OK              |
|                                            | DELETE | Delete a specific comment. Requires authentication.         | -                                                                   | 204 No Content      |
| `/api/articles/<pk>/comments/<comment_id>/like/` | POST | Like or unlike a specific comment. Requires authentication. | -                                                                   | 200 OK              |
| `/api/signup/`                            | POST   | Register a new user. Returns a message upon successful registration. Requires authentication. | `{ "username": "Username", "password": "Password" }`          | 201 Created        |
| `/api/profile/<username>/`                | GET    | Retrieve the profile of a specific user. Requires authentication. | -                                                                   | 200 OK              |


