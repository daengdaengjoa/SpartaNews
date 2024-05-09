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
- Frontend Development:
Main Page:
Implemented sorting functionality.
Detail Page:
Implemented detail page.
- **김예은** :
accounts login/out functionality,
Comment CRUD operations
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
![image](https://github.com/daengdaengjoa/SpartaNews/assets/156053546/b1e7eb57-53b7-494e-9059-258a4fbdaba5)

시연영상
[ttps://www.youtube.com/watch?v=lOL_L8jN1uk](https://www.youtube.com/watch?v=JPraElNvQ0U)
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
| Endpoint                                                            | Method | Description                                                  | Request Body Data                                                           |
|---------------------------------------------------------------------|--------|--------------------------------------------------------------|-----------------------------------------------------------------------------|
| `/api/accounts/signup/`                                             | POST   | 회원가입                                                      | - {"username":ID, "password":PASSWORD}                                      |
| `/api/accounts/login/`                                              | POST   | 로그인                                                        | - {"username":ID, "password":PASSWORD}                                      |
| `/api/accounts/logout/`                                             | POST   | 로그아웃                                                      | -                                                                           |
| `/api/accounts/login/refresh/`                                      | POST   | 토큰 재발급                                                   | - {"refresh_Token":refresh_Token}                                           |
| `/api/articles/`                                                    | GET    | 게시글 목록 조회                                              | -                                                                           |
|                                                                     | POST   | 게시글 생성                                                   | - {"title": title, "content": content, "url": url, "category": category}    |
| `/api/articles/<int:article_id>/`                                   | GET    | 게시글 조회                                                   | -                                                                           |
|                                                                     | PUT    | 게시글 수정                                                   | - {"title": title, "content": content}                                      |
|                                                                     | DELETE | 게시글 삭제                                                   | -                                                                           |
| `/api/articles/<int:article_id>/like/`                              | POST   | 게시글 좋아요                                                 | -                                                                           |
| `/api/articles/<int:article_id>/comments/`                          | GET    | 댓글 조회(한 게시글)                                          | -                                                                            |
|                                                                     | POST   | 댓글 생성                                                     | - {"content":content}                                                       |
| `/api/articles/<int:article_id>/comments/<int:comment_id>/`         | PUT    | 댓글 수정                                                     | - {"content":content}                                                       |
|                                                                     | DELETE | 댓글 삭제                                                     | -                                                                           |
| `/api/articles/<int:article_id>/comments/<int:comment_id>/like/`    | POST   | 댓글 좋아요                                                   | -                                                                           |


