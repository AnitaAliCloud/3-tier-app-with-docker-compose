# 3-Tier App with Docker Compose 

A simple web app split into 3 parts — Frontend, Backend, and Database — all running together with Docker.

---

## What Does It Do?

It shows a list of users on a webpage. That's it!
But instead of one big program, 3 separate services work together to make it happen:

```
Browser → Frontend (shows the page)
               → Backend (fetches the data)
                     → Database (stores the data)
```

---

## The 3 Services

| Service | Technology | Job |
|---------|-----------|-----|
| Frontend | Python + Flask | Shows the webpage to the user |
| Backend | Python + Flask | Talks to the database and returns data |
| Database | MySQL 8 (from DockerHub) | Stores the users |

---

## How to Run It

Make sure Docker Desktop is running, then:

```bash
# Start everything
docker compose up --build

# Open in browser
http://localhost:3000
```

To stop:
```bash
docker compose down
```

To stop and wipe the database:
```bash
docker compose down -v
```

---

## Project Structure

```
project/
├── frontend/        → webpage code
├── backend/         → API code
├── db/
│   └── init.sql     → creates the users table on first run
├── docker-compose.yml
└── .env             → passwords (never share this file!)
```

---

## The `.env` File

Create this file in the project root before running:

```bash
DB_USER=admin
DB_PASSWORD=secret
DB_NAME=myapp
DB_ROOT_PASSWORD=rootsecret
```

>  Never commit this file to GitHub. It contains passwords.

---

## Common Errors

| Error | Fix |
|-------|-----|
| `address already in use: 5000` | change the port in `docker-compose.yml` ports: "5001:5000" |
| `Table 'myapp.users' doesn't exist` | Run `docker compose down -v` then `docker compose up --build` |
