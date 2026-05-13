# Data Model

## Entity 1: User

| Field       | Type      | Description                        |
|-------------|-----------|------------------------------------|
| id          | UUID      | Primary key                        |
| email       | String    | Unique user email                  |
| password    | String    | Hashed password                    |
| created_at  | Timestamp | Account creation date              |

## Entity 2: Decision

| Field       | Type      | Description                        |
|-------------|-----------|------------------------------------|
| id          | UUID      | Primary key                        |
| user_id     | UUID      | Foreign key referencing User       |
| title       | String    | Short decision title               |
| description | Text      | Full decision context              |
| voted_option| String    | User final choice (Pro or Con)     |
| created_at  | Timestamp | Decision creation date             |

## Entity 3: Argument

| Field       | Type      | Description                        |
|-------------|-----------|------------------------------------|
| id          | UUID      | Primary key                        |
| decision_id | UUID      | Foreign key referencing Decision   |
| type        | Enum      | Pro or Con                         |
| content     | Text      | Argument description               |
| source      | Enum      | AI-generated or User-added         |

## Relationships
- One User has many Decisions
- One Decision has many Arguments
