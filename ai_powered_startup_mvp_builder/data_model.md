# Data Model

## Entity 1: User

| Field       | Type      | Description                        |
|-------------|-----------|------------------------------------|
| id          | UUID      | Primary key                        |
| email       | String    | Unique user email                  |
| password    | String    | Hashed password                    |
| created_at  | Timestamp | Account creation date              |

## Entity 2: Task

| Field       | Type      | Description                        |
|-------------|-----------|------------------------------------|
| id          | UUID      | Primary key                        |
| user_id     | UUID      | Foreign key referencing User       |
| category_id | UUID      | Foreign key referencing Category   |
| title       | String    | Short task title                   |
| description | Text      | Detailed task description          |
| status      | Enum      | To Do, In Progress, Done           |
| priority    | Enum      | Low, Medium, High                  |
| due_date    | Date      | Task deadline                      |
| created_at  | Timestamp | Task creation date                 |

## Entity 3: Category

| Field       | Type      | Description                        |
|-------------|-----------|------------------------------------|
| id          | UUID      | Primary key                        |
| user_id     | UUID      | Foreign key referencing User       |
| name        | String    | Category name (e.g. Work, Personal)|
| color       | String    | Hex color code for UI display      |

## Relationships
- One User has many Tasks
- One User has many Categories
- One Category has many Tasks
